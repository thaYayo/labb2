import os

# 3. Shoppinglista
# Skapa ett program som hanterar en inköpslista. Programmet ska kunna:
# ● Lägga till, ta bort och visa alla varor till inköpslistan.
# ● Spara inköpslistan till en textfil (användaren får välja filnamn).
# Krav:
# ● Programmet ska ha en meny där användaren kan välja att lägga till varor, visa
# listan, ta bort varor, spara listan eller avsluta programmet.
# ● Använd funktioner för att strukturera koden och hantera varje menyval.


# function till lägga till varor till listan

def appenlist(itemname):
    inköpslista.append(itemname)

# function till ta bort varor från listan

def removelist(itemname):
    inköpslista.remove(itemname)


## function till att visa innehållet av listan

def showlist(inköpslista):
    print(inköpslista)           


inköpslista = []

def lista():
    while True:
        print("1. Lägga till varor")
        print("2. Ta bort varor")
        print("3. Visa varor")
        print("4. Spara lista som en txt.fil")        
        print("5. Avsluta program")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            itemname = input("Ange vara du vill lägga till: ")
            appenlist(itemname)
            print("******************")

        elif choice == "2":
            itemname = input("Ange vara du vill ta bort: ")
            removelist(itemname)
            print("******************")

        elif choice == "3":
            showlist(inköpslista)
            print("******************")
        
        elif choice == "4":
            strlista = str(inköpslista)
            listname = input("Ange namnet på listan: ")
            if  not os.path.exists(listname):
                with open(listname, "w") as file:
                    file.write(strlista)
            else:
                print("Filen existerar redan.\n")

        elif choice == "5":
            print("Avslutar programmet....")
            break
        else:
            print("Ogiltigt val!\n")

lista()

