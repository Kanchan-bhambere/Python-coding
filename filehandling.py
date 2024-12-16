
f= open("D:\ToDoApp\Python-coding\overloading and overriding.py", "r")
i=1
while i<=10:
    print(f.readline())
    i+=1

# reverse string using slicing operator

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



