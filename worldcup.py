
li=[]
ls=[]
lp=[]
lm=[]
li.insert(0,"Iran")
li.insert(1,0)
li.insert(2,0)
li.insert(3,0)
li.insert(4,0)
li.insert(5,0)
ls.insert(0,"Spain")
ls.insert(1,0)
ls.insert(2,0)
ls.insert(3,0)
ls.insert(4,0)
ls.insert(5,0)
lp.insert(0,"Portugal")
lp.insert(1,0)
lp.insert(2,0)
lp.insert(3,0)
lp.insert(4,0)
lp.insert(5,0)
lm.insert(0,"Morocco")
lm.insert(1,0)
lm.insert(2,0)
lm.insert(3,0)
lm.insert(4,0)
lm.insert(5,0)
a=input()
if(int(a[0])>int(a[2])):
    li[1]+=1
    li[4]+=int(a[0])-int(a[2])
    li[5]+=3
    ls[3]+=1
    ls[4]+=int(a[2])-int(a[0])
elif(int(a[0])==int(a[2])):
    li[3]+=1
    ls[3 ]+=1
    li[4]+=int(a[0])-int(a[2])
    ls[4]+=int(a[2])-int(a[0])
    li[5]+=1
    ls[5]+=1
else :
    li[2]+=1
    li[4]+=int(a[0])-int(a[2])
    ls[1]+=1
    ls[4]+=int(a[2])-int(a[0])
    ls[5]+=3
b=input()
if(int(b[0])>int(b[2])):
    li[1]+=1
    li[4]+=int(b[0])-int(b[2])
    li[5]+=3
    lp[3]+=1
    lp[4]+=int(b[2])-int(b[0])
elif(int(b[0])==int(b[2])):
    li[3]+=1
    lp[3 ]+=1
    li[4]+=int(b[0])-int(b[2])
    lp[4]+=int(b[2])-int(b[0])
    li[5]+=1
    lp[5]+=1
else :
    li[2]+=1
    li[4]+=int(b[0])-int(b[2])
    lp[1]+=1
    lp[4]+=int(b[2])-int(b[0])
    lp[5]+=3
c=input()
if(int(c[0])>int(c[2])):
    li[1]+=1
    li[4]+=int(c[0])-int(c[2])
    li[5]+=3
    lm[3]+=1
    lm[4]+=int(c[2])-int(c[0])
elif(int(c[0])==int(c[2])):
    li[3]+=1
    lm[3 ]+=1
    li[4]+=int(c[0])-int(c[2])
    lm[4]+=int(c[2])-int(c[0])
    li[5]+=1
    lm[5]+=1
else :
    li[2]+=1
    li[4]+=int(c[0])-int(c[2])
    lm[1]+=1
    lm[4]+=int(c[2])-int(c[0])
    lm[5]+=3
d=input()
if(int(d[0])>int(d[2])):
    ls[1]+=1
    ls[4]+=int(d[0])-int(d[2])
    ls[5]+=3
    lp[3]+=1
    lp[4]+=int(d[2])-int(d[0])
elif(int(d[0])==int(d[2])):
    ls[3]+=1
    lp[3 ]+=1
    ls[4]+=int(d[0])-int(d[2])
    lp[4]+=int(d[2])-int(d[0])
    ls[5]+=1
    lp[5]+=1
else :
    ls[2]+=1
    ls[4]+=int(d[0])-int(d[2])
    lp[1]+=1
    lp[4]+=int(d[2])-int(d[0])
    lp[5]+=3
e=input()
if(int(e[0])>int(e[2])):
    ls[1]+=1
    ls[4]+=int(e[0])-int(e[2])
    ls[5]+=3
    lm[3]+=1
    lm[4]+=int(e[2])-int(e[0])
elif(int(e[0])==int(e[2])):
    ls[3]+=1
    lm[3 ]+=1
    ls[4]+=int(e[0])-int(e[2])
    lm[4]+=int(e[2])-int(e[0])
    ls[5]+=1
    lm[5]+=1
else :
    ls[2]+=1
    ls[4]+=int(e[0])-int(e[2])
    lm[1]+=1
    lm[4]+=int(e[2])-int(e[0])
    lm[5]+=3
f=input()
if(int(f[0])>int(f[2])):
    lp[1]+=1
    lp[4]+=int(f[0])-int(f[2])
    lp[5]+=3
    lm[3]+=1
    lm[4]+=int(f[2])-int(f[0])
elif(int(f[0])==int(f[2])):
    lp[3]+=1
    lm[3 ]+=1
    lp[4]+=int(f[0])-int(f[2])
    lm[4]+=int(f[2])-int(f[0])
    lp[5]+=1
    lm[5]+=1
flag=True
l=[li[5],ls[5],lp[5],lm[5]]
for i in range(0,3):
    for j in range(i+1,3):
        if l[i]<l[j] :
            flag=False
    if flag==True :
        if i==0:
            print(li[0],"wins:",li[1],",","loses",li[2],",","draws",li[3],",","goal difference",li[4],",","points",li[5])
            break
        if i==1:
             print(ls[0],"wins:",ls[1],",","loses",ls[2],",","draws",ls[3],",","goal difference",ls[4],",","points",ls[5])
             break
        if i==2 :
            print(lp[0],"wins:",lp[1],",","loses",lp[2],",","draws",lp[3],",","goal difference",lp[4],",","points",lp[5])
            break
        if i==3 :
            print(lm[0],"wins:",lm[1],",","loses",lm[2],",","draws",lm[3],",","goal difference",lm[4],",","points",lm[5])
            break