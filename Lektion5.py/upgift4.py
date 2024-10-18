# Uppgift 1
# Skriv en funktion som tar emot ett godtyckligt antal args och kwargs, och sedan skriver ut
# dessa på ett strukturerat sätt.

def printargs(*args, **kwargs):
    print(args, kwargs)



printargs("hello","world", stad= "Heslinki", job ="Säljare")