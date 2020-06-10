import requests
import json

class MyCls:
    a = 22
    b = 33

    def __init__(self, data: str, a, b):
        self.data = data
        self.a = a
        self.b = b


    @staticmethod
    def some(a, b):
        return a + b

    @classmethod
    def some_cls(cls):
        return cls.a + cls.b




if __name__ == '__main__':
    a = MyCls('some name', 2, 5)
    print(MyCls.__dict__)
    print(MyCls.__module__)
    print(MyCls.__name__)

    print(a.a + a.b)
    print(MyCls.some_cls())

    # print(a.some(2, 3))
    # print(MyCls.some(2, 6))

# https://checkio.org/
# чистый python