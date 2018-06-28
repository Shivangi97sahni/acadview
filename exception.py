#1
#exception occured is ZeroDivisionError
try:
 a = 3
 if(a<4):
     a = a/(a-3)
     print(a)
except ZeroDivisionError:
    print("num is divided by 0")


#2
#exception occured is IndexError
try:
    a=[1,2,3]
    print(a[3])
except (ZeroDivisionError,IndexError):
    print("num is divided by 0")


#3
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")

#Output will be An exception


#4
def AbyB(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#Output will be -5.0, a/b result in 0


#5
try:
    import shivangi
    a=[1,2,3]
    print(a[3])
except IndexError:
    print("Index does not exist")
except ImportError:
    print("file doesnot exist")
except ValueError:
    print("number should be int")



#6
class AgeTooSmallError(Exception):
    pass
while True:
 try:
    a=int(input("Enter age"))
    if(a<18):
        raise AgeTooSmallError
    break
 except ValueError:
    print("Please enter int")
 except AgeTooSmallError:
    print("Your age is less than 18")

print("You are eligible")



