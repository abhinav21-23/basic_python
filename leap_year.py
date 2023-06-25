year=int(input("Enter the year\n"))
if(year%400==0 and year%4==0):
    print("The", year, "is a leap year")
else:
    print("The", year, "is not a leap year")