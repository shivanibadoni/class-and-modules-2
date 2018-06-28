#Q1.Animal 


class Animal():                              #Base Class
    def __init__(self):                      #Constructor
      self.legs = 2
      self.wing = True
      self.tail = False

    def animal_attribute(self):              #Function to showcase attributes of animal as Initialized earlier
      print("Entering parent class Animal")
      print("Animal attributes:\nLegs: %d\nWings: %r\nTail: %r" % (self.legs,self.wing,self.tail))
 
class Pegion(Animal):                         #Derived Class
    print("Flow in Inherited class Pegion")

#Driving Code    
T = Pegion()                                  #Object Creation of Class Pegion
T.animal_attribute()                         #Function invocation of base class

"""


#Q2.output of the code:


a is object of base class A 

b is object of inherited class B

when we call functions f() or g() with respect to a, it executes content of class A 
when we call f() or g() wrt b, we access class B first

a.f() = 'A' because we simply called function f() of A which returned via value of function g() of A
b.f() = 'B' because b can inherit it's parent class' methods. As we reach f() of A, we come back to g() of b
a.g() = 'A' because we called function g() of class A which returned the value 'A'
b.g() = 'B' because we called function g() of class B which returned the value 'B'
"""


#Q3.Cop


class Cop:                                         #Base class

  def __init__(self, naam, age, work_xp, desg):    #Constructor 
    self.name = naam
    self.age = age
    self.xp = work_xp
    self.desg = desg

  def Display(self):                               #Function to display details of Cop
    print("Name: ", self.name)
    print("Age:", self.age)
    print("Work Experience: ", self.xp)
    print("Designation: ",self.desg)

  def Update(self, name, age, work_experience, des):      #Function to update details of Cop
    self.name = name
    self.age = age
    self.xp = work_experience
    self.desg = des

  def Add(self):                                   #Function add details of Cop
    location = input("Enter Current location: ")
    duration = int(input("Enter duration of posting(in months): "))
    print("Current Location: ", location)
    print("Duration spent(in months): ",duration)


class Mission(Cop):                                #Derived Class 
  def add_mission_details(self):                   #Function make cop available add details of Mission
    NewLocation = input("Enter New Location: ")
    timespan = int(input("Enter Timespan of new location: "))
    print("Cop available for mission at %s for %d months" % (NewLocation, timespan))

#Driving Code
M = Mission("xyz", 30, 2, "CBI Field Agent")         #Object Creation of Derived Class 
M.Display()                                          #Invocation of Display function from Base Class 
M.Update("xyz", 32, 4, "CBI Field Agent")            #Invocation of Update function from Base Class 
M.Add()                                              #Invocation of Add function from Base Class 
M.add_mission_details()                              #Invocation of add_mission_details function from Derived Class


#Q4.Shape
class Shape():                                     #Base Class
  def __init__(self, l, b):                        #Constructor
    self.length = l
    self.breadth = b

  def Area(self):                                  #Function to calculate area 
    area = self.length * self.breadth 
    print("Area: ", area)

class Square(Shape):                               #Derived Class
  print("Square Class")

class Rectangle(Shape):                            #Derived Class
  print("Rectangle Class")                         #Driving Code
S = Square(5,5)                                    #Object Creation Derived Class Square
R = Rectangle(6,12)                                #Object Creation Derived Class Rectangle
S.Area()                                           #Invocation of Area function from Base Class 
R.Area()                                           #Invocation of Area function from Base ClasS 
