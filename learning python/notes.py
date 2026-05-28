# 2D lists
'''''''''
drinks = ["pop", "water", "coffee", "tea"]
dinner = ["pizza", "spaghetti"]
lunch = ["sandwich"]

food =  [lunch, dinner, drinks]

print(food)
'''''''''
from select import KQ_FILTER_AIO

# tuples
'''''''''
name_age_gender = ("shawn" ,19, "male")
print(name_age_gender.index(19))
print(name_age_gender.count("male"))
age = name_age_gender[1]
print(age)
name_age = name_age_gender[0:2]
print(name_age)
for x in name_age_gender:
    print(x)
if age >= 18:
        print("shawn is old")
'''''''''

# sun project
'''''''''
from turtle import*

speed(0)
bgcolor("black")
colors=['orange', 'white']
hideturtle()
for i in range(122):
    goto (0,0)
    color(colors[i%2])
    left(3)
    forward (130)
    circle(40)
    forward (130)
    right(180)
done()
'''''''''

# bill calculator
'''''''''
pre_total = float(input("how much was your bill"))
tax = 0.09
tax_in_bill = pre_total * tax
total = pre_total * tax + pre_total
service = input("how was you service? good, okay, bad?")
if service == "good":
    tip = total * 0.20 + total
elif service == "okay":
    tip = total * 0.15 + total
elif service == "bad":
    tip = total * 0.10 +total
else:
    tip = total * 1.00

print("Bill summary")
print("--------------")
print(f"your final bill is ${pre_total:.2f}")
print(f"tax {tax_in_bill}")
print("suggested tip {service}")
'''''''''

#sets

'''''''''
bedding = {"sheets", "comforter", "pillows", "blanket"}
couch_items = {"pillow", "blanket", "cushions"}

bedding.add("pillow case")
bedding.remove("comforter")
#couch_items.clear()
#bedding.update(couch_items)
#print(bedding.union(couch_items))
print(bedding.difference(couch_items))
print(bedding.intersection(couch_items))
'''''''''

# dictionary
'''''''''
car = {"Make" : "Kia", "Model" : "Optima FE", "Year" : 2018}
print(car["Year"])
car.update({"Color" : "White"})
car.update({"Year" : 2024})
car.pop("Model")
print(car)

for key, value in car.items():
    print(key, value)
for value in car.values():
    print(value)
'''''''''

# index functions
'''''''''
name = "savvy westerberg"
if (name[0].lower()):
    name = name.capitalize()
last_name = name[5:]
last_name = last_name.upper()
first_name = name[:5]
print(last_name)
'''''''''

#funtions
'''''''''
def savvy(name, age):
    print("hello", name)
    print("you are", str(age), "years old")
    print("have a nice day", name)
name = input("whats your name ")
savvy(name, 18)
'''''''''

# nested functions
'''''''''
print((round(abs(float(input("whats your age?" ))))))
'''''''''

#args
'''''''''
def ages(*args):
    sum = 0
    args = list(args)
    args[0] = 19

    for a in args:
        sum += a
    return sum
print(ages(18,19))
'''''''''
#kwargs
'''''''''
def name(**kwargs):
    print("hello",end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")
name(first = "shawn", middle = "paul", last = "martin")
'''''''''

#string formation
'''''''''
name = "shawn"
age = 19
print("hello {1}, you are {0} years old".format(name, age))


print("hello {}, you are {} years old".format("shawn", "19"))
'''''''''

#exception handling
'''''''''
try:
    numerator = int(input("enter a number you want to divide "))
    denominator = int(input(f"enter a number you want to divide {numerator} by: "))
    answer = numerator / denominator
except ZeroDivisionError as e:
    print("you cannot divide by zero!")
except ValueError as e:
    print("you must enter a number")
except Exception as e:
    print("something went wrong")
else:
    print(answer)
'''''''''

#file detection
'''''''''
import os
path = "/Users/shawnmartin/Desktop/poop.rtf"
if os.path.exists(path):
    print("file exists")
    if os.path.isfile(path):
        print("this is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("file does not exists")
'''''''''

#read a file
'''''''''
import os

path = "/Users/shawnmartin/Desktop/test.txt.rtf"
try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")
'''''''''

#write a file
'''''''''
text = "Cannot wait to see savvy!"
with open ("text.text", "a") as file:
    file.write(text)
'''''''''

#copy a file
'''''''''
import shutil

shutil.copyfile("text.text", "new.text")
'''''''''

#move a file
'''''''''
import os

source = "new.text"
destination = "/Users/shawnmartin/desktop/new.text"

try:
    if os.path.exists(destination):
        print("file exists")
    else:
        os.replace(source, destination)
        print(source + "was moved ")
except FileNotFoundError:
    print("file was not found")
'''''''''

#remove/delete folder/directory
'''''''''
import os
import shutil

path = "text.txt"

try:
    os.remove(path) - remove file
    os.rmdir(path) - remove directory
    os.rmtree(path) - remove folder containing files
except FileNotFoundError:
    print("file not found")
else:
    print("file deleted")
'''''''''

'''''''''

#Object-Oriented Programming
class EnergyDrinks:
    def __init__(self, brand, flavor, store, caffeine):
        self.brand = brand
        self.flavor = flavor
        self.store = store
        self.caffeine = caffeine
    def good(self):
        print(f"{self.brand} is very good")
    def bad(self):
        print(f"{self.brand} is not very good")
    def __str__(self):
        return f"{self.brand}, {self.flavor}, {self.store}, {self.caffeine}"

drink_1 = EnergyDrinks("Alani", "Orange Crush", "Walmart", "200mg")
print(drink_1)
drink_1.good()
'''''''''

#importing classes from other files
'''''''''
#other file named "class cars.py" with "class Car"
class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def stock(self):
        print(f"The {self.color}, {self.year}, {self.make}, {self.model} is currently available for purchase ")
--------------------
from cars import Car

dream_car = Car("Neon green", 2026, "Lamborgini", "Hurrican")
current_car = Car("White", 2018, "Kia", "Optima FE")

dream_car.stock()

#class varibles - default value for variable
wheels = 4
print(dream_car.wheels)
-- prints "4"
'''''''''


#inheritence/multi_level
'''''''''
class Animal:
    alive = True

    def sleep(self):
        print("this animal sleeps")

    def eat(self):
        print("this animal eats")

class Falcon(Animal):
    def falcon(self):
        print("this animal can fly")

class Turtle(Animal):
    def turtle(self):
        print("this animal swims")

turtle = Turtle()
falcon = Falcon()
'''''''''

#mulitple inheritance
'''''''''
class Prey():
    def runs(self):
        print("this animal runs from predetors")


class Predetor():
    def hunts(self):
        print("this animal hunts prey")

class Shark(Predetor, Prey):
    pass
class Lion(Predetor):
    pass
class Bunny(Prey):
    pass

shark = Shark()
lion = Lion()
bunny = Bunny()

shark.hunts()
shark.runs()
'''''''''

#method overriding
'''''''''
class Animal:

    def eats(self):
        print("this animal eats")

class Bunny(Animal):
    def eats(self):
        print("this animal eats grass")

bunny = Bunny()
bunny.eats()
'''''''''

#method chaining
'''''''''
class Car:

    def turn_on(self):
        print("turn on car")
        return self

    def drive(self):
        print("drive the car")
        return self

    def brake(self):
        print("brake")
        return self

car = Car()

car.brake().drive()
'''''''''

#super function
'''''''''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self. width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.length * self.width

square = Square(4, 6)
cube = Cube(3, 6,8)

print(square.area())
print(cube.volume())
'''''''''

#abstract classes
'''''''''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("this car dirves")

class Voom(Vehicle):
    def stop(self):
        print("this car is topped")
    def go(self):
        print("this car goes")

car = Car()
voom = Voom()
voom.go()
'''''''''

#objects as arguments
'''''''''
class Car:
    color = None

class Motorcycle:

    color = None

def change_color(car, color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1, "blue")
change_color(car_2, "red")
change_color(car_3, "white")
change_color(bike_1, "black")

print(car_1.color, car_2.color, car_3.color, bike_1.color)
'''''''''

#duck typing
'''''''''
class Duck:
    def walk(self):
        print('this duck is waddling')

    def talk(self):
        print('this duck quacks')

class Chicken():
    def walk(self):
        print('this chicken is walking')

    def talk(self):
        print('this chicken gobbles')

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('you caught emas chicken')

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
'''''''''

#walrus operator
'''''''''
foods = list()
while food := input("what are you favorite foods?") != "quit":
    foods.append(food)
'''''''''

#functions to variables
'''''''''
def hi():
    print("hello")

hello = hi
hello()
'''''''''

#higher order functions
'''''''''
def quiet(text):
    return text.lower()

def loud(text):
    return text.upper()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

def mult(x):
    def by(y):
        return x * y
    return by

multiply = mult(3)
print(multiply(3))
'''''''''

#lambda function
'''''''''
multiply = lambda x, y, z: x * y * z
print(multiply(2,3,2))
#
name = lambda first_name, last_name, middle_name: first_name + " " + middle_name + " " + last_name
print(name("shawn", "martin", "paul"))
#
age_check = lambda age: True if age >= 18 else False
print(age_check(12))
'''''''''

#sort
'''''''''
names = ("pat", "sav", "shawn")
sorted_names = sorted(names, reverse=True)
for i in sorted_names:
    print(i)
#
students = [("savvy", 18, "A"), ("shawn", 19, "A"), ("eli", 13, "C")]

age = lambda students: students[1]
students.sort(key = age)

for i in students:
    print(i)
#
student = (("savvy", 18, "A"), ("shawn", 19, "A"), ("eli", 13, "C"))
ages = lambda student:student[0]
sort_students = sorted(student, key=age)

for b in student:
    print(b)
'''''''''

#map()
'''''''''
store = [("shirt", 20), ("food", 40)]

to_euros = lambda price: (price[0], price[1]*0.82)
to_dollars = lambda price: (price[0], price[1]/0.82)

store_price = list(map(to_euros, store))

for i in store_price:
    print(i)
'''''''''

#filter
'''''''''
buddies = [("tanner", 19), ("graydon", 19), ("emmitt", 19), ("alex", 17), ("eli", 13)]

age = lambda ages: ages[1] >= 18

weed = list(filter(age, buddies))

for i in weed:
    print(i)
'''''''''

#reduce
'''''''''
import functools

numbers = [1, 3, 5, 6, 7]
result = functools.reduce(lambda x, y: x * y, numbers)
print(result)
'''''''''

#list comprehensions
'''''''''
scores = [100, 60, 30, 90, 55, 0]

passed_students = [i if i >= 60 else "Failed" for i in scores]
print(passed_students)
'''''''''

#dictionary comprehensions
'''''''''
cities = {"LA": 90, "MN": 70, "Yes":80, "Alaska": 30}

city_tempsC = {key: round((value-32) * (5/9))  for (key, value) in cities.items()}
print(city_tempsC)

weather = {"La": "sunny", "MN": "snowy", "alaska": "snowy", "arizona": "HOTTTTT"}
sunny = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny)

cities = {"LA": 90, "MN": 70, "Yes":80, "Alaska": 30}
weat = {key: ("warm" if value >= 70 else "cold") for (key,value) in cities.items()}
print(weat)


def check_temp(value):
    if value >= 80:
        return "hot"
    elif 80 > value >= 60:
        return "warm"
    else:
        return "cold"

cities = {"LA": 90, "MN": 70, "Yes":80, "Alaska": 30}
d_c = {key: check_temp(value) for (key, value) in cities.items()}
print(d_c)
'''''''''

#zip
'''''''''
usernames = ("shmeep12", "savarooni", "nightttt")
passwords = ("18d92", "123s", "p@ssword")
login = ("1/23/26", "3/29/26", "5/13/26")

users = list(zip(usernames, passwords,))

for key, value in users:
    print("username: "+ key + " : " + "password: " + value)

use = zip(usernames, passwords, login)

for i in use:
    print(i)
'''''''''

#if __name__ == "__main__"
'''''''''
def hello():
    print("hello")
if __name__ == "__main__":
    hello()
'''''''''

#time module
'''''''''
import time

print(time.ctime(0))

print(time.time())

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H: %S,", time_object)
print(local_time)

time_string = "20 April, 2026"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)


time_tuple = (2026, 2, 20, 4, 20, 0, 0, 20, 0)
time_string = time.asctime(time_tuple)
print(time_string)
'''''''''

#threading
'''''''''
import threading
import time

def eat():
    time.sleep(3)
    print("you woke ate")
def wake_up():
    time.sleep(2)
    print("you woke up")
def shower():
    time.sleep(4)
    print("you showered")

x = threading.Thread(target = eat)
x.start()
y = threading.Thread(target = wake_up)
y.start()
z = threading.Thread(target = shower)
z.start()

x.join()
y.join()
z.join()


#eat()
#wake_up()
#shower()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
'''''''''

#daemon threads -IO bound
'''''''''
import threading
import time
def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "second")

x = threading.Thread(target=timer, daemon = True)
x.start()

#x.setDaemon(True)
#print(x.isDaemon)
answer = input ("do you wish to exit?: ")
'''''''''

#multiprocessing -CPU bound
'''''''''
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    start = time.perf_counter()
    a = Process(target=counter, args=(250000000,))
    a.start()
    a.join()

    b = Process(target=counter, args=(250000000,))
    b.start()
    b.join()

    c = Process(target=counter, args=(250000000,))
    c.start()
    c.join()

    d = Process(target=counter, args=(250000000,))
    d.start()
    d.join()

    print("finished in", time.perf_counter() - start, "seconds")

if __name__ == "__main__":
    main()
'''''''''

#GUI windows
'''''''''
from tkinter import *

window = Tk()
window.geometry("500x500") #size
window.title("shawns first GUI program") - title

#icon = PhotoImage(file="photo.png") - inserts photo by title
#window.iconphoto(True, icon) 

window.config(background="#5cfcff")
window.mainloop() #place window on screen
'''''''''

#labels
'''''''''
import smtplib
sender = "shawnmartin1231@gmail.com"
receiver = "idmybiz@gmail.com"
password = "xiqb wdve btve zamw"
subject = "poop"
body = "cunt"

message = f"""From: Shmeep{sender}
To: meep {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

Try:
    server.login(sender, password)
    print("logged in...")
    server.sendmail(sender,receiver,message)
    print("sent")

except smtplib.SMTPAuthenticatorError:
    print("unable to sign in")
'''''''''

#pip
'''''''''
pip3 list

pip3 list --outdated

pip3 instal xxx --upgrade

pip3 install xxx
'''''''''


# phase 2 ready?

#1
'''
inp = input('reverse you answer: ')
reversed = inp[::-1]
print(reversed)

user_input = input('enter your name: ')
reversed_name = user_input[::-1]
print(reversed_name)
'''

#2
'''
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_in_word = 0
word = input("enter a word you would like to count how many vowels are in it: ")
for i in word:
    if i in list(vowels):
        vowel_in_word += 1t
print('Your word has {} vowels'.format(vowel_in_word))
'''

#3
'''
fizz = range(1, 51)
for i in fizz:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print('Neither Fizz nor Buzz')
    print(i)
'''

#4
'''
user_nums = input("enter 5 numbers using a space to seperate each: ").split()
sorted_nums = sorted(user_nums, key=int)
print('the largest number is {}'.format(sorted_nums[-1]))
'''

#5
'''
n = int(input('enter a number: '))
n_list = []
for i in range(1, n + 1):
    if i % 2 == 0:
        n_list.append(i)
print(sum(n_list))
'''

#6
'''
def calculate_area(width, height):
    area = int(width) * int(height)
    return area

user_width = input("enter the width: ")
user_height = input("enter the height: ")

print(calculate_area(user_width, user_height))
'''

#7
'''
class Dog:
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def bark(self):
        print('{} says woof!'.format(self.name))

dog1 = Dog('chico', 8)
dog2 = Dog('oscar', 10)

dog1.bark()
dog2.bark()
'''

#8
'''
user_input = input('Enter a number: ')

while True:
    user_input = input('Enter a number: ')
    try:
        int(user_input)
        break
    except ValueError:
        print('please enter a number')
'''

#9
'''
user_dict = {}

name1 = input("Enter name for 1st person: ")
name2 = input("Enter name for 2nd person: ")
name3 = input("Enter name for 3rd person: ")
score1 = int(input("Enter score for {} : ".format(name1)))
score2 = int(input("Enter score for {} : ".format(name2)))
score3 = int(input("Enter score for {} : ".format(name3)))

user_dict[name1] = score1
user_dict[name2] = score2
user_dict[name3] = score3

highest_score = max(user_dict, key=user_dict.get)
print(highest_score)
'''

#10
#Functions + Lists
'''
def remove_duplicates(x):
    return list(set(x))

my_list = ['shawn', 'savvy', 'shmeep', 'meep', 'shawn']
print(remove_duplicates(my_list))
'''
'''
class BankAccount:
   def __init__(self):
       self.balance = 0
   def deposit(self):
        self.balance += int(input("How much would you like to deposit:? "))
        print(self.balance)
   def withdraw(self):
        self.balance -= int(input('How much would you like to take out?: '))
        print(self.balance)


account = BankAccount()
account.withdraw()
account.deposit()
'''
'''
class Student:
    grade = []
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average(self):
        return sum(self.grades) / len(self.grades)
student1 = Student('Shawn',[100, 30, 45, 60])
print('your average grade is {}'.format(student1.average()))
'''

'''
import math

class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def area(self, radius):
        return math.pi * radius ** 2

class Rectangle(Shape):
    def area(self, height, length):
        return length * height

shape1 = Circle('red')
shape2 = Rectangle('blue')

print(shape1.area(5))
print(shape2.area(20, 30))
'''

'''
user_numerator = (input('enter a numerator: '))
user_denominator = (input('enter a denominator: '))

try:
    dividend = int(user_numerator) / int(user_denominator)
    print(dividend)
except ValueError:
    print('you must answer a number')
except ZeroDivisionError:
    print('you cannot divide by zero')
'''

'''












































