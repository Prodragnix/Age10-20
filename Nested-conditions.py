print('This program enables whether you are allowed to go to college or not')
age=int(input('Please enter your age: '))
if age<10:
    print('You are not allowed to go to college.You are too young!')
elif age>=10:
    if age<=20:
        print('You are allowed to go to college.Good luck!')
    else:
        print('You are too old!You should know this stuff.')
else:
    print('ERROR! Please rerun the program! :(')