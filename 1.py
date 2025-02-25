#1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

#2

total = 0

for grade in grades:
    total += grade

average = total / len(grades)

print(f"The average grade is: {average:.2f}")
