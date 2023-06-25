p1=int(input("Enter the age of 1st person\n"))
p2=int(input("Enter the age of 2nd person\n"))
p3=int(input("Enter the age of 3rd person\n"))
if p1<p2 and p1<p3:
    print("The 1st person with age", p1, "is the youngest among 3.")
elif p2<p1 and p2<p3:
    print("The 2nd person with age", p2, "is the youngest among 3.")
elif p3<p1 and p3<p2:
    print("The 3rd person with age", p3, "is the youngest among 3.")

if p1>p2 and p1>p3:
    print("The 1st person with age", p1, "is the oldest among 3.")
elif p2>p1 and p2>p3:
    print("The 2nd person with age", p2, "is the oldest among 3.")
elif p3>p1 and p3>p2:
    print("The 3rd person with age", p3, "is the oldest among 3.")
