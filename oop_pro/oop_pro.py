import random as rn
class person:
    def __init__(self, name):
        self.name = name
class footballist(person):
    def __init__(self,name,team_name):
        self.team_name = team_name
        person.__init__(self,name) 
    def get_info(self):
        print(self.name,self.team_name)
footplayer=[]
names=["حسین" , "مازیار" , "اکبر" , "نیما" ,  "مهدی" , "فرهاد" , "محمد" , "خشایار" , "میلاد" , "مصطفی" , "امین" , "سعید" , "پویا" , "پوریا" , "رضا" , "علی" , "بهزاد" , "سهیل" , "بهروز" , "شهروز" , "سامان" , "محسن"]
team="A"
for i in range(0,22):
    x=rn.choice(names)
    footplayer.append(footballist(x,team))
    names.remove(x)
    if(i==10):
        team="B"
for i in range(0,22):
    footplayer[i].get_info()