def main():
    print("Welcome to the Gradebook! This can either ruin your day or make it better, depending on how smart you are!")
    print("The Gradebook says that you are taking Data Science, Physics, and Calculus.")
    print("Here's a list of what you can use the Gradebook for.")
    playing = True
    while playing == True:
        print("A. Print out each class and its average grade!")
        print("B. Print our all the grades for a specific class of your choice!")
        print("C. Print out the total, accumulative GPA across all of your classes!")
        print("D. See what your GPA is in letter form! (A, B, C, D, etc.)")
        print("E. Leave the Gradebook IMMEDIATELY")

        choice = input("Which option would you like to choose? (Make sure to answer with a single, uppercase letter A-E): ")
        if choice == "A":
            print_all_averages()
        elif choice == "B":
            sub = input("Which subject would you like to see? (Data Science, Physics, or Calculus): ")
            print_grades(sub)
        elif choice == "C":
            print("Your overall GPA is:", get_GPA())
        elif choice == "D":
            gpa = get_GPA()
            if gpa >= 4.0:
                letter = "A"
            elif gpa >= 3.7:
                letter = "A-"
            elif gpa >= 3.0:
                letter = "B"
            elif gpa >= 2.0:
                letter = "C"
            elif gpa >= 1.0:
                letter = "D"
            else:
                letter = "F"
            print("Your GPA letter grade is:", letter)

        elif choice == "E":
            print("Byeee. Until next time!")
            playing = False
        else:
            print("That is NOT even an option girl... choose an uppercase letter A, B, C, D, or E!")

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

def print_all_averages():
    bestsubname = ""
    worstsubname = ""
    bestavg = -100
    worstavg = 200
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

def get_GPA():
    totalgpa = 0
    for sub in gradebook:
        grades = gradebook[sub]
        average = (sum(grades))/(len(grades))
        gpa = 0
        if average >= 92.5:
            gpa = 4.0
        elif average >= 89.5:
            gpa = 3.7
        elif average >= 79.5:
            gpa = 3.0
        elif average >= 69.5:
            gpa = 2.0
        elif average >= 65:
            gpa = 1.0
        else:
            gpa = 0.0

        totalgpa += gpa
    
    finalgpa = totalgpa / len(gradebook)
    return finalgpa

main()