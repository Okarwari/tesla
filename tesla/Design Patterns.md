# 使用Python来实现对应的设计模式


## 六大设计原则
### 1 开放封闭原则
含义： 对拓展开放、对修改封闭

为什么需要遵循开放封闭原则？
>修改某段代码（比如某个函数）可能会导致引用此段代码（函数）的功能受到影响，需要重新对代码进行全面的测试,有些改动需要对原来的代码做大规模的改动甚至重新构造系统.
而对拓展新的功能应该开放,是系统具备良好的拓展性，以适应未来可能出现的变化

解决方案：多使用接口或者抽象类实现，实现新功能时继承相应接口

注意： 对Python来说同样适用

### 2 里氏替换原则
含义： 基类可以直接被替换成子类，换句话说。基类可以出现的地方、子类一定能出现

为什么需要遵循里氏替换原则？
>一个子类一定数据对应的基类，就好比男人一定属于人。因此人可以出现的地方，
男人一定可以出现，因为男人具有人的所有属性和行为。所以，子类应该能替换基类所处的位置。
并在此基础上，能够为基类增加新的功能。
如果修改了基类的某个方法实现，则会导致其他继承基类的子类的该方法被改变。

解决办法：使用抽象类继承，而不是用具体类继承。若是继承具体类，也不应该重写某具体方法，只能增加新的方法。

注意： 对Python来说同样适用

### 3 依赖倒转原则
定义：高层模块不应该依赖低层模块，二者都应该依赖其抽象；
抽象不应该依赖细节；细节应该依赖抽象。

为什么需要遵循依赖倒转原则？
>高层模块Person直接依赖底层模块Book会限制高层模块Person的拓展性，假设某天高层模块需要依赖其他底层模块时(想读报纸)，
则需要修改对应的高层模块（修改阅读方法，去加一个读报纸）。这样显然不合理。

解决办法：
>报纸和书籍统一继承抽象类（读物）或者直接继承接口IReader，实现对应的获取内容方法
在Person中形参设为抽象类（读物）或者IReader。通过Java多态获取对应的底层模块或类的方法。

注意：Python由于不限定某个参数的类型，这样虽可以避免直接依赖某个底层模块。
但太过灵活性可能导致错误传参造成错误。因此，在Python编程中应同样继承抽象类读物。
栗子：
```python
from abc import abstractmethod, ABCMeta


class Reader(metaclass=ABCMeta):

    @abstractmethod
    def get_content(self):
        pass


class Newspaper(Reader):
    def get_content(self):
        return '报纸内容.....'


class Book(Reader):
    def get_content(self):
        return '书的内容'


class Person:
    def read(self, reader):
        if isinstance(reader, Reader):
            print(reader.get_content())
        else:
            print('未知读物')

Person().read(Book())
Person().read('sdfsdf')
```



### 4 单一职责原则
定义： 同一个类或者方法应该只有一项职责

为什么要遵守单一职责原则？
1. 同一个方法实现了两个功能，将无法对某一个功能进行重用。使代码过于冗余
2. 若一个类或者方法同事拥有职责A或者职责B,在某个功能被改变之后，可能对另一个功能造成影响
使另一个功能无法正常执行。

解决方案：对方法和类进行拆分，拆成更细粒度的功能，在实现时请确认是否是一个功能。

有些时候写着写着，单一职责原则就变的不单一了。是因为最开始的时候，
你认为的单一职责可能会有很多种情况，可以被拆成更细粒度的。

 
### 5 迪米特原则（待深入理解）
定义： 一个对象应该对其他对象保持最少的了解，一个类应该对自己需要耦合或调用的类知道得最少，
迪米特原则也叫最少知道原则，且一个对象只和自己的朋友通信。

迪米特法则还有一个更简单的定义：只与直接的朋友通信。
首先来解释一下什么是直接的朋友：每个对象都会与其他对象有耦合关系，只要两个对象之间有耦合关系，
我们就说这两个对象之间是朋友关系。耦合的方式很多，依赖、关联、组合、聚合等。其中，
我们称出现成员变量、方法参数、方法返回值中的类为直接的朋友，而出现在局部变量中的类则不是直接的朋友。
也就是说，陌生的类最好不要作为局部变量的形式出现在类的内部。

为什么要遵守迪米特原则？
>一般在使用框架的时候，框架的开发者会抽出一个类供外部调用，
而这个主要的类像是一个中介一样去调用框架里面的其他类，
恰恰框架里面其他类一般都是不可访问（调用）的，这个框架就遵守了迪米特原则，
其他开发人员只关心调用的方法，并不需要关心功能具体如何实现

解决方案：降低类与类之间的耦合。


### 5 接口隔离原则
定义: 在定义接口方法时应该合理化，尽量追求简单最小，避免接口臃肿

为什么要遵守接口隔离原则？
>在实际开发中，往往为了节省时间，可能会将多个功能的方法抽成一个接口，其实这设计理念不正确的，
这样会使接口处于臃肿的状态，这时就需要合理的拆分接口中的方法，另外抽取成一个独立的接口，
避免原有的接口臃肿导致代码理解困难


### 六大原则小结
* 代码应该对修改关闭，但对拓展开放（开闭原则）
* 子类不该修改父类已经实现的功能（里氏替换原则）
* 高级类不该依赖某个具体的实现，而应该依赖于抽象类（某一类事物），从而适应变化
* 每个类和方法只要实现同一个任务，若这个任务具有变化性，则应该进行拆分。（单一职责原则）
* 不要实现无用的方法（接口隔离）
* 不要依赖陌生人。（迪米特原则）
### 个人思考
1.不要对在现实生活中抽象事物的某些属性和行为进行实现，
除非你确定这个抽象在被继承后，子类所拥有的行为是所有的功能都一样。----关于单一职责引发的思考
>举个栗子，人都是呼吸空气，那么人这个抽象事物可以实现呼吸方法。
但是动物不全是呼吸空气，比如鱼和牛。那么动物就不该去实现具体的呼吸方法，
而是使用抽象方法，让子类去实现对应的具体细节。

网上反面教材：动物类的呼吸方法不该直接实现，同样动物也不该被实例，他是一个抽象概念。
```
class Animal{
    public void breathe(String animal){
        System.out.println(animal+"呼吸空气");
    }
}
public class Client{
    public static void main(String[] args){
        Animal animal = new Animal();
        animal.breathe("牛");
        animal.breathe("羊");
        animal.breathe("猪");
    }
} 
```
在设计中，多去思考这个类是否是抽象事物，他的行为属性是否会在子类的过程中被改变。


## 设计模式
### 1 单例模式

单例模式的定义就是每个类只有一个对象。整个对象在项目的整个全局中被使用，同时需要避免多线程时的并发访问问题。

#### Python的实现方式
##### 1. __new__方法
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
##### 2. 装饰器
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

##### 3. import方式
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


##### 4.使用元类
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