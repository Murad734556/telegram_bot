


# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname

#     @property
#     def info(self):
#         return self.__name + " " + self.__surname


#     @info.setter
#     def info(self, new_name):
#         self.__name = new_name

#     @info.deleter
#     def info(self):
#         del self.__name

# person = Person("Faha", "IT")
# print(person.info)
# person.info = "Hello"
# print(person.info)
# print(person.__dict__)
# del person.info
# print(person.__dict__)


# Напишите класс GTA, которая имитирует поведение игры GTA.
# Там есть много методов, но вы должны сделать основные методы
# как ходить, атаковать, получать урон и делать деньги. Так
# конструктор принимает персонажи из игры GTA V (Майкл,
# Тревор, Франклин), то есть если вы ввели другое имя, 
# то вам он должен выводить "Нету такого персонажа". 
# И также создайте переменные экземпляра (health 100, 
# money 100, satiety, 100, walk 0)Затем создайте
# магический метод для того чтоб он возвращает все значения.
#Создайте метод walk для ходьбы и чтоб когда вызывали метод,
#в walk добавлялось 1 единица значения. Потом создайте метод
#attack, которая принимает единицу урона. Если урон между 
#1 и 20, то он должен выводить "Ваш персонаж атаковал и 
#сделал урон{ваш урон}".  Иначе выводит "Вы не нанесли урон".
#Затем создайте метод для получения урона(случайное значение). 
#И также если ваше здоровье закончилась то он должен списать 
#с вашего баланса 10 долларов и также пополнить вашe здоровье
#на 100 единиц. Сделайте последний метод для заработка денег. 
# То есть когда мы вызываем метод то он должен добавлять 100 долларов в наш баланс.
# Теперь создайте экземпляр класса и вызовите все методы которые у нас присутствуют. 

import random

class GTA:
    def __init__(self, character):
        if character != "Майкл" and character != "Тревор" and character != "Франклин":
            print("Нету такого персонажа")
        else:
            self.character = character
            self.health = 100
            self.money = 100
            self.satiety = 100
            self.walk = 0


    def go_walk(self):
        self.walk += 1
        print(f"Вы прошагали {self.walk} шагов")

    def attack(self, uron):
        self.uron = uron
        if uron  >= 1 and uron <= 20:
            print(f"Ваш персонаж атаковал и сделал урон{self.uron}")
        else:
            print(f"Вы не нанесли урон")

    def get_uron(self):
        self.uron =  random.randit()
       
    def get_money(self):
        self.money += 100

    def __str__(self):
        return self.character, self.health, self.money, self.satiety, self.walk
gta = GTA("Майкл")
# gta.go_walk()
# print(gta.__str__())
# gta.attack()

        




