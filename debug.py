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