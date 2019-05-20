import sys


def singleton(func):
    pass


#
# class Singleton(type):
#     pass

#
# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance
#
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


