# functions
# def is defining the function
from datetime import date


def cal_area_triangle(b, h):
    area = 0.5 * b * h
    print(area)


def area_of_square(side):
    area = side * side
    print('area of square', area)


area_of_square(20)
squares = [[3], [4], [9], [3], [6]]
for s in squares:
    area_of_square(s[0])


def say_hi(name, age=21):
    print("hello", name, "i am", age, "years old")


say_hi("sam")
say_hi("ann",19)


# function to print date
def print_todays_date():
    today = date.today()
    print(today)


print_todays_date()


# fuction to add as many numbers as possible
def add(*args):
    total = 0
    for num in args:
        total += num
        print("total is", total)


add(10, 5)
add(3, 9)

# the define and call function identification must match
# using a function is what we refer as calling a function
# t means the smaller triangle ie [5,6]
# b and h are the parameters ie is values inside a function

cal_area_triangle(8, 10)
cal_area_triangle(20, 30)
triangles = [[5, 6], [4, 5], [4, 8], [10, 20], [12, 15]]
for t in triangles:
    cal_area_triangle(t[0], t[1])
