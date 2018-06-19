# class-and-modules-2
#q1
class animal():
def_init_(self):
self.legs=2
self.wing=True
self.tail=False
def animal_attribute(self):
print("entering parent class animal")
print("animal attributes:\nlegs:%d\nwings:%r\ntail:%r"%(self.legs,self.wing,self.tail))
class pegion(animal):
print("flow in inherited class pegion")
t=pegion()
t.animal_attribute()
""
#q2
a is object of base class A
b is object of inherited class B
when we call functions f() or g() with respect to a,it executes content
of class A when we call f() or g() wrt b,we access class B first
a.f()='A' because we simply called function f() of A which returned via value 
of function g() of A
b.f()='B' because b can inherit it's parent class' methods .As we reach f()
of A,we come back to g() of b
a.g()='A' because we called function g() of class A which returned the value 'A'
b.g()='B' because we called function g() of class B which returned the value 'B'
#q3
def_init_(self,name,age,work_xp,desg):
self.name=name
self.age=age
self.xp=work_experience
self.desg=des
def display(self)
print("name:",self.name)
print("age:",self.age)
print("work experience:",self.xp)
print("designation:",self.desg)
def update(self,name,age,work_experience,des):
self.name=name
self.age=age
self.xp=work_experience
self.desg=des
def add(self):
location=input("enter current location:")
duration+int(input("enter duration of posting(in months):"))
print("current location:",location)
print("duration spent(in months):",duration)
class mission(cop):
def add_mission_details(self):
newlocation=input("enter new location:")
timespan=int(input("enter timespan of new location:"))
print("cop available for mission at %s for %d months"%(newlocation,timespan))
m=mission("xyz",32,4,"CBI field agent")
m.add()
m.add_mission_details()
#q4
class shape():
def_init_(self,i,b):
self.length=i
self.breadth=b
def area(self):
area=self.length*self.breadth
print("area:",area)
class square(shape):
print("square class")
class rectangle(shape):
print("rectangle class")
s=square(5,5)
r=rectangle(6,12)
s.area()
r.area()
