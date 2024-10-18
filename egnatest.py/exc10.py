# Write a function that takes a list of integers and returns a new list containing only those greater than 5.

list = [10,6,4,3,8,1,5]

def show_numbers():
    greaterthan = []
    for numbers in list:
        if numbers > 5:
            greaterthan.append(numbers)
    print(greaterthan)

show_numbers()


