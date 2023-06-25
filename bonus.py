salary=int(input("Enter your salary\n"))
service=int(input("Enter your year of service\n"))
if(service>5):
    print("Your bonus is:", salary*0.05)
else:
    print("You still not completed more than 5 years of service to be eligible for the bonus.")
