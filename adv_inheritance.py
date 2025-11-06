
# ## ------ Multi Level Inheritance ------
# class Animal: #grand eparent class
#     def __init__(self,name):
#         self.name= name

#     def speak(self):
#         print(f"{self.name} makes a sound.")


# # intermidiate class
# class Dog (Animal): # parent class
#     def __init__(self,name):
#         super().__init__(name)

        
#     def speak(self):
#         super().speak()
#         print(f"{self.name} Barks.")


# class breed(Dog): # child class
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed

#     def color(self):
#         super().speak()
#         if self.breed=='Golden Retriver':
#             print(f"{self.name} is {self.breed} and has golden colour.")
#         else:
#             print(f"{self.name} is {self.breed}.")


# dog=breed(name='Simba',breed='Golden Retriver')
# dog.color()


#-------------------------------------------------------------------------#




# ## ------ Hierachical Inheritance ------
# class Animal: # parent class
#     def __init__(self,name):
#         self.name= name

#     def speak(self):
#         print(f"{self.name} makes a sound.")


# # intermidiate class
# class Dog (Animal): # Chils 1 class
#     def __init__(self,name):
#         super().__init__(name)

        
#     def speak(self):
#         super().speak()
#         print(f"{self.name} Barks.")


# class Cat(Animal): # child 2 class
#     def __init__(self,name):
#         super().__init__(name)
#         self.behavior='Cute'

#     def behave(self):
#         super().speak()
#         print(f"{self.name} is {self.behavior} .")

        

# dog=Dog("Simba")
# dog.speak()
# cat=Cat("Mona")
# cat.behave()
# ##-------------------------------------------------------------------------#





# ## 1------ Multiple  Inheritance ( Diamod Problem) ------ #
# class Animal: # parent class
#     def __init__(self,name):
#         self.name= name

#     def speak(self):
#         print(f"{self.name} makes a sound.")


# # intermidiate class
# class Dog (Animal): # Chils 1 clas    
#     def speak(self):
#         super().speak()
#         print(f"{self.name} is Dog.")


# class Cat(Animal): # child 2 class
#     def speak(self):
#         super().speak()
#         print(f"{self.name} is cat.")

# class Pet(Cat,Dog):

#     def speak(self):
#         super().speak()
#         print(f"{self.name} is very friedly.")

# ## Derived class#####

# pet=Pet("Sonu")
# pet.speak()

# ''' Out put 


# Sonu makes a sound.
# Sonu is Dog.
# Sonu is cat.
# Sonu is very friedly 


# Pet → Cat → Dog → Animal → object
# Inside Cat.speak, the call to super().speak() asks: “what’s the next class after Cat in the Pet MRO?”
# Answer: Dog. So it goes to Dog.speak(). 

# '''
        

# ## 2------ Multiple  Inheritance ( Diamod Problem) ------ #
# class Animal: # parent class
#     def __init__(self,name):
#         self.name= name

#     def speak(self):
#         print(f"{self.name} makes a sound.")


# # intermidiate class
# class Dog (Animal): # Chils 1 clas    
#     def speak(self):
#         print(f"{self.name} is Dog.")
#         super().speak()
       


# class Cat(Animal): # child 2 class
#     def speak(self):
#         print(f"{self.name} is cat.")
#         super().speak()
        

# class Pet(Cat,Dog):

#     def speak(self):
#         print(f"{self.name} is very friedly.")
#         super().speak()
        

# ## Derived class#####

# pet=Pet("Sonu")
# pet.speak()


## 2------ Multiple  Inheritance ( Diamod Problem) ------ #
class Animal: # parent class
    def __init__(self,name):
        self.name= name

    def speak(self):
        print(f"{self.name} make sounds.")


# intermidiate class
class bird (Animal): # Chils 1 clas    
    def body_part(self):
        print(f"{self.name} has wings.")
        #super().speak()
       


class swim(Animal): # child 2 class
    def ability(self):
        print(f"{self.name} can swim.")
        #super().speak()
        

class Pet(bird,swim):

    def ability(self):
        print(f"{self.name} lays eggs.")
        super().ability()
        super().speak()
        

## Derived class#####

duck=Pet("duck")
duck.ability()
duck.body_part()



