# 1. Multiplikationstabellen
# Skapa ett program som genererar och skriver ut en multiplikationstabell för ett tal
# som användaren matar in.
# Krav:
# ● En funktion för att skapa en multiplikationstabell.
# ● Programmet ska fråga användaren vilket tal som ska multipliceras och till
# vilket maxvärde.
# ● En funktion för att kontrollera om den inmatade strängen bara innehåller
# siffror. Använd funktionen isdigit()
# ● Skriv ut tabellen

# multiplication_table = []
# for i in range(1, 4):
#     for j in range(1, 4):
#         multiplication_table.append(i*j)
# print(multiplication_table)

# multiplication_table = [i * j for i in range(1, 4) for j in range(1, 4)]
# print(multiplication_table)


def multi_tabell():
    usernumber = input("Enter number: ")
    if usernumber.isdigit():
        #global convertednumber
        convertednumber = int(usernumber)
    usermaxvalue = input("Enter max value: ")
    if usermaxvalue.isdigit():
        #global convertedmax
        convertedmax = int(usermaxvalue)
    for i in range(0,11):
        result = convertednumber * i
        if result <= convertedmax:
            print(result)
                                

multi_tabell()



