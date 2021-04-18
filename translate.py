n=int(input())
l=[]
for i in range(0,n):
    x=input().split()
    l.append(x)
s=input().split()
for i in range(0,len(s)):
    for j in range(0,n):
        if(s[i]==l[j][1]or s[i]==l[j][2] or s[i]==l[j][3]):
            s[i]=l[j][0]
print(' '.join(s))

