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



import time



def retry(times=3, second=1): # 重试时间为一秒，重试次数为3次
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                i = 0
                result = func(*args, **kwargs)
                while not result and i < times:
                    time.sleep(second)
                    i += 1
                    result = func(*args, **kwargs)
            except:
                pass
            return result
        return wrapper
    return decorator


@retry(times=5)
def func():
    print('run failed')
    return False
func()
