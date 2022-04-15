# 1

class Subscriber:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def __str__(self):
        return self.firstname , self.lastname

    
s = Subscriber('Kuma', 'Aitishnikov')
print(s.__str__())


# 2

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0
        self.fuel = 70
    
    def __add_distance(self, km):
        self.odometr += km
    
    def __subtract_fuel (self, fuel):
        self.fuel -= fuel

    def drive(self, km):
        fuel = km / 10
        if self.fuel >= fuel:
            self.__add_distance(km)
            self.__subtract_fuel(fuel)
            print("Let's drive")
        else:
            print("Need more fuel, please fill more")

lexus = Car('Lexus', 'lx570', 2020)
lexus.drive(900)


# 3

class Bank:
    def __init__(self):
        self.__balance = 0

    def add_balance(self, amount):
        self.__balance += amount
        return f"Vash balance popolnen na {amount} USD"
    
    def __nalog(self, nalog):
        self.__balance -= nalog
    
    def sub_balance(self, amount):
        nalog = amount / 10
        if self.__balance >= amount:
            self.__balance -= amount
            self.__nalog(nalog)
            return f"S vashego balansa bilo snyato {amount}. Nalog - {nalog}"
    
        else:
            return f"Na vashem balanse-{self.__balance}, Vi ne mozhete snyat-{amount}"

    def __str__(self):
        return f"Na vashem schetu: {self.__balance} USD"

kuma = Bank()
print(kuma.add_balance(1000))
print(kuma)
print(kuma.sub_balance(200))
print(kuma)

print(kuma.sub_balance(1100))
print(kuma)