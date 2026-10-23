gradebook = {
    "Data Science": [100, 99, 98],
    "Physics": [95, 89, 94],
    "Calculus": [97, 90, 92]
}

def add_grade(sub, grade):
    if sub not in gradebook:
        gradebook[sub] = []
    gradebook[sub].append(grade)

def print_average(sub):
    if sub in gradebook:
        allgrades = gradebook[sub]
        average = sum(allgrades) / len(allgrades)
        print("Your average grade in ", sub, " is: ", round(average, 2))
    else:
        print("You're not taking that subject!! So silly! Do better.")
