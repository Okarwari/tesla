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