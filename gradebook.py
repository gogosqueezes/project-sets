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

def print_grades(sub):
    if sub in gradebook:
        print("Your grades in", sub, "are:")
        for grade in gradebook[sub]:
            print(grade)
    else:
        print("You're not taking that subject!! Such a silly goose! Do better.")


# Prints all subject averages and identifies the best and worst
def print_all_averages():
    bestsubname = ""
    worstsubname = ""
    bestavg = -1
    worstavg = 101

    for sub in gradebook:
        grades = gradebook[sub]
        average = sum(grades) / len(grades)
        print(sub, "average:", round(average, 2))

        if average > bestavg:
            bestavg = average
            bestsubname = sub

        if average < worstavg:
            worstavg = average
            worstsubname = sub

            
    print("Your BEST subject is ", bestsubname)
    print("Your WORST subject is ", worstsubname, "... better work on that!")