# Given a list of strings, return a dictionary with the strings as keys and frequency counts as the values.



def return_dict(strings):
    frekvens = {}

    for item in strings:
        if item not in frekvens:
            frekvens[item] = 1
        else:
            frekvens[item] += 1
    return frekvens

print(return_dict(["hello", "my", "neighbors", "hello"]))
