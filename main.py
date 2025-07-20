from importlib.metadata import files
from sys import modules

name = "Maciej :)"
age = 23
birthday = 2002
year = birthday + age
print(name, age, birthday, year)

#------------------------------------------------

name = "james"
full_name = "J Juan"  #For two words variable we use underscore or camel case
PI = 3.14
print(name, full_name, PI)

#------------------------------------------------

brand: str = "Moja nazwa firmy"
isAdult: bool = True

def hello() -> str:
    return "Hello"

"""
Tak 
się robi
commenty wieloliniowe
"""

#------------------------------------------------

brand: str = "Moja nazwa firmy"
print(brand.upper())
print(brand.replace("Moja nazwa firmy", "Nie ma nazwy "))
print(len(brand))
print(brand == "Moja nazwa firemki")
print(brand != "Moja nazwa firemki")
print("nazwa" in brand)

#------------------------------------------------

comment = "sdadasdadad"\
            "adsadsadasdad"\
            "adsdasdadasd"
print(comment)

commentLineByLine = """
sdasdadas
dasd
as
dasd
"""
print(commentLineByLine)

name = "Maciej"
email = f"""
Hello {name},
will you be a python dev?
Maybes
"""
print(email)
# print(email.format(name))   Output: Hello Maciej


#------------------------------------------------

#indentation
name = "Maciej"
    # surname = "Juan"   it causes error indent

def myFunction():
    isWorking = True
    surname = "Juan"

#This is not in function because of indent shift+tab
age=23


#------------------------------------------------

print(1 + 2)
print(2 * 2)
print(9 % 2)
print(10 / 2)
print(2 ** 5)

#------------------------------------------------

print(10 > 5)
print(10 < 5)
print(10 >= 5)
print(10 <= 5)
print(10 == 5)

#------------------------------------------------

#Logical operators
print((10 != 5)
      and (1 > 3)
      and "A" == "c")   #First and second expression needs to be true

print((10 != 5)
      or (1 > 3)
      or "A" == "c")

#------------------------------------------------

#if else

number = 1
if number > 0:
    print(f"Number {number} is positive")
elif number == 0:
    print(f"Number {number} is zero")
else:
    print(f"Number {number} is negative")

#------------------------------------------------
#Ternary operators
number = 1
checkingIfNumberIsPositive = "positive" if number > 0 else "0 or negative"
print(checkingIfNumberIsPositive)


#------------------------------------------------
#Lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers.sort())
print(numbers.reverse())
print(numbers.append(2))
print(len(numbers))
print(numbers.clear())
print(5 in numbers)  #If statement
# print(numbers.remove(1))
# print(numbers.pop())
# del numbers[1] #delete index 1 from list
# del numbers[1 : 3] #delete from index 1 to index 3 without third from list

#------------------------------------------------
# Sets

numberList = [1, 1]
numberSet = {1, 1}   #no duplicates, random order
print(f"Number list is : {numberList}")
print(f"Number set is : {numberSet}")

lettersA = {"A", "B", "C", "D", "E", "F", "G", "H", "I"}
lettersB = {"J","K"}
union = lettersA | lettersB
print(union) # union puts two sets into one, combines them
intersection = lettersA & lettersB # gives the same things in both sets
print(intersection)

difference = lettersA - lettersB # everything in lettersA but not in lettersB
print(difference)


#------------------------------------------------
#Dictionaries

person = {
    "name" : "Jamal",
    "age" : 23,
    "address": "Poland"
}

print(person["name"])  #looking by key, they must be unique

person.keys()
person.values()
person.items()

#------------------------------------------------
# Loops

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

for key in person:
    print(f"{key} : {person[key]}")

#------------------------------------------------
# Exercise

numbers = [1, 3, 5, 6, 7, 9]
summerize = 0
for number in numbers:
    summerize += number
print(summerize)

#------------------------------------------------
#While loops

number = 2

# while number < 8:
#     print(number)
#     number += 1
# else:
#     print("End of list")

while number < 8:
    if number % 2 == 0:
        print(number)
        number += 1
    else:
        break

#------------------------------------------------
# Functions

def greeting():
    print("Hello")

greeting()

def func(name, age = 0):
    print(f"Hello, {name}. You are {age} years old.")
    if age < 1:
        print("I don't know your age.")

func(name="Jamal", age=23)
func(name="Maciej")

def age_checker(your_age):
    return your_age >= 18
result = age_checker(35)
print(result)

#------------------------------------------------
# creating modules

# from calculator import add
import calculator

calculator.add(1, 2)
calculator.subtract(1, 2)
calculator.divide(1, 2)
calculator.multiply(1, 2)


#------------------------------------------------
# Classes

class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

    def __str__(self) -> str:
        return f"{self.brand} \n Price =  {self.price}"

iphone = Phone("Iphone", 1400)
samsung = Phone("Samsung", 1500)

print(iphone.brand)
print(iphone.price)
iphone.call("123123123")
print(samsung)

#------------------------------------------------
# Dates

import datetime

print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().day)


now = datetime.datetime.now()

now.strftime("%d/%m/%Y %H:%M:%S")

print(now) #Printing formated date


#------------------------------------------------
# Working with files

file = open("./data.csv", "r+") # r+ means reading/writing
file.write("id, name, email\n")
file.write("1, Juan, email@test.com\n")

print(file.read()) #read the entire file

for line in file:
    print(line)

print(file.readlines())

file.close()

#good way to work with files. We dont need to open and cloes file, it does it
import os.path

filename = "./data.csv"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.readlines())
else:
    print("File not found")

# with open("./data.csv", "r+") as file:
#     print(file.readlines())


#------------------------------------------------
# Fetching data API calls

from urllib import request
import json

r = request.urlopen("http://www.official-joke-api.appspot.com/random_ten")
data = r.read()
jsonData = json.loads(data)
# print(jsonData)

class Joke:
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"{self.setup} {self.punchline}\n"

jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

# print(jokes)













