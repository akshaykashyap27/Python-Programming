def largest(a,b,c):
    if(a>b) and (a>c):
        return(a)
    elif(b>a) and (b>c):
        return(b)
    else:
        return(c)

def year(age):
    if(age==100):
        return("You are 100 years old")
    elif(age<100):
        return ("You will turn 100 in " + str(2021 + (100 - age)))

    else:
        return ("You are more than 100 years old")