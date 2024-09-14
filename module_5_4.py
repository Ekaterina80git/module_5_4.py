class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self,first,second,third):
        print(first)
        print(second)
        print(third)


ex = Example('data',second= 25,third=3.14)

class House:
    houses_history = []  # атрибут класса

    def __new__(cls,*args,**kwargs):
         cls.houses_history.append(args[0]) # добавляем новые обьекты
         #print(*cls.houses_history)
         return super().__new__(cls)

    def __init__(self,name,number_of_floors):
          self.name = name
          self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название:{self.name},кол-во этажей:{self.number_of_floors}'

    def __del__(self):
        print(f'{self.name},снесён,но он останеться в истории')





h1 = House("ЖК Эльбрус",10)
print(House.houses_history)

h2 = House("ЖК Акация",20)
print(House.houses_history)

h3 = House("ЖК Матрёшки",20)
print(House.houses_history)


# Удаление обьектов
del h2
del h3

print(House.houses_history)
del h1