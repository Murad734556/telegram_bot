# import random 
# class GTA:
#     def __init__(self, character):
#         if character == "Michael" or character == "Trevor" or character == "Franklin":
#             self.character = character
#             self.health = 100
#             self.money = 100
#             self.satiety = 100
#             self.walk = 0
        
#     def go_walk(self):
#         self.walk += 1
#         return f"Вы прошагали {self.walk} шагов"
    
#     def attack(self, xp):
#         if xp >= 1 and xp <= 20:
#             return f"Ваш персонаж атаковал и сделал урон: {xp}"
#         else:
#             return f"Вы не нанесли урон"

#     def get_damage(self):
#         damage = random.randint(1, 20)
#         self.health -= damage
#         if self.health < 0:
#             self.money -= 10
#             self.health = 100
#             return f"You dead"
#         return f"You've got crushed {damage}"
    
#     def make_money(self):
#         self.money += 100
#         return f"You've earned 100 USD"
    
#     def __str__(self):
#         try:
#             return f"Name: {self.character}, Health: {self.health}%, Cash: {self.money}USD, {self.walk} шагов"
#         except AttributeError: 
#             print("No such character")

# gta = GTA('Michael')
# print(gta)
# print(gta.attack(15))
# print(gta.get_damage())
# print(gta.get_damage())
# print(gta)
# print("=================")



# print(gta.go_walk())
# print(gta.go_walk())
# print(gta)

# print(gta.make_money())
# print(gta.make_money())

# print(gta)
# print(gta.get_damage())
# print(gta.get_damage())
# print(gta)


# Создайте журнал с оценками для класса из пяти человек. (Имена можете взять выдуманные).  В этом журнале должны храниться оценки каждого ученика. Считайте, что у каждого ученика должно быть по 5 оценок (в диапазоне от 1 до 100 баллов). Высчитайте среднее арифметическое значение оценок для каждого ученика. Сохраните и выведите в переменную имя и средний балл лучшего ученика.

journal = {"Gabai" : [4,50,22,6,7],
           "Murad" : [10,2,23,44,5],
           "Chopin" :[12,5,3,9,41],
           "Alina" : [2,12,4,11,17],
           "Erbol" : [2,34,32,45,12]}
for key, val in journal.items():
        print(sum()) 




# n = [1,34,23,32,1]
# print(sum(n)/ len(n))







# Напишите класс Сonstructor, которое имитирует строительство жилого дома. В конструкторе мы передаем сколько этажей мы хотим построить. Затем делаем метод build, который строит наш дом пока мы не дойдем до этажа которую мы хотим построить. И также создайте магический метод __str__, для выведение данных нашего класса

# class Constructor:
#     def __init__(self):
#         self.floor = 18

#     def build(self):
#         for i in range(self.floor):
#             print(f"Строиться: {i} этаж")

#     def __str__(self):
#         return f"Построили {self.floor} этажей "    

# con = Constructor()
# print(con.build())
# print(con.__str__())
