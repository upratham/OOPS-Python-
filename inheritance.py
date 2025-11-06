# # Simple inheritance

# # Base calss

# class Animal:
#     def __init__(self,name):
#         self.name= name

#     def speak(self):
#         print(f"{self.name} makes a sound.")


# # derived class
# class Dog (Animal):
        
#     def speak(self):
#         print(f"{self.name} Barks.")


# # generic = Animal("generic animal")
# # generic.speak() # Output - generic makes sound

# dog=Dog('Simba')
# dog.speak()


## Super Keyword



# Base calss

class Animal:
    def __init__(self,name):
        self.name= name

    def speak(self):
        print(f"{self.name} makes a sound.")


# derived class
class Dog (Animal):
    def __init__(self,breed,name):
        super().__init__(name)
        self.breed= breed
        
    def speak(self):
        super().speak()
        print(f"{self.name} Barks. and it is {self.breed}")

dog=Dog("Golden Retriver",name='Simba')
dog.speak()
# out put 
# Simba makes a sound.
# Simba Barks. and it is Golden Retriver