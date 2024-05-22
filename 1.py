# Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades , reverse=True)
print(f"Sorted grades in descending order:", sorted_grades)

# Task 2
average_grade = (grades[0]+grades[1]+grades[2]+grades[3]+grades[4]+grades[5]+grades[6]+grades[7]+grades[8]+grades[9])/len(grades)
print(f"Average grade:", average_grade)

# Task 3
grades[2] = "failed"
grades[8] = "failed"
print(f"Modified grades" , grades)


