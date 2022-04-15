# class Human:
#     def walk(self):
#         return "Я могу ходить"

#     def talk(self):
#         return "Я могу говорить"

#     def breathe(self):
#         return "Я могу дышать"

# class Doctor(Human):
#     def cure(self):
#         return "Я могу лечить"

# class Programmer(Doctor):
#     def programming(self):
#         return "Я могу програмировать"
    
# programmist = Programmer()
# print(programmist.walk())
# print(programmist.talk())
# print(programmist.breathe())
# print(programmist.programming())
# print(programmist.cure())


# from io import BufferedRandom


# class Father:
#     def build(self):
#         return "I can to build"
#     def cure(self):
#         return "I can to cure"

# class Mother:
#     def cook(self):
#         return "I can to cook"

# class Son(Father, Mother):
#     def programming(self):
#         return "I can to programming"

# son = Son()
# print(son.cook())



# class A:
#     def hello(self):
#         return "Class A"

# class B:
#     def hello(self):
#         return "Class B"

# class C(A,B):
#     def hello(self):
#        return "Class C"
# d = C

# print(d.hello)

# class Car:
#     def __init__(self,brand , model, year, color, price):
#         self.brand = brand
#         self.model = model
#         self.year = year 
#         self.color = color
#         self.price = price
    
#     def info(self):
#         return f"{self.brand} {self.model} {self.year} {self.color} {self.price}"

# car = Car("BMW", "X5", 2020, "Black", 100000)
# print(car.info())

# class FutureCar(Car):
#     def __init__(self, brand, model, year, color, price, is_flying):
#         super().__init__(brand, model, year, color, price)
#         self.is_flying = is_flying 

#     def info(self):
#         return super().info()+ str(self.is_flying)

# future = FutureCar("Tesla", "Model X", 2021, "white", 100000, True)
# print(future.info)


# class Person:
#     def talk(self):
#         return "I can to talk"
    
#     def walk(self):
#         return "I can to walk"

# class Programmer(Person):

#     def programming(self):
#         return "I can to programming"

# class LittleProgrammer(Programmer):
#     def coding(self):
#         return "I can to write code"

# class Builder(Person):
#     def build(self):
#         return "I can to build"

# d = Programmer()
# print(d.talk())
# print(d.walk())

# b = LittleProgrammer()
# print(b.coding())

# c = Builder()
# print(c.talk())



# class Steamship:
#     def __init__(self, make, model, year, max_speed, odometer):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = odometer
#         self.is_swimming = False
#         self.stop_swimming = True

#     def info_about_swimming(self):
#         self.is_swimming = False
#         self.odometer = 0
#         return f"{self.make} {self.model} {self.year} {self.odometer} {self.stop_swimming} {self.is_swimming}"


#     def get_swimming(self):
#         self.is_swimming = True
#         self.stop_swimming =False 
#         self.odometer = 20
#         self.max_speed = 200
#         return f"{self.make} {self.model} {self.year}  {self.max_seed} {self.odometer} {self.is_swimming} {self.stop_swimming}"

#     def stop_swimming(self):
#         self.is_swimming = False
#         self.stop_swimming = True
#         self.max_speed = 0 
#         return f"{self.max_speed} {self.odometer} {self.is_swimming} {self.stop_swimming}" 

# ship = Steamship("Titanic", "AN150", 2021, 150, 0)  
# # ship.max_speed(500)
# print(ship.info_about_swimming())



# Полиморфизм..............................................................


# from codecs import namereplace_errors


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#     def info(self):
#         return f" Dog {self.name} age {self.age}"

#     def make_sound(self):
#         return f"Gaww"

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#     def info(self):
#         return f" Cat {self.name} age {self.age}"

#     def make_sound(self):
#         return f"Meow"

# class Cow:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#     def info(self):
#         return f" Cow {self.name} age {self.age}"

#     def make_sound(self):
#         return f"Muuu"

# dog = Dog("Django", 5)

# cat = Cat("Persik", 7)

# cow = Cow("Burka", 12)

# for animal in (dog, cat, cow):
#     try:
#         print(animal.info())
#         print(animal.make_sound())
#     except AttributeError:
#         print("Неправильно") 


# class Add:
#     def calc(self, a, b):
#         return a+b

# class Sub:
#     def calc(self, a, b):
#         return a - b 


# class Mult:
#     def calc(self, a, b):
#         return a * b 


# class Div:
#     def calc(self, a, b):
#         return a / b 



# class Student:
    
#     def __init__(self, name = "Ivan", groupNumber = "10A", age = 18):
#         self.name = name
#         self.groupNumber  = groupNumber
#         self.age = age

#     def getName(self):
#         return self.name

#     def getAge(self):
#         return self.age

#     def setGroupNumber(self,groupNumber ):
#         self.groupNumber = groupNumber 
#         return f"{self.name} {self.groupNumber} {self.age}"

#     def SetNameAge(self, name,age):
#         self.name = name
#         self.age = age
#         return f"{self.name} {self.groupNumber} {self.age}"

#     def setGroupNumber(self, groupNumber):
#         self.groupNumber = groupNumber
#         return f"{self.name} {self.groupNumber} {self.age}"

# student = Student()
# print(student.setGroupNumber("8A"))

# import string


# class Alphabet:
#     def __init__(self, lang, letter):
#         self.lang = lang
#         self.letter = letter
#     def print(self):
#         return self.letter

#     def letters_num(self):
#         return len(self.letter)

# class EngAlphabet(Alphabet):

#     __letters_num = 26


#     def __init__(self):
#         super().__init__('En', string.string.ascii_uppercase)

#     def is_en_letter(self,letters):
#         if letters.upper() in self.letters:
#             return f"in Alph"
#         else:
#             return f"not"

#     def letters_num(self):
#         return EngAlphabet.__letters_num

#     @staticmethod
#     def example():
#         return "Hello"


# class Student:
#     def __init__(self, name , surname):
#         self.name= name
#         self.surname = surname

#     def info(self):
#         return f"{self.name} {self.surname}"

#     def __str__(self):
#         return f"Str {self.name} {self.surname}"

#     def __repr__(self):
#         return f"Repr {self.name} {self.surname}"

#     def __call__(self):
#         return "Call"





# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
        
#     def __str__(self):
#         return f"{self.brand} {self.model} {self.price}"
    
#     def __eq__(self,car):
#         return self.price == car.price

#     def __lt__(self,car):
#         return self.price < car.price

#     def __le__(self,car):
#         return self.price <= car.price   
    
#     def __ne__(self,car):
#         return self.price != car.price

#     def __gt__(self,car):
#         return self.price > car.price

#     def __ge__(self,car):
#         return self.price => car.price
          
# bmw = Car("BMW", "M5", 800000)
# print(bmw)
# lexus = Car("Lexus", "LX570", 800000)
# print(lexus)
# print(bmw == lexus)
# print(bmw <lexus)
# print(bmw <= lexus)
# print(bmw != lexus)


# __lt__ -- x<y
# __le__ -- x<=y
# __ne__ -- x!=y
# __gt__ -- x>y
# __ge__ -- x>=y

# Абстрактные классы


# from abc import ABC, abstractmethod


# class Math(ABC):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b 

#     @abstractmethod
#     def add(self):
#         pass

#     @abstractmethod
#     def sub(self):
#         pass

#     @abstractmethod
#     def div(self):
#         pass

#     @abstractmethod
#     def mult(self):
#         pass

# class AbcMath(Math):
#     def __init__(self, a, b):
#         super().__init__(a,b)

#     def add(self):
#         print(self.a + self.b)

#     def sub(self):
#         print(self.a - self.b)

#     def div(self):
#         print(self.a / self.b)

#     def mult(self):
#         print(self.a * self.b)

# math = AbcMath(10, 10)
# math.add()
# math.sub()
# math.div()
# math.mult()

# import random

# print(random.randit(1,10))
# print(random.randrange(1,100,2))

# names = ["Mark", "Edzen", "Faha", "Diana", "Zalkar"]
# print(random.choice(names))


# random_num = random.randint(1,10)
# n = 0 
# while True:
#     find_num = int(input("угадайте число:"))
#     if find_num >= 1 and  find_num <= 10:
#         n += 1
#         if n == 5:
#             print("У вас закончились попытки ")
#             break

#         elif find_num == random_num:
#             print("Вы выиграли")
#             break
#         else:
#             print(f"Неверно {5 - n} попыток")
#     else:
#         print("Введите число от 1 - 10")



# class SlotMachine:
#     def __init__(self, name):
#         self.name = name
#         self.__user_balance = 100
#         self.__game_balance = 0 

#     def info(self):
#         print(f"Name: {self.name} Balance{self.__user_balance} game balance: {self.__game_balance}")

#     def top_up_balance(self):
#         money = int(input("Введите набранный балл:"))
#         if money <= 100:
#             self.__balance_up(money)
        
#         else:
#             print("Ошибка")

#     def __balance_up(self, money):
#         self.__user_balance -= money
#         self.__game_balance += money
        



#     def game(self):
#         random_num = random.randint(1,10)
#         n = 0 
#         while True:
#             find_num = int(input("угадайте число:"))
#             if find_num >= 1 and  find_num <= 10:
#                 n += 1
#             if n == 5:
#                 print(f"Вы проиграли:{self.__user_balance - 10}, {self.__user_balance}, {self.__game_balance}")
#                 self.__game_balance -= 10

#             elif find_num == random_num:
#                 print(f"Вы выиграли! {self.__game_balance + 10}") 
#                 self.__user_balance += 10
#             else:
#                 print(f"Неверно {5 - n} попыток")

#     def consulation_money(self):
#         how_many = int(input("How: "))
#         if self.__game_balance >= 50:
#             self.__game_balance -= how_many
#             self.__user_balance += how_many
#         else:
#             print("Мы не можем вывести столько")

#     def main(self):
#         while True:
#             a = input("Укажите команду: ")
#             if a == "1":
#                 self.info()
#             elif a == "2":
#                 self.top_up_balance()

#             elif a == "3":
#                 self.game()
#             elif a == "4":
#                 self.consulation_money()
#             else:
#                 print("None")

# num = SlotMachine("Murad")
# num.main()





# Миксины



# class Subscriber:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     def __str__(self):
#         return f"{self.firstname},{self.lastname}"

# num  = Subscriber("Murad", "Yahoo")
# print(num.__str__())


class Car:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, km):
        self.odometer += km

    def __subtract_fuel(self, fuel):
        self.fuel -= fuel



    def drive(self, km ):
        fuel = km /10
        if self.fuel >= fuel:
            self.__add_distance(km)
            self.__subtract_fuel(fuel)
            print("Let's drive!")
        else:
            print("Need more fuel, please, fill more!")

car = Car("Rolls-Royce", "Cullinan", 2020)
car.drive(500000)


class Bank:
    def __init__(self, money ):
        self.money = money
    
    def add(self):
        n = 10
        num = int(input("How much: "))
        num -= n
        self.money += num
        print(f"{self.money}")

    def sub(self):
        m = 10
        num = int(input("How much: "))
        num -= m 
        self.money -= num
        print(f"{self.money}")





    def main(self):
        while True:
            a = input("Укажите команду: ")
            if a == "1":
                self.add()
            elif a == "2":
                self.sub()
            else:
                print("Error")

mun = Bank(1000)
mun.main()























