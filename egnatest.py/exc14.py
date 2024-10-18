# Given two lists, find the unique elements in both using sets.

list1 = [1, 2, 3, 4]
list2 = [2, 4, 6, 8]

set1 = set(list1)
set2 = set(list2)

print(set1 ^ set2)