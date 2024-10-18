# Uppgift 2
# Skriv ett program som använder lambda-uttryck tillsammans med map och filter för att
# bearbeta en lista av tal.
# Programmet ska först kvadrera alla tal i listan och sedan filtrera ut de tal som är större än ett
# angivet värde.
# Krav:
# Använd map för att kvadrera alla tal i listan.
# Använd filter för att behålla endast de tal som är större än ett specificerat värde.
# Använd lambda-uttryck för både map och filter


lista_tal = [1,4,8,5,1,4,7,9,3,1]

def squared(x):
    return x*x

squared = list(map(lambda x: x*x, lista_tal))


## squared blir x så den jämför bara med sig själv. fixa imorn
def greater(x):
    if x < 20:
        return x
##lambda for greater function

greaterthan = list(filter(lambda x: x if x > 20 else None, squared))

print(greaterthan)

