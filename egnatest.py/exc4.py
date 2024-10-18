# The exercise is almost identical to a previous exercise with a minor change. It's the end of the semester and you got your marks from, Geometry, Algebra, Physics classes. 
# If the average score is 7 and above print "Good job!", 
# if the average score is between 6 and 4 print "You need to work harder!", if the average score is below 4 print "Failed, you really need to work harder!".

# Create a program that:

# Reads the values of these 3 lessons
# Calculate the average of your grades
# Example: Geometry = 6, Algebra = 7, Physics = 8
# Output: Your average score is 7, Good job!"
# Warning! Do not use the programming language magic. After you complete the exercise feel free to do so.


classes = {"Geometry": 2, "Algebra": 2, "Physics": 5}



grades = classes.values()

result = sum(grades)

divisor = len(classes.keys())

average_grades = result / divisor 



def average():
    if average_grades >= 7:
        print("Good job!")
    if average_grades < 6:
        print("You need to work harder!")
    if average_grades < 4:
        print("Failed, you really need to work harder!")
    else:
        exit()

average()    



