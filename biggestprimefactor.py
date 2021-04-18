l=[]
for i in range(0,10,1):
    l.append(int(input()))
smax=0
imax=l[0]
for i in range(0,10):
    s=0
    for j in range(2,l[i]):
        if l[i]%j==0:
            w=0
            for x in range(2,j):
                if j%x==0:
                    w=w+1
            if w==0:
                s=s+1
        if s>=smax :
            smax=s
            if l[i]>imax:
                imax=l[i]
print(imax,"   ",smax)



