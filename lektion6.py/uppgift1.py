# Uppgift 1
# Skapa en klass Person med attributen name och age.
# Använd en while-loop för att ta emot användarens namn och ålder.
# Validera att åldern är ett heltal
# Skapa och skriv ut ett Person-objekt om inputen är giltig.

class Person:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder
        
    def printperson(self):
        return f"{self.namn} {self.ålder}."

while True:
    Person1namn = str(input("Ange namnet till personen: "))
    try:
        Person1ålder = int(input("Ange ålder till personen: "))
        person1 = Person(Person1namn, Person1ålder)
        print(person1.printperson())
        break
    except ValueError:
        print("Endast heltal tillåtna")




