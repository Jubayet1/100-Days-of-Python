# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# print(student_heights)
total_height = 0
total_students = 0
for student in student_heights:
  total_students += 1
  total_height += student

print(f'There are total {total_students} and their avarage height is {total_height/total_students}')
