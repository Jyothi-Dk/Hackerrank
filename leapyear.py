def is_leap(year):
    if(year%400==0):
        print("Its a leap year")
    elif(year%100==0):
        print("Its not a leap year")
    elif(year%4==0):
        print("Its a leap year")
    else:
        print("Its not a leap year")

year = int(input("Enter your year:"))
is_leap(year)
