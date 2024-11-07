

entered_value=input("enter score:")

if not entered_value.isnumeric():
    print("enter a valid figure fellow")
    exit(0)#stop
score=int(entered_value)# converting it to number


if score >=70:
    print('A')
elif score >=65 and score <70:
   print('A-')
elif score >=60 and score <65:
   print('B+')
elif score >=55 and score <60:
   print("B")
elif score >=50 and score <55:
   print("B-")
else:
    print('C')
