#if-elif-else

#find if the number entered is positive or negative
try:
    number= float(input("enter number: "))


    if number >0:
        print(" number is positive")
    elif number <0:
        print("numbers is negative")

    else:
        print("number is zero")
except ValueError:
        print( "you cannot entrer string")        