#calculator program
x=input("enter the first number:")
y=input("enter the second number:")
z=input("enter the third number:")
try:
    x_num=int(x)
    y_num=int(y)
    z_num=int(z)
    print(x_num*y_num*z_num)
except:
    print("enter valid number")

