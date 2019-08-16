
### 总结
1. 当$后面的字符串不是代表一个变量时，默认返回空,即使在字符串内也是一样

        (.airflow) bamboo@ubuntu:~$ echo "$sdfsdfawq"
        
        (.airflow) bamboo@ubuntu:~$ echo $sdfsdfawq
        
        (.airflow) bamboo@ubuntu:~$ echo $sf
        
        (.airflow) bamboo@ubuntu:~$  

    



##　Bash Shell命令
### sed


#### N


#### :a、ta.
他们是一对符号，:a是先做一个标记，然后如果ta之前执行成功，则跳转到:a标识符继续执行，达到了循环的效果。
```
有如下分行的数据：
|      32742 |
|      39013 |
|     481472 |
|     481658 |
|     481885 |
     把格式转换为：32742,39013,481337,481472,481658,481885
     
cat tt | awk '{print $2}' | sed ":a;N;s/\n/,/g;ta"
```
解释: N命令将12、34行用\n拼接在一起，然后循环使用,将\n替换，


### 各个括号以及和$组合的用法
参考：[Linux Shell 基础 -- 总结几种括号、引号的用法](https://zhuanlan.zhihu.com/p/64953183)
#### 单小括号的作用()
1. $() 和 `` 类似，都表示命令替换(将内部命令的执行结果替换到对应位置)
```
a=$(ls) 
echo

 result: 
airflow Aristotle Desktop Documents Downloads examples.desktop Music Pictures Public runtime Templates Videos Winners

```
2. 开辟子shell执行一组命令，命令内部的变量不会影响到外部，但打印输入等会显示到控制台
3. 定义数组

#### 单中括号的作用[]，等价于test
1. []和test一样，用文本符号来表示数值的比较， 用数学符号表示字符串的比较
2. 使用[]和test时，变量尽量使用“”括起来，避免变量未生命而报错
数值比较

    -eq	等于则为真
    -ne	不等于则为真
    -gt	大于则为真
    -ge	大于等于则为真
    -lt	小于则为真
    -le	小于等于则为真
    
    eg:
    num1=100
    num2=100
    if test $[num1] -eq $[num2]
    then
        echo '两个数相等！'
    else
        echo '两个数不相等！'
    fi

字符比较 

    =	等于则为真
    !=	不相等则为真
    -z 字符串	字符串的长度为零则为真
    -n 字符串	字符串的长度不为零则为真
    
    num1="ru1noob"
    num2="runoob"
    if test $num1 = $num2
    then
        echo '两个字符串相等!'
    else
        echo '两个字符串不相等!'
    fi
注意： 大于符号或小于符号必须要转义，否则将理解为重定向，且只能用来做字符比较 \
必须在左括号的右侧和右括号的左侧各加一个空格，否则会报错。

文件测试
    
    -e 文件名	如果文件存在则为真
    -r 文件名	如果文件存在且可读则为真
    -w 文件名	如果文件存在且可写则为真
    -x 文件名	如果文件存在且可执行则为真
    -s 文件名	如果文件存在且至少有一个字符则为真
    -d 文件名	如果文件存在且为目录则为真
    -f 文件名	如果文件存在且为普通文件则为真
    -c 文件名	如果文件存在且为字符型特殊文件则为真
    -b 文件名	如果文件存在且为块特殊文件则为真
    
    cd /bin
    if test -e ./bash
    then
        echo '文件已存在!'
    else
        echo '文件不存在!'
    fi

####  双中括号的作用[[]]
1. 字符串比较拓展了通配符匹配， 当右侧字符串没有使用引号时，将进行通配符匹配
2. 对逻辑运算符直接支持， $$, || , > < 等等
3. 变量没有声明且没有使用引号引起来时，将进行通配符匹配 ## 这句话经过测试不成立
4. 变量没有声明且没有使用引号，默认返回空字符串，自我理解

#### $+中括号 $[]
$[]等价于$(()) 用于算数运算，里面可以有多个表达式，返回值取最后一个表达式的值
eg:
    
    (.airflow) bamboo@ubuntu:~$ a=$[a=1,b=2,c=3,c+4]
    (.airflow) bamboo@ubuntu:~$ echo $a
    7
    (.airflow) bamboo@ubuntu:~$ b=$((a=1,b=2,c=3,d=4))
    (.airflow) bamboo@ubuntu:~$ echo $b
    4
    (.airflow) bamboo@ubuntu:~$ a=$[a=1,b=2,c=3,d=4]
    (.airflow) bamboo@ubuntu:~$ echo $a
    4
    (.airflow) bamboo@ubuntu:~$ a=$((a=1,b))
    (.airflow) bamboo@ubuntu:~$ echo $a
    2
    (.airflow) bamboo@ubuntu:~$ 

$()和$(())从左到右运算，并将最后一个语句或者表达式的结果返回。即使是赋值语句或者是变量，也将其结果返回给等号左边。\
其真正的原理是运算得到一个变量（a+1,a=1,a)都可以视为一个临时承载的变量，代表某个值的含义