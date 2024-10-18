# Write a function to find all duplicate values in a list.



def show_duplicates():
    list = [4,6,3,3,1,8,7]
    seen = set()

    for nums in list:
        if nums in seen:
            print(nums)
        else:
            seen.add(nums)

show_duplicates()