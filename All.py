
# Question 1 Task 1: Given list of grades.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)
print(grades)

# The sorted list
[95, 93, 90, 89, 88, 85, 80, 78, 76, 72]

# Question 1 Task 2: Calculate the average grade and display it.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average_grade = sum(grades)/len(grades)
print(average_grade)

# Question 1 Task 3:  Replace any grade below 80 with the value Failed.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades = ["Failed" if grade < 80 else grade for grade in grades]
print(grades)


# Question 2 Task 1: Given the two lists:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
attended = set(submitted).intersection(attended)
print(list(attended))

# Question 2 Task 2: Check if the two lists are identical in terms of their content, regardless of order.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print(submitted is attended)
print(submitted is not attended)
print(submitted != attended)
# Question 2 Task 3:  Using list methods, remove any student from the attended list who did not submit their assignment.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
attended = [student for student in attended if student in submitted]
print(attended)
# Question 3 Task 1:  Given the list of temperatures.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
#Extract the temperatures for the second week (7 days) of the month. Expected Outcome:

83, 85, 86, 87, 88, 89, 90,

print(temperatures[7:14])

# Question 3 Task 2:Extract all the temperatures above 100.
print(temperatures[24:30])
# Extracted temperatures
[101, 102, 103, 104, 105, 106]

# Question 3 Task 3: Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures.reverse()
print(temperatures)
# Reversed list
[106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 83, 82, 81, 80, 79, 78, 75, 72]
[101, 100, 99, 98, 97]

#extracted temperatures from the 5th to the 10th day of the reversed list.
print(temperatures[5:10])
[101, 100, 99, 98, 97]
# Question 4 Task 1: Given Lists:
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i in range (len(grades)):
    if grades [i] < 80:
        print(students[i], grades[i], activities[i])
# Question 4 Task 2: 
students_approved = ["John", "Doe", "Smith"]
grades = [85, 90, 88]
activities = ["Football", "Music", "Dance"]
students_approved.append(students[i])

# Question 4 Task 3: 
students_approved = ["John", "Doe", "Smith"]
grades = [85, 90, 88]
activities = ["Football", "Music", "Dance"]
students_approved.append(students[i])
print(students_approved)





