# Python语言特性
**Table of Contents**
    
   * [Python效率总结]()
   * [Python基础](#Python基础)
      * [1 Python2和3的区别](#1-Python2和3的区别)  
      * [2 Python函数传参以及变量传递](#2-Python函数传参以及变量传递)  
      * [3 闭包](#3-闭包)  
      * [4 Late Binding](#4-Late Binding)  
      * [5 Python装饰器](#5-python装饰器)  
      * [6 Python单例模式](#6-Python单例模式)  
      * [7 Python面向对象](#7-Python面向对象)
         * [1 Python C3算法](#1-Python C3算法)
      * [8 生成器、迭代器、可迭代对象](#8-生成器、迭代器、可迭代对象)

## Python效率总结
1. extend比append要快

```python
import time
gen = [0 for i in range(90000000)]
pen = [0 for v in range(90000000)]
t1 = time.time()
num = []
for i in gen:
    num.append(i)
t2 = time.time()
print(t2-t1)
new_num = []
new_num.extend(pen)
t3 = time.time()

print(t3-t2)
```

## Python基础
## 1 Python2和3的区别
### 1.1 Python2编码问题

参考：[Python 2.7.x 与 Python 3.x 的主要差异](http://chenqx.github.io/2014/11/10/Key-differences-between-Python-2-7-x-and-Python-3-x/)

## 2 Python函数传参以及变量传递

1. python的参数传递可以分为顺序传参和关键字传参，通过*args, **kwargs可以将接受任意多的参数

举个栗子

```python
def func(*args, **kwargs):
    print(args, kwargs)
func(1,2,3,a=2,c=3)
```
output: 
```python

```

同样，可以再固定参数的函数里使用列表传参和字典传参

举个栗子

```python

def func(a, b, c, d, e):
    print(a, b, c, d, e)
func(1, *[2,3], **{"d":1, 'e': 2})
```

注意： 顺序传参一定要再字典传参之前

2. python的变量并不是存储的变量值，而是存储的一个对应值的地址。


注意： 尽力不要使用可以对象当默认值，python的默认值在函数首次调用时初始化，此后不再重新初始化
举个栗子：
```python
def f(a, b=[]):
    print(b)
    a.append(2)
    b.append(2)
    print('inter', a)
    print('inter', b)

a = [1]
b = [1]
f(a)
print(a)
f(a)
print(a)

f(a, b)

f(a)
print(a)

print(a)
```

## 3 闭包

举个栗子
```python
def out(x):
    def inter(y):
        return x * y
    return inter


func = out(2)
print(func(2))
```

由以上栗子引出闭包的定义。当一个内嵌函数引用其外部作作用域的变量,我们就会得到一个闭包. 总结一下,创建一个闭包必须满足以下几点:

1. 必须有一个内嵌函数
2. 内嵌函数必须引用外部函数中的变量
3. 外部函数的返回值必须是内嵌函数

经过测试后，我认为闭包的具有以下性质
>1. 未被内部函数应用的变量将会被gc回收
```python
import sys

import sys

print(sys.getrefcount('123123123'))
print(sys.getrefcount('sdfsdfsdfdsfdsfdsfdsf'))

def out(x):
    f = '123123123'
    s = 'sdfsdfsdfdsfdsfdsfdsf'
    x = f
    print(sys.getrefcount('123123123'))
    print(sys.getrefcount('sdfsdfsdfdsfdsfdsfdsf'))
    def inter(y):
        return x * y
    return inter




func = out(2)
func(2)
# print(func(2))
print(sys.getrefcount('123123123'))
print(sys.getrefcount('sdfsdfsdfdsfdsfdsfdsf'))
``` 

>2. 如果外部引用变量为可变对象（set、list)则可以被改变。
```python
def func(l):
    def inter(x):
        l.append(x)
        print(l)
    return inter

l = []
inter = func(l)
inter(1)
inter(2)
print(l)
```


闭包的作用
>作用1. 当闭包执行完后，仍然能够保持住当前的运行环境。原因是外部引用变量没有回收，使用可变对象时，可以使用被引用变量保存当时的状态。
```python
origin = [0, 0]  # 坐标系统原点  
legal_x = [0, 50]  # x轴方向的合法坐标  
legal_y = [0, 50]  # y轴方向的合法坐标  
def create(pos=origin):  
    def player(direction,step):  
        # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等  
        # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。  
        new_x = pos[0] + direction[0]*step  
        new_y = pos[1] + direction[1]*step  
        pos[0] = new_x  
        pos[1] = new_y  
        #注意！此处不能写成 pos = [new_x, new_y]，原因在上文有说过  
        return pos  
    return player  
 
player = create()  # 创建棋子player，起点为原点  
print player([1,0],10)  # 向x轴正方向移动10步  
print player([0,1],20)  # 向y轴正方向移动20步  
print player([-1,0],10)  # 向x轴负方向移动10步 

"""
output:
[10, 0]  
[10, 20]  
[0, 20]  
"""
```
>作用2. 可以通过传入不用的外部，生成一批功能类似，但作用不同的函数
```python
def make_filter(keep):  
    def the_filter(file_name):  
        file = open(file_name)  
        lines = file.readlines()  
        file.close()  
        filter_doc = [i for i in lines if keep in i]  
        return filter_doc  
    return the_filter  
    
filter = make_filter("pass")  
filter_result = filter("result.txt")
```
## 4 Late Binding
看看这个两个例子
```python
flist = []
for j in range(5):
    def foo(x): print(x+j)
    print(foo)
    flist.append(foo)
for f in flist:
    f(2)
```

```python
def out(x):
    def inter(y):
        print('x_id', id(x))
        return x * y
    return inter

fancs = []
fo****r i in range(5):
    f = out(i)
    print(id(f))
    fancs.append(f)

for f in fancs:
    print(f(2))
```
由于python的变量只在调用时才会去查找对应的变量值。因此第一个例子在调用的时候，i的值已经变成了4，因此将输入6 6 6 6 6
但是第二个例子，由于i将他的引用值传递给了x。 此时每个函数的x的值分别为0， 1， 2， 3， 4.
此时各个函数查找x时，则会输出0, 2 ,4, 6, 8。
这是正确答案，所以在内部函数引用外部变量时，请尽量不要使用全局变量

## 5 python装饰器
装饰器其实是一个典型的闭包，主要功能是原函数添加新的功能
举个例子

```
def add_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time-start_time)
    return wrapper

@add_time
def func():
    print('func')

func()
```

如果要为装饰器添加参数
```python
def log(log_field):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func()
            print(log_field)
        return wrapper
    return decorator  # log() 调用后返回decorator


@log(log_field='name')  # 等价于  func = log(log_field='name')(func) => decorator(func)
def func():
    print('func')
func()
```

类装饰器
```python
class Count(object):
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(self.count)
        self.func()

@Count
def func():
    print('hello world')


func()
func()

```

其实所谓装饰器都是通过函数的特性衍生出来的，因为函数可以被当成变量传递，才会有装饰器、闭包等产生。
所谓装饰器语法都绕不过`@decorator -> func = decorator(func)`这个公式，
类装饰器也是一样，@Count -> func = Count(func) 
将实例化一个Count对象，func被当成对象的属性，调用func等于调用__call__方法


## 6 Python单例模式

 [设计模式之单例模式](../tesla/Design%20Patterns.md#1.单例模式)

## 7 Python面向对象
### 1 Python C3算法
C3算法用于Python3的类继承

#### 为什么采用C3算法
C3算法最早被提出是用于Lisp的，应用在Python中是为了解决原来基于深度优先搜索算法不满足本地优先级，和单调性的问题。

#### C3算法

公式：`mro(B) = [B] + merge(mro(A1), mro(A2), mro(A3) ..., [A1,A2,A3])`

遍历执行merge操作的序列，如果一个序列的第一个元素，在其他序列中也是第一个元素，或不在其他序列出现，
则从所有执行merge操作序列中删除这个元素，合并到当前的mro中。

merge操作后的序列，继续执行merge操作，直到merge操作的序列为空。如果merge操作的序列无法为空，
则说明不合法。

[参考:Python的多重继承问题-MRO和C3算法](https://www.jianshu.com/p/a08c61abe895)

### 2 类变量和实例变量

在类里面的所有属性都可以通过对象访问，换句话说，类变量可以被对象获取。即对象也可以通过getattr获取类变量的值

```python
class Person:
    country = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("hello world")


p = Person('stack', 12)
print(Person.__dict__)
print(p.__dict__)
print(hasattr(Person, 'say'))
print(hasattr(p, 'country'))

```

## 8 生成器、迭代器、可迭代对象
#### 生成器

生成器指向的并不是一系列数据，而是生成一系列数据的算法

#### 可迭代对象
凡是实现了__iter__方法的对象都是可迭代对象


#### 迭代器

凡是实现了__next__和__iter__方法的都是迭代器,可迭代对象使用iter()方法可以生成迭代器
生成器既是迭代器又是可迭代对象

```python
from collections import Iterator, Iterable

class LinkIter():
    def __init__(self, lst, index=0):
        self.lst = lst
        self.index = index

    def __next__(self):
        try:
            value = self.lst[self.index]
            self.index += 1
        except:
            raise StopIteration
        return value


class Link():
    def __init__(self, lst, index=0):
        self.lst = lst
        self.index = index

    def __iter__(self):
        return LinkIter(self.lst, self.index)

for i in Link([1,2,3,4,5]):
    print(i)

it = iter(Link([1,2,3,4,5]))

print(it, type(it))

print(hasattr(it, '__iter__'))

#print(iter(iter(Link([1,2,3,4,5]))))

print(isinstance(it, Iterator))
print(isinstance(Link([1,2,3,4,5]), Iterable))

```
这段代码是我想判断是否迭代器一定就是可迭代对象。其实，官方约定迭代器协议是实现__iter__和__next__方法
所以这段代码其实是误导，只是我觉得规则是死的人是活的。
不过这段代码若是这样执行是会出错的
`print(iter(iter(Link([1,2,3,4,5]))))`

## Python的lru_cache 最近最久使用缓存
Python的Lru_chahe用了一个循环引用的方式，做了一个循环链表，链表的每个节点指向的是一个列表，有一个引用root。
存储着每个节点的前驱和后继、每个节点的KEY、value.并生成一个缓存字典，key是KEY。链表有最大值。
程序的逻辑：
- 当待缓存值小于最大值时，将生成的新的节点插入在root的后面。代表这是最近出现的，将最后被销毁，然后返回结果。
- 当缓存中有这次KEY。将找到列表的前驱和后继。删除这个节点，将其插入到root的后面，返回结果。
- 当缓存未没有这次KEY, 将root赋值给oldroot，并将KEY和Result赋值给old_root，将root.next作为新的root,
这样old_root代表root的前驱，时最新出现的节点。并从cache中删除root.next总的KEY，代表这次KEY已经很久没有使用了。
![](../assets/images/Untitled%20Diagram.png)


# Python的Del
python的del关键字并不是删除某个数据、而是删除引用数据的变量，当数据（对象）的引用置为0时，
变量就会被GC回收
```python
l = [1, 2, 3]

a = {1: l}

del a[1]

print(l)

ll = l

del l

print(ll)

print(a)

print('-----')

l = [1,2,3]
del[l[1]]

print(l)

```


## Python的引用和C的指针

对于C来说，一个指针p存储了一个地址，这个地址对应内存的一块区域，指针能够改变这块地址的值
即能够直接操控内存的某块区域的值的变化。
而Python的赋值是将在内存某块地址的值（假设为1），用一个变量a去绑定他，对于a变量的更改（a=2)，
即是将a变量从1这里解绑，重新绑定2.
我对Python的引用推测如下（可能有误，以后会从源码找答案）
>a变量存储某个地址，这个地址是内存的某块区域，这块区域存储的值在a变量赋值(a='1')时开辟'1'。
当a变量重新赋值(a='2')时，会重新开辟一个对象'2'.而变量a的值由'1'的地址，转变成'2'的地址。

对上面的推测，我一个有一个疑问，所以不敢确定推测的合理性
按照我的推测，a存储的是1的地址, 那么print(id(a))的值时，打印的是1的地址，为什么不打印a的地址。
a的地址又是什么，这让我对a是否拥有自己的空间有所怀疑，常理来说a这个变量肯定是需要存储的，
可能的推测之一是a和代码一块存储在指令区把。


所以他们的区别，一个是改变自己（Python变量）的值（换一个引用对象），
一个是改变指向的地址（C指针）的值（将地址的值改变）

希望这段代码能够稍微证实一下我的推断，a确实在内存一个地方存着，存着一个跟1有关的东西，这个东西叫引用。等我啃源码！！！
```python
l = [1,2,3]

print(id(1))
print(id(l[0]))
print(id(l))
```

我曾一直将Python的变量当成一个void型指针，其实他和指针的特性还是有些区别。




## Python性能调优
[Python性能优化的几种方式](https://blog.csdn.net/u010159842/article/details/54573102)

