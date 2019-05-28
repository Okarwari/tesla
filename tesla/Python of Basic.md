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
