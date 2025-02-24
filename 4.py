students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
#1
if grades[0]<80 :
    print(str(students[0])+" "+str(grades[0])+" "+str(activities[0]))
elif grades[1]<80 :
    print(str(students[1])+" "+str(grades[1])+" "+str(activities[1]))
elif grades[2]<80 :
    print(str(students[2])+" "+str(grades[2])+" "+str(activities[2]))
elif grades[3]<80 :
    print(str(students[3])+" "+str(grades[3])+" "+str(activities[3]))
#2
approved_students=[]
if grades[0]>80 :
    approved_students.append(students[0])
if grades[1]>80 :
    approved_students.append(students[1])
if grades[2]>80 :
    approved_students.append(students[2])
if grades[3]>80 :
    approved_students.append(students[3])

print(approved_students)
