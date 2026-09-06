name = input("Enter your name:")
roll = input("Enter your roll:")
board = input("Enter your board:")
GPA = float(input("Enter your GPA:"))

if GPA == 5.00:
    print(name, roll, board, GPA,
          "CONGRATULATIONS YOU HAVE GOT GPA 5.00. WE APPRICIATE YOUR HARDWORK AND SUCESS")
elif GPA != 5.00:
    print("Sorry you have missed gpa 5.00")
