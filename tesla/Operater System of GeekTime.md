### Test

1. ABC 对D不太理解，没有使用过
2. ABC 
3. B
4. 
5. BC
6. A
7. BC
8. BD
9. C
10.
11. AD
12. BD

### 推荐书籍
OSTEP(Operating System Three Easy Picies)

### 趣谈操作系统中的外包对应名词
* 项目运行体系 -- 祖宗进程
* 会议室 -- 内存
* 会议室管理系统 -- 内存管理系统
* 项目执计划书 -- 代码段
* 会议记录 -- 数据段
* 
    



### 从入门到放弃-- Linux六大山坡
#### 第一个坡： 抛弃旧的思维习惯， 熟练使用Linux命令行
    鸟哥的Linux私房菜
    LInux系统管理技术手册
#### 第二个坡：通过系统调用或者 glibc，学会自己进行程序设计
    UNIX环境高级编程

#### 



### 基本Linux命令
![](https://static001.geekbang.org/resource/image/88/e5/8855bb645d8ecc35c80aa89cde5d16e5.jpg)


###  部分系统调用
#### 进程管理（立项服务）
1. Linux中父进程调用fork创建子进程。
2. 父进程调用fork时，子进程拷贝所有父进程的数据接口和代码过来。
3. 当前进程是子进程，fork返回0；当前进程是父进程，fork返回子进程进程号
4. 如果返回0，说明当前进程是子进程，子进程请求execve系统调用，执行另一个程序。
5. 如果返回子进程号，说明当前进程是父进程，按照原父进程原计划执行。
6. 父进程要对子进程负责，调用waitpid将子进程进程号作为参数，父进程就能知道子进程运行完了没有，成功与否。
7. 操作系统启动的时候先创建了一个所有用户进程的“祖宗进程”，课时1，第3题A选项：0号进程是所有用户态进程的祖先
* fork 创建进程
* execve 执行另一个程序的系统调用
* waitpid 父进程调用判断子进程是否执行完毕
#### 内存管理（会议室管理）
* brk 分配连续小内存
* mmap 分配连续大内存
#### 文件管理（档案资料库管理）
一切皆是文件： （程序文件（二进制文件）、文本文件、标准输入输出文件、管道文件、
Socket、设备、文件夹等皆是文件
* open 打开文件
* close 关闭文件
* creat 创建文件
* lseek 跳到文件的指定位置
* read 文件读取
* write 文件写入

![](https://static001.geekbang.org/resource/image/e4/df/e49b5c2a78ac09903d697126bfe6c5df.jpeg)

#### 信号处理
* kill 终止一个进程
* sigaction 注册一个信号处理函数

####  进程通信（项目间沟通）
当进程间发送较小的信息时，使用消息队列方式，消息队列存在于内核中
* msgget 创建一个新的队列
* msgsnd 将消息发送到消息队列
* msgrcv 从队列中读取消息
当进程间需要交互的信息较大时，使用共享内存的方式，即两个项目共享了一个会议室
* shmget 创建一个共享内存块
* shmat 将共享内存映射到自己的内存控件，就可以开始读写
注： 共享内存需要注意数据竞争问题（两个进程同时读写数据），由此引出信号量机制

信号量机制Semaphore
>对于只允许一个人访问的需求，我们可以将信号量设为 1。当一个人要访问的时候，
先调用sem_wait。如果这时候没有人访问，则占用这个信号量，他就可以开始访问了。
如果这个时候另一个人要访问，也会调用 sem_wait。由于前一个人已经在访问了，
所以后面这个人就必须等待上一个人访问完之后才能访问。当上一个人访问完毕后，
会调用sem_post将信号量释放，于是下一个人等待结束，可以访问这个资源了。

#### 网络通信（公司间沟通）
不同机器间进行网络通信，需要遵循相同的网络协议,即TCP/IP网络协议栈。
Linux内核实现了网络协议栈

网络服务是通过Socket来提供服务的。Socket可以比作一个插槽，双方通信之间都需要建立一个Socket
Socket，也是一个文件，也有一个文件描述符。

#### 查看源代码的系统调用

unistd_64.h
```
#define __NR_restart_syscall	  0
#define __NR_exit		  1
#define __NR_fork		  2
#define __NR_read		  3
#define __NR_write		  4
#define __NR_open		  5
#define __NR_close		  6
#define __NR_waitpid		  7
#define __NR_creat		  8
......

```

#### glibc
##### glibc是Linux下开源标准C库
##### glibc把系统调用进一步封装

##### sys_open对应glibc的open函数
##### 一个单独的glibcAPI可能调用多个系统调用
##### printf函数调用sys_open、sys_mmap、sys_write、sys_close等等系统调用


#### 总结系统调用图
![](../assets/images/系统调用命令.jpg)    




 



