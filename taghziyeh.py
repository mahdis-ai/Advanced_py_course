class School: 
    def __init__(self,age_average,height_average,weight_average):
        self.age_average = age_average
        self.height_average = height_average
        self.weight_average = weight_average
    def getage(self):
        print(self.age_average)
    def getheight(self):
        print(self.height_average)
    def getweight(self):
        print(self.weight_average)
    def get_height_average(self):
        return self.height_average
    def get_weight_average(self):
        return self.weight_average
class Person:
    count=0
    def __init__(self,age,height,weight):
        self.age = age
        self.height = height
        self.weight = weight
c_a=int(input())
age_a=list(input().split())
height_a=list(input().split())
weight_a=list(input().split())
c_b=int(input())
age_b=list(input().split())
height_b=list(input().split())
weight_b=list(input().split())
persons_a=[]
persons_b=[]
aa=0
ha=0
wa=0
ab=0
hb=0
wb=0
for i in range(0,c_a):
    persons_a.append(Person(age_a[i],height_a[i],weight_a[i]))
    aa+=int(age_a[i])
    ha+=int(height_a[i])
    wa+=int(weight_a[i])
A=School(aa/c_a,ha/c_a,wa/c_a)
for i in range(0,c_b):
    persons_b.append(Person(age_b[i],height_b[i],weight_b[i]))
    ab+=int(age_b[i])
    hb+=int(height_b[i])
    wb+=int(weight_b[i])
B=School(ab/c_b,hb/c_b,wb/c_b)
A.getage()
A.getheight()
A.getweight()
B.getage()
B.getheight()
B.getweight()
if(float(A.get_height_average())>float(B.get_height_average())):
    print('A')
elif(float(A.get_height_average())<float(B.get_height_average())):
    print('B')
else:
    if(float(A.get_height_average())<float(B.get_height_average())):
        print('A')
    elif(float(A.get_height_average())>float(B.get_height_average())):
        print('B')
    else:
        print('Same')