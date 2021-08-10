name=input("enter your name:")
age=int(input("enter your age:"))
if(age==100):
    print("You are 100 years old")
elif(age<100):
    print("You will turn 100 in", 2021 + (100 - age))
else:
    print ("You are more than 100 years old")
