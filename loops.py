#1
i=0
while(i<5):
    num=input("enter the number")
    print(num)
    i=i+1

#2
while True:
    print("INFINITE")


#3
numbers=[]
for i in range (0,8):
    num=int(input("enter the number"))
    numbers.append(num)
print("the list is",numbers)
squares=[]
for num in numbers:
    sq=num*num
    squares.append(sq)
print("the new list is",squares)


#4
l=[7,'sona',4.15,19,'ishi',9.8]
for i in l:
    print("the type is",i,"is",str(type(i)))


#5
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("list for even numbers is",even)
print("list for odd numbers is",odd)

#6
i=1
while i<=4:
    print("*"*i)
    i=i+1


#7
val={'rohru':'ishu','jammu':'shivi','kangra':'prachi'}
for key in val.keys():
    print(key,val[key])


#8
l=['corneto','magnum','baskin robbins','amul']
name=input("enter the name of ice cream")
for ice in l:
    if ice==name:
        print("available")
        l.remove(ice)
        print("list",l)