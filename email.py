import re
seq=input()
result=re.findall(r'\d*\w+\d*\w+@\w+\.\w+',seq)
if (len(result)!=0 and result[0]==seq):
    print("OK")
else:
    print("WRONG")

