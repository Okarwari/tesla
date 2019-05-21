# 使用Python来实现对应的设计模式

## 1. 单例模式

单例模式的定义就是每个类只有一个对象。整个对象在项目的整个全局中被使用，同时需要避免多线程时的并发访问问题。

###Python的实现方式
#### 1. __new__方法
```python
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance

a = Singleton()
b = Singleton()
print(id(a))
print(id(b))
```
#### 2. 装饰器
```python
def singleton(cls):
    instance = {}

    def get_instance(*args, **kwargs):
        print(args, kwargs)
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
            print(instance)
        return instance[cls]

    return get_instance


@singleton
class Person(object):
    def __init__(self, x):
        self.x = x

a = Person(2)
b = Person(3)
print(a is b)
print(a.x)
```

#### 3. import方式
```python
# mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()

# to use
from mysingleton import my_singleton

my_singleton.foo()
```


#### 4.使用元类
```python
class Singleton(type):
    def __new__(cls, name, bases, attrs):
        cls.__instance = None
        print('signer')
        return super(Singleton, cls).__new__(cls, name, bases, attrs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance



print('*****')

class Person(metaclass=Singleton):
    pass

a = Person()
b = Person()
print(id(a))
print(id(b))
```