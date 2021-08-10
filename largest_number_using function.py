def largest(a,b,c):
    if(a>b) and (a>c):
        return(a)
    elif(b>a) and (b>c):
        return(b)
    else:
        return(c)

result=largest(2,45,6)
print(result)