print('**** Welcome to the LAB grade calculator! ****')
print()

name = input('Who are we calculating grades for? ==> ')
print()

#if user input is > 100 or < 0
labs = int(input('Enter the Labs grade? ==> '))
if (labs > 100):
  labs = 100
  print('The lab value should have been 100 or less. It has been changed to 100.')
if (labs < 0):
  labs = 0
  print('The lab value should have been zero or greater. It has been changed to zero.')
print()
exams = int(input('Enter the EXAMS grade? ==> '))
if (exams > 100):
  exams = 100
  print('The exam value should have been 100 or less. It has been changed to 100.')
if (exams < 0):
  exams = 0
  print('The exam value should have been zero or greater. It has been changed to zero.')
print()
attendance = int(input('Enter the attendance grade? ==> '))
if (attendance > 100):
  attendance = 100
  print('The attendance value should have been 100 or less. It has been changed to 100.')
if (attendance < 0):
  attendance = 0
  print('The attendance value should have been zero or greater. It has been changed to zero.')

#weighted grade calculations
weighted_labs = labs * 0.7
weighted_exams = exams * 0.2
weighted_attendance = attendance * 0.1
weighted_total = weighted_labs + weighted_exams + weighted_attendance

print()
print('The weighted grade for', name, 'is', weighted_total)

#determine grades from user input
if (90 <= weighted_total <= 100):
    print(name, 'has a letter grade of A')
elif (80 <= weighted_total < 90):
    print(name, 'has a letter grade of B')
elif (70 <= weighted_total < 80):
    print(name, 'has a letter grade of C')
elif (60 <= weighted_total < 70):
    print(name, 'has a letter grade of D')
elif (0 <= weighted_total < 60):
    print(name, 'has a letter grade of F')
else:
    print('Invalid input')

print()
print('**** Thanks for using the Lab grade calculator ****')
