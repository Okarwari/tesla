import sys


#
# print(Singleton())
# #
# class Interpreter:
#     _instance = None
#     #
#     # def __init__(self, x):
#     #     super().__init__()
#     #     self.val = x
#     #     print(self.val)
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             ori
#             cls._instance = .__new__(cls, *args, **kwargs)
#         return cls._instance


# a = Interpreter(1)
# print(a.val)
# b = Interpreter(2)
# print(b.val)
# print(a == b)

#
# def get_parameter(*args, **kwargs):  # 工厂函数，用来接受@get_parameter('index.html/')的'index.html/'
#     print(args, kwargs)
#     def log_time(func):
#         def make_decorater():
#             print(args, kwargs)
#             print('现在开始装饰')
#             func()
#             print('现在结束装饰')
#
#         return make_decorater
#
#     return log_time
#
#
# @get_parameter('index.html/')
# def test():
#     print('我是被装饰的函数')
#     # return num+1
#
#
# test()  # test()=make_decorater()


# class Person:
#     _state = {}
#     def __init__(self):
#
#
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, x):
        self.x = x

a = Singleton(2)
b = Singleton(3)
print(id(a))
print(id(b))
print(a.x, b.x)

class My_Singleton(object):
    def foo(self):
        pass

print('*****')

my_singleton = My_Singleton()