'''
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
c=int(input("enter 3rd num:"))

if(a>b) and (a>c):
    print(a)
elif(b>a) and (b>c):
    print(b)
else:
    print(c)
    '''
name=input("enter your name:")
age=int(input("enter your age:"))
if(age==100):
    print("You are 100 years old")
elif(age<100):
    print("You will turn 100 in", 2021 + (100 - age))
else:
    print ("You are more than 100 years old")

'''     
def largest(a,b,c):
    if(a>b) and (a>c):
        return(a)
    elif(b>a) and (b>c):
        return(b)
    else:
        return(c)

result=largest(2,45,6)
print(result)


def year(age):
    if(age==100):
        return("You are 100 years old")
    elif(age<100):
        return "You will turn 100 in ", 2021 + (100 - age)
    else:
        return ("You are more than 100 years old")

result=year(10)
print(result)




while True:
    p1 = input("Input choice of p1:")
    p2 = input("Input choice of p2:")
    if p1 == p2:
        print("It's a tie!")
    elif p1 == "rock":
        if p2 == "scissors":
            print("p1 wins!!!")

        else:
            print("p2 wins!!!")

    elif p1 == "paper":
        if p2 == "rock":
            print("p1 wins!!!")

        else:
            print("p2 wins!!!")
    elif p1 == "scissors":
        if p2 == "paper":
            print("p1 wins!!!")
        else:
            print("p2 wins!!!")
    new_game = input("Do you want to play a new game? (y/n): ")
    if(new_game!='y'):
        break
'''