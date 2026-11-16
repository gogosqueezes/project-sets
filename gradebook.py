import csv
def main(): #Menu that the user can navigate through and decide what they would like to use the gradebook for.
    print("Welcome to the Gradebook! This can either ruin your day or make it better, depending on how smart you are!")
    print("The Gradebook says that you are taking:", list(gradebook.keys()))
    print("Here's a list of what you can use the Gradebook for.")
    playing = True
    while playing == True:
        print("A. Print out each class and its average grade!")
        print("B. Print out all the grades for a specific class of your choice!")
        print("C. Print out the total, accumulative GPA across all of your classes!")
        print("D. See what your GPA is in letter form! (A, B, C, D, etc.)")
        print("E. Add a new grade to a subject!")
        print("F. Leave the Gradebook IMMEDIATELY")

        choice = input("Which option would you like to choose? (A-F): ").upper()
        if choice == "A":
            print_all_averages()
        elif choice == "B":
            print("Your current subjects are:", list(gradebook.keys()))
            sub = input("Which subject would you like to see?: ")
            for subject in gradebook:
                if sub.lower() == subject.lower():
                sub = subject
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
            print("Your current subjects are:", list(gradebook.keys()))
            sub = input("Which subject would you like to add a grade to?: ")
            for subject in gradebook:
                if sub.lower() == subject.lower():
                    sub = subject
            grade = float(input("What grade would you like to add? "))
            add_grade(sub, grade)
            print("Great. Your grade has been added!")
        elif choice == "F":
            save_grades()
            print("Okay.. I just saved your grades before you leave.")
            print("Byeee. Until next time!")
            playing = False
        else:
            print("That is NOT even an option girl... choose A, B, C, D, E, or F!")

gradebook = {}

with open("grades.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            sub = row[0]
            grades = []
            for grade in row [1: ]:
                grades.append(float(grade))
            gradebook[sub] = grades

def add_grade(sub, grade): #Allows for a grade to be added to its corresponding subject within the dictionary
    if sub not in gradebook:
        gradebook[sub] = []
    gradebook[sub].append(grade)

def print_average(sub): #Prints the average of one, specific subject
    if sub in gradebook:
        allgrades = gradebook[sub]
        average = sum(allgrades) / len(allgrades)
        print("Your average grade in ", sub, " is: ", round(average, 2))
    else:
        print("You're not taking that subject!! So silly! Do better.")

def print_grades(sub): #Prints all the individual grades in one, specific subject
    if sub in gradebook:
        print("Your grades in", sub, "are:")
        for grade in gradebook[sub]:
            print(grade)
    else:
        print("You're not taking that subject!! Such a silly goose! Do better.")

def print_all_averages(): #Prints all subjects and corresponding averages, then indicates users best and worst subjects
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

def get_GPA(): #Returns the users GPA across all subjects on a 4.0 scale
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

def save_grades(): # This method will save the updated grades and update the CSV file "grades.csv" as well
    with open("grades.csv", "w", newline = "") as f:
        writer = csv.writer(f)
        for sub in gradebook:
            row = [sub]
            for grade in gradebook[sub]:
                row.append(grade)
            writer.writerow(row)                
main()