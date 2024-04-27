print("~~~~Welcome in grading Software~~~~")

s1 = float(input("Enter marks for Subject 1 : "))
s2 = float(input("Enter marks for Subject 2 : "))
s3 = float(input("Enter marks for Subject 3 : "))
s4 = float(input("Enter marks for Subject 4 : "))
s5 = float(input("Enter marks for Subject 5 : "))

t_m = s1 + s2 + s3 + s4 + s5
average_marks = t_m / 5


if average_marks >= 90:
    grade = "A++"
elif average_marks >= 80:
    grade = "A+"
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B+"
elif average_marks >= 50:
    grade = "B"
elif average_marks >= 40:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)
