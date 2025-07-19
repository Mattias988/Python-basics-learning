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











