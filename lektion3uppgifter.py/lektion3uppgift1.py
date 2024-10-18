# 1. FizzBuzz
# Klassisk uppgift. Loopa genom 1-100 med följande regler:
# ● Om talet är delbart med 3, skriv ut "Fizz".
# ● Om talet är delbart med 5, skriv ut "Buzz".
# ● Om talet är delbart med både 3 och 5, skriv ut "FizzBuzz".
# ● Annars, skriv ut talet självt.

x = 0
while x < 100:
    #string = ""
    x += 1
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

