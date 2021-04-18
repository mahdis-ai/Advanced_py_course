s=input().split()
b=""
flag=False
for i in range(0,len(s)):
    if(s[i][0].isupper()  and i>=1 and s[i-1][-1]!='.'):
        if( s[i][-1]=='.' or  s[i][-1]==','):
            a=len(s[i])
            b=s[i]
            flag=True
            print('%d:%s'%(i+1,b[0:a-1]))
        else:
            b=s[i]
            flag=True
            print('%d:%s'%( i+1 ,b[0:]))
if(flag==False):
    print("None")