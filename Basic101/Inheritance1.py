#!/usr/bin/python3.6

class Animal:
    
    totalpet = 0

    def __init__(self, name, country):
        self.name = name
        self.country = country
        Animal.totalpet += 1

    @classmethod
    def pets(cls):
        return cls.totalpet



class Dog(Animal):
    
    totaldog = 0
    def __init__(self,name, country, species, age):
        super().__init__(name, country)
        self.species = species
        self._age = age
        Dog.totaldog += 1

    @classmethod
    def pets(cls):
        return cls.totaldog

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self , myage):
        self._age = myage

    @property
    def nametag(self):
        return "{0}23{1}".format(self.name[-2:] , self.country[:-2])


    def details(self):
        return "Name: {0} and Age: {1}".format(self.name , self.age)

d = Dog('Tommy' , 'India' , 'Street' , 2)
cu = Dog('Tommy' , 'India' , 'Street' , 2)
du = Animal('Tommy' , 'India')
print(d.details())
print(d.nametag)
print(Animal.pets())
print(Dog.pets())