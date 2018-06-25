#1
class Circle():
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        print(3.14*self.radius*self.radius)
    def getCircumference(self):
        print(self.radius*2*3.14)

c = Circle(radius=4)
c.getArea()
c.getCircumference()


#2
class student():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print(self.name)
        print(self.rollno)
    def setAge(self,age):
        self.age = age
        print(self.age)

s = student("shivi", '45')
s.display()
s.setAge(21)


#3
class temperature():
    def convertFahrenhiet(self,celsius):
        print((celsius*(9.0/5.0))+32.0)

    def convertCelsius(self,fahrenhiet):
        print((fahrenhiet-32.0)*(5.0/9.0))

t = temperature()
t.convertCelsius(98.6)
t.convertFahrenhiet(37.5)


#4
class MovieDetails():
    def __init__(self,moviename,artistname,year,ratings):
        self.moviename=moviename
        self.artistname=artistname
        self.year=year
        self.ratings=ratings
    def display(self):
        print(self.moviename)
        print(self.artistname)
        print(self.year)
        print(self.ratings)
    def update(self,update):
        self.update=update
        print(self.update)

m=MovieDetails("ABCD","Varun",'2015','7.5/10.0')
m.display()
m.update('2016')


#5
class Expenditure():
    def __init__(self,expenditure,savings):
        self.expenditure=expenditure
        self.savings=savings
    def display(self):
        print(self.expenditure)
        print(self.savings)
    def total_salary(self,total_salary):
        self.total_salary = total_salary
        print(self.expenditure*total_salary/100)
        print(self.savings*total_salary/100)
    def display_salary(self,display_salary):
        self.display_salary=display_salary
        print(self.display_salary)

e=Expenditure(expenditure=7000,savings=15000)
e.display()
e.total_salary(40000)
e.display_salary(7575546)



