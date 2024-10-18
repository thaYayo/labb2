# Uppgift 2
# Skapa en klass Rectangle med attributen length och width.
# Implementera metoder för att beräkna arean och omkretsen.
# Ta emot och validera input för length och width.
# Skriv ut arean och omkretsen

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length*self.width
        return f"Area is: {area}"
    
    def circumf(self):
        omkrets = (self.length*2) + (self.width*2)
        return f"circumferense is: {omkrets}"    


while True:
    längd = float(input("Ange längd: "))
    bredd = float(input("Ange bredd: "))
    rectangle1 = Rectangle(längd, bredd)
    print(rectangle1.area(), rectangle1.circumf())
    break

