## Debugging ##

# number = int(input("Enter a number"))
# print(10 / 0)

# def calculate(length, width):
#     return length + width

# x = 15

# if x > 10:
#     print("x is greater than 10")

# try:
#     number = (int(input("Enter a number:")))
#     result = 10 / number
# except ValueError:
#     print("Not a number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# class MyError(Exception):
#     pass

# try:
#     raise MyError("This is my error")
# except MyError as e:
#     print(e)

## Assert ##

# x = 0
# assert x > 0, "x är inte större än 0"

## Logging ##

# import logging

# logging.basicConfig(filename='program.log', level=logging.DEBUG)
# logging.debug("Detta är ett debug-meddelande")
# logging.info("Detta är ett informationsmeddelande")
# logging.warning("Detta är en varning")
# logging.error("Detta är ett felmeddelande")
# logging.critical("Detta är ett kritiskt fel")

## pdb och breakpoints ##

# def add(a, b):
#     result = a + b
#     return result

# print(add(10, 12))

## Decorators ##

# def my_decorator(func):
#     def wrapper():
#         print("Innan funktionen")
#         func()
#         print("Efter funktionen")
#     return wrapper

# @my_decorator
# def print_some_text():
#     print("I funktionen")

# print_some_text()

# Generators ##

# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1

# counter = count_up_to(5)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# squares_list = [x * x for x in range(10)]

# squares_generator = (x * x for x in range(10))

# print(squares_list)
# print(list(squares_generator))

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num +=1

# infinite = infinite_sequence()
# print(next(infinite))
# print(next(infinite))
# print(next(infinite))
# print(next(infinite))
# print(next(infinite))

## Inbyggda moduler ##

# from collections import namedtuple

# point = namedtuple('Point', ['x', 'y'])

# p = point(10,20)

# print(p.x)
# print(p[0])

# from collections import deque

# d = deque([1,2,3,4,5])
# d.append(6)
# d.appendleft(0)

# print(d)

# d.pop()
# d.popleft()

# print(d)

# from collections import Counter

# c = Counter(['apple', 'banana', 'apple', 'orange', 'banana'])

# c.update(['apple', 'grape'])

# c.subtract(['apple'])
# print(c)

# from collections import defaultdict

# d = defaultdict(int)

# d['apple'] += 1
# d['grape'] += 2

# print(d)

# from collections import OrderedDict

## datetime ##

# from datetime import date

# datum = date(2024, 10, 8)
# print(datum)

# today = date.today()
# print(today)

# print(today.year)
# print(today.month)
# print(today.day)

# from datetime import time

# tid = time(10, 46, 25)
# print(tid)

# print(tid.hour)
# print(tid.minute)
# print(tid.second)

# from datetime import datetime

# datumtid = datetime(2024, 10, 8, 22, 48, 45)
# print(datumtid)

# from datetime import timedelta, datetime

# delta = timedelta(days=5, hours=3, minutes=30)
# print(delta)

# new_date = datetime(2023, 7, 17,22, 48, 45) + delta
# print(new_date)

# from datetime import timezone, datetime, timedelta

# utc_timezone = datetime.now(timezone.utc)
# print(utc_timezone)

# cest = timezone(timedelta(hours=2))
# local_cest = datetime.now(cest)
# print(local_cest)

# from datetime import datetime

# now = datetime.now()

# formatted = now.strftime("Datum: %Y-%m-%d Klockan: %H:%M:%S")
# print(formatted)

## Time ##

# import time

# current_time = time.time()
# print(current_time)

# time.sleep(2)

# local_time = time.localtime()
# print(f"Local time {time.strftime('%Y-%m-%d %H:%M:%S', local_time)}")

# import time

# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Funktionen {func.__name__} tog {end_time - start_time} sekunder")
#         return result
#     return wrapper

# @timer_decorator
# def calculate_sum(n):
#     return sum(range(n))

# print(calculate_sum(10000000))