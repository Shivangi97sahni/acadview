#1
year=int(input("enter year"))
if (year%4==0):
    print("it is a leap year")
else:
    print("it is not a leap year")


#2
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("dimensions are of square")
else:
    print("dimensions are of rectangle")


#3
a=int(input("enter age"))
b=int(input("enter age"))
c=int(input("enter age"))
if(a>=b) and (a>=c):
    print("a is oldest")
else:
    print("a is youngest")
if(b>=a) and (b>=c):
    print("b is oldest")
else:
    print("b is youngest")
if(c>=a) and (c>=b):
    print("c is oldest")
else:
    print("c is youngest")


#4
a=int(input("number scored"))
if(a<=50):
    print("sorry! no prize")
    if(a>50 and a<=150):
        print("congratulations! you won a wooden dog")
    elif(a>151 and a<=180):
        print("congratulations! you won a book")
    if(a>181 and a<=200):
        print("congratulations! you won a chocolates")


#5
a=int(input("enter the quantity "))
c=a*100
if(c>1000):
    c=c*100-c/10
    print("discount given is ")
    print(c)
    print("cost after discount is ")
    print(c)
else:
    print("sorry no discount is given")