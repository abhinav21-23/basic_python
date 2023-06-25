quantity=int(input("Enter the quantity of purchased product\n"))
cost=quantity*100
if quantity>1000:
    total_cost=cost-(cost*0.1)
else:
    total_cost=cost
print("The total cost is:", total_cost)