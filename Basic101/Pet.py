#!/usr/bin/python3.6

##Pet class which restricts the species to allowed list

class Pet:

    allowed_species = ['cat' , 'dog' , 'bird' , 'rat']
    petsintown = 0
    def __init__(self, petname , species):

        if species in Pet.allowed_species:
            self.species = species
        else:
            raise ValueError("Only these species are allowed: {0}".format(Pet.allowed_species))
        self.name = petname
        Pet.petsintown += 1
    
    @classmethod
    def set_species(cls, add_species):
        cls.allowed_species.append(add_species)      

    def __repr__(self):
        return "Hi, I am {0} and i am a {1}".format(self.name, self.species)

tommy = Pet('tommy' , 'dog')
print(tommy)

#tiger = Pet('Ibra' , 'Tiger')
#print(tiger.details())