# Python语言特性

##1. Python2和3的区别
### 1.1 Python2编码问题

参考：[Python 2.7.x 与 Python 3.x 的主要差异](http://chenqx.github.io/2014/11/10/Key-differences-between-Python-2-7-x-and-Python-3-x/)

##2. python函数传参以及变量传递

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

##3. python装饰器