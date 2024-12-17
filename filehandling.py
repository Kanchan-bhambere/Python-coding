# file is nothing but name of memory location on disk that stores data permnantly.
# file handling ids mechanism through which we can handle(read,write, create, etc) the file.


# to read fist 10 line
f= open("D:\ToDoApp\Python-coding\overloading and overriding.py", "r")
i=1
while i<=10:
    print(f.readline())
    i+=1

# to read first 30 charecter
f=open("D:\ToDoApp\Python-coding\overloading and overriding.py", "r")
print(f.read(30))

# to create file
a= open(" path ","x")
print("file created susccesfully")
# to add content in created file
a.write("My name is kancahn\n I am from matargaon\n I am an IT engineer\n I am learning Python langauge")
Print("Content added succesefully")
# To read all content from file
print(a.readline())
# reverse string using slicing operator

# File exception handling--File is not availabe

A=opent("D:\ToDoApp\Python-coding\exception.py", "r")
print(a.readline())
---->>> File is no available
# If exception occur
try:
    A=opent("D:\ToDoApp\Python-coding\exception.py", "r")   """file not craeted"""
    print(a.readline())
Except:
  print(" File is not available.. plaese craete first!")
Else: 
   a.close()                   """To close file"""
   print("File is closed ")  
O/P---->>>  File is not available.. plaese craete first!

#If no exception occur
try:
    A=opent("D:\ToDoApp\Python-coding\overloading and overriding.py", "r")     """File is there"""
    a.readline()
    print("Reading completed")
Except:
  print(" File is not available.. plaese craete first!")
Else: 
   a.close()                   """To close file"""
   print("File is closed ")  
O/P--->>> Reading completed
          File is closed

s="Hello, Welcome Home"
print(s[ : : -1])

#Instance variable
class Test:
    def __init__(self):
        self.a=10    #----instance variable
        print(self.a)
    def name(self):
        self.d = 5  #----instance variable
        print(self.d)

t1=Test()
t2=Test()
t1.name()
t2.c=15  #----instance variable
print(t1.__dict__)
print(t2.__dict__)

#Lambda expression

r=lambda a,b:a+b

print(r(10,20))

n=[1,2,3,4,5,6,7,8,9]
a=list(map(lambda x: x**2,n))
print(a)

#split and join methods
a= "I want to go home for vacation"
s=(a.split(" "))
print(s)
print(' '.join(s))
print(' '.join(s[::-1]))



