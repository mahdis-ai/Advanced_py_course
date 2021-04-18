n=int(input())
l=[]
for i in range(0,n):
    x=input().split('.')
    l.append(x)
    l[i][1]=l[i][1].lower()
    l[i][1]=l[i][1].capitalize()

l.sort(key=lambda x:x[1])
l.sort(key=lambda x:x[0])

for i in range(0,n):
    print(l[i][0]+" "+l[i][1]+" "+l[i][2])