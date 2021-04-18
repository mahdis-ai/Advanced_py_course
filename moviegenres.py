n=input()
Action=['Action',0]
Adventure=['Adventure',0]
History=['History',0]
Comedy=['Comedy',0]
Romance=['Romance',0]
Horror=['Horror',0]
for i in range(0,int(n)):
    a=[]
    b=input()
    a=list(b.split(' '))
    for j in range(1,len(a)):
        if a[j]==Action[0]: 
            Action[1]+=1
        if a[j]==Adventure[0]:
            Adventure[1]+=1
        if a[j]==History[0]:
            History[1]+=1
        if a[j]==Comedy[0]:
            Comedy[1]+=1
        if a[j]==Romance[0]:
            Romance[1]+=1
        if a[j]==Horror[0]:
            Horror[1]+=1
list=[Action,Adventure,History,Comedy,Romance,Horror]
list.sort(key=lambda x: x[0])
list.sort(reverse=True , key=lambda x: (x[1]))
for i in range(0,len(list)):
    print('%s  : %s'%(list[i][0],list[i][1]))
        
