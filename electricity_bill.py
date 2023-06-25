units=int(input("Enter the no. of units consumed\n"))
bill=0
if(units<=100):
    bill=0
elif(units>=101 and units<=200):
    bill=(units-100)*5
else:
    bill=100*5 + (units-200)*10
print("The electricity bill is:", bill)

