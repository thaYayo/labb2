# Invert the following dictionary mapping names to ages to instead map ages to names.

ages = {"Mike": 20, "Jen": 19, "Sally": 21}
new_ages = {}


def invert_dict():
    #for loop reding keys in ages dict
    for names in ages:
        #craeting variable(age) conatining the values of of corresponding key(name) in age list
        age = ages[names]
        #adding keys to the dict(new_ages) with the new keys [age] and assigning values (names)
        new_ages[age] = names
    print(ages)
    print(new_ages)

invert_dict()

