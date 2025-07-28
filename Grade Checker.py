print('''
GRADE CHECKER
''')

while True:
    marks = float(input("Type your marks out of 100:  "))
    if marks > 100 or marks < 0:
        print("Error: Input a number between 0-100 ")
    elif marks >= 90:
        print("Wow, A+")
    elif marks >= 75:
        print("Grade A")
    elif marks >= 55:
        print("Grade B")
    elif marks >= 35:
        print("Grade C [Just Passed]")
    else:
        print("failed :(")
        