#Faulty Calculator
import random
a=int(input("Enter a no.\n"))
b=int(input("Enter the 2nd no.\n"))
print("Choose your operator:- +,-,/,*,**,//, %\n")
operator=input("Enter your operator")
if operator=="+":
    c=random.randrange(1,100)
    print(c)
elif operator=="-":
    c=random.randrange(1,100)
    print(c)
elif operator=="/":
    c=random.randrange(1,100)
    print(c)
elif operator=="*":
    c=random.randrange(1,100)
    print(c)
elif operator=="**":
    c=random.randrange(1,100)
    print(c)
elif operator=="//":
    c=random.randrange(1,100)
    print(c)
elif operator=="%":
    c=random.randrange(1,100)
    print(c)
else:
    print("invalid")

