# 2. Miniräknare
# Skapa en enkel miniräknare som kan utföra addition, subtraktion, multiplikation och
# division.
# Krav:
# ● Funktioner för varje matematiskt operation.
# ● Programmet ska ta in två tal från användaren och en operation som input.
# ● Hantera felaktig inmatning och division med 0.



## gemensamma variablar

## additions funktionen

def add(num1, num2):
   return num1 + num2


## subtraktion funktionen

def sub(num1, num2):
    return num1 - num2

## multiplikations funktionen

def mult(num1, num2):
    return num1 * num2

## division funktionen

def div(num1, num2):
    return num1 / num2


## miniräknar funktionen

def calculator():
    while True:
        try:
            num1 = float(input("Enter a number: "))
            operator = input("Enter arithmatic you wish to execute: ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = add(num1, num2)
                print(result)
                break
            elif operator == "-":
                result = sub(num1, num2)
                print(result)
                break
            elif operator == "*":
                result = mult(num1, num2)
                print(result)
                break
            elif operator == "/":
                result = div(num1, num2)
                print(result)
                break
            else:
                print("invalid operator ")
        except ValueError:
            print("Invalid datatype!!")


calculator()