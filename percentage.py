percent=int(input("Enter your percentage\n"))
if(percent>90):
    print("Grade A")
elif(percent>80 and percent<=90):
    print("Grade B")
elif(percent>=60 and percent<=80):
    print("Grade C")
else:
    print("Grade D")