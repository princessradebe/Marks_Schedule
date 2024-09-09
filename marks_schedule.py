# Get stu_num from user
try:
    stu_num = int(input('Enter student number: '))
except ValueError:
    print('Invalid student number entered')

# Get test scores from the user
print('Enter your test scores')
test_1 = input('Test 1: ')
test_2 = input('Test 2: ')
test_3 = input('Test 3: ')
test_4 = input('Test 4: ')

# Calculate the final grade
final_grade = (test_1 + test_2 + test_3 + test_4)/4

# Display the student number and their grades
print('Student No: ', stu_num)
print("Final grade: ", final_grade)
