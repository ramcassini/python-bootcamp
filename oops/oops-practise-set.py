# 1. Create a Simple Class and Object
# 2. Constructor and Attributes
class animal:
    name = 'animal'

    def __init__(self,name):
        self.name = name

    def typeOfAnimal(self):
        print('general')

class dog(animal):
    name = 'dog'
    def __init__(self):
        #super().__init__(name)
        self.name = 'am a dog'
    def typeOfAnimal(self):
        super().typeOfAnimal()
        print('pet animal')
obj = animal("general")

obj2 = dog()
#print(obj.name)
obj2.typeOfAnimal()
