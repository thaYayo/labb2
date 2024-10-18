# Create two variables a and b, and initially set them each to a different number. Write a program that swaps both values.


# Output: a = 20, b = 10
# Warning! Do not use the programming language MAGIC. After you complete the exercise feel free to do so.

def swap(a,b):
    return b,a

a = 10
b = 20
print(swap(a,b))

a,b = swap(a,b)
print("a:", a)
print("b:", b)

