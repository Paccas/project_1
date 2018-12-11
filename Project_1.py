# Letter grade bot
pointspossible = 100
studentname = input("Student Name: ")

def calcthegrade():
    percent = score / pointspossible * 100
    grade = ""

    # Print the student name and what grade they got

    if percent >= 90:
        grade = "A"
    elif 90 > percent >= 80:
        grade = "B"
    elif 80 > percent >= 70:
        grade = "C"
    elif 70 > percent >=60:
        grade = "D"
    else:
        grade = "F"
        print("")
        print('{}\'s grade is {}'.format(studentname,grade))
try:
    score = int(input("What score did {} get on the exam? ".format(studentname)))
    calcthegrade()

except Exception:
    print("Please make sure you enter a number for the score.")
