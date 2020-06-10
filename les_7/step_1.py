class MyCollection:
    def __int__(self, *args):
        self.box = list(args)

    def __add__(self, other):
        result = map(sum, zip(self, other)) # в метод список меджик методов
        return MyCollection(*result)

    def __bool__(self):
        return True if len(self.box) & 1 else False
    
    def __str__(self) -> str:
        return str(self.box)
    
    def __del__(self):
        return str(self.box)
    
    def __getitem__(self, item):
        return self.box(item)
    
    def __call__(self, x, y):
        return sum((self(0), x, y)) # двойные скобки т к он может передать только один объект
    
    
    


a = MyCollection(1, 2, 3, 4, 5)

b = MyCollection(1, 2, 3, 4)
print(bool(b))
