from datetime import date
birth=input().split('/')
if(int(birth[1])<1 or int(birth[1])>12 or int(birth[2])<0 or int(birth[2])>31):
    print("WRONG")
else:
    birthDate = date(int(birth[0]), int(birth[1]), int(birth[2]))
    today=date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day))
    print(age)