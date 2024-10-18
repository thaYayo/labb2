## Input ###

# user_input = input("Skriv något här")
# print(f"Du skrev: {user_input}")

# user_input = input("Ange ett number: ")
# if user_input.isdigit():
#     user_number = int(user_input)
#     print(f"Ditt nummer {user_number}")
# else:
#     print("Ange ett nummer")

# try:
#     user_input = input("Ange ett nummer: ")
#     user_number = int(user_input)
#     print(f"Ditt nummer: {user_number}")
# except ValueError:
#     print("Ange ett nummer")


# while True:
#     user_input = input("Ange ett number: ")
#     if user_input.isdigit():
#         user_number = int(user_input)
#         print(f"Ditt nummer {user_number}")
#         break
#     else:
#         print("Ange ett nummer")

# valid_options = ["ja", "nej", "kanske"]
# user_input = input("Tycker du om glass").lower()

# if user_input in valid_options:
#     print(f"Glass {user_input}")
# else:
#     print("Fel input")

## Klasser ##

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# car1 = Car("Toyota", "Corolla", 2020)
# print(car1.make)
# print(car1.model)
# print(car1.year)

# class Car:
#     wheels = 4


#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Volvo", "240", 1987)

# class Car:
#     wheels = 4

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def description(self):
#         return f"{self.year} {self.make} {self.model}"
    
# car2 = Car("Volvo", "240", 1987)
# print(car2.description())

## Arv ##

# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof"
    
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow"
    
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.speak())
# print(cat.speak())

# class Animal:
#     def __init__(self, name, legs):
#         self.name = name
#         self.legs = legs
    
#     def speak(self):
#         pass

# class Dog(Animal):
#     def __init__(self, legs, breed):
#         self.legs = legs
#         self.breed = breed

#     def speak(self):
#         return f"{self.name} says Woof"
    
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow"
    
# dog = Dog("Buddy", "Golden retriever")
# cat = Cat("Whiskers")

## Polymorfism ##

# class Dog():
#     def speak(self):
#         return "Woof"
    
# class Cat():
#     def speak(self):
#         return "Meow"
    
# def make_animal_speak(animal):
#     print (animal.speak())

# dog = Dog()
# cat = Cat()

# make_animal_speak(dog)
# make_animal_speak(cat)


###############
## Kapitel 6 ##
###############


## Modules ##

# import my_module

# print(my_module.greet("Bobbo"))
# print(my_module.add(5,5))

# from my_module import greet, add

# print(greet("Bobbo"))

# from my_package import module1, module2

# print(module1.function1())
# print(module2.function2())

# if __name__ == "__main__":
#     main()

# import math_op

# print(math_op.add(2,3))

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Fel: Division med noll")

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Fel: Division med noll")
# else:
#     print(f"Resultat: {result}")

# try:
#     value = int(input("Ange ett heltal: "))
#     result = 10 / value
# except ValueError:
#     print("Du måste ange ett heltal")
# except ZeroDivisionError:
#     print("Kan ej dela med 0")
# else:
#     print(f"Resultat: {result}")

# try:
#     file = open("test.txt", 'r')
#     content = file.read()
# except FileNotFoundError:
#     print("Filen finns inte")
# else:
#     print(content)
# finally:
#     try:
#         file.close()
#     except NameError:
#         pass



