"""ENTERING INPUT

name = input("Enter name: ")
fav_color = input("Enter Fav color:  ")

print(name + " likes " + fav_color)
"""

"""TYPE CONVERSION e.g for age
birth_year= input('enter birth year: ') 
age = 2024 - int(birth_year)
print(age)
"""

"""TYPE CONVERSION e.g for pounds to kg
weight_pounds= float(input("enter weight in pounds: "))
weight_kg= weight_pounds * 0.453592 
print(weight_kg )
"""

"""STRING MANIPULATION

fact1= "God is good"
fact2= 'previous is "God is good"'
fact3='''
    God
    is
    good
'''

course= "Python for beginners"
#for first character
print(course[0])
#for last character
print(course[-1])
#for first to third character 
#counting starts from 0
print(course[0:3])
#for first character to last
print(course[0:])
print(course[:])
#creates copy of course
course_copy= course[:]
"""

"""Formatted String
first= "ugo"
last= "agwuna"
msg= f'{first} [{last}] is a coder'
print(msg)


#string length
print(len(course))
#uppercase this will not chage original variable 
print(course.upper())
#To find index of character (note: it's case sensitive) e.g find B in varialble course
print(course.find("P"))
#To find index of sequence of character 
print(course.find("Python"))
#To print every first letter in capital 
print(course.title())
#To replace
print(course.replace("beginners", "Absolute beginners"))
#To check if something is in a string(note; this will return a boolean  value. it's a boolean expression)
print('Python' in course)   
"""

"""ARITHMETIC OPERATIONS
#adding
print(10 + 3)
#subtracting
print(10 - 3)
#multiplying
print(10 * 3)
#diving
print(10 / 3)
#diving to get intenger
print(10 // 5)
#to get the remainder of the division 
print(10 % 3)
#exponentiation or to the power
print(10 ** 3)

#incrementing a number (note: same principle for decrementing)
x = 10
x = x + 3
# same thing with augmented assingment operator 
x += 3
print(x)

#operator precedence
order='''
    p
    (x)

#operator precedence
orderarenthesis
    exponentiation 2**3
    multiplication or division
    additon or subtraction 
    so x= 10 + 3 * 2 will be 16 and not 26
'''

"""

"""IF STATEMENTS

is_hot= False
is_cold= False

if is_hot: 
    print("it's a hot day")
elif is_cold:
    print("it's not a cold day")
else:
    print("enjoy your day")

house_price= 1000000
good_credit= True

if good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
print(f"Down_Payment: ${down_payment}")
"""

"""LOGICAL OPRERATORS

has_high_income= True
has_good_credit= False
has_criminal_record = False

#"and" operator for both conditions
if has_high_income and has_good_credit:
    print("Eligible for loan")
#"or" operator for either conditions 
if has_high_income or has_good_credit:
    print("Eligible for loan")
#"not" inverses any boolean value it's given
if has_high_income and not has_criminal_record:
    print("Eligible for loan")
"""

"""COMPAIRISON OPERATORS
tempreture = 30

#greater than oposite would be less than "<"
if tempreture > 30:
    print("it's a hot day")
else:
    print("it's not a hot day")
#greater than or equals to oposite would be less than or equals to "<="
if tempreture >= 30:
    print("it's a hot day")
else:
    print("it's not a hot day")
#"==" makes it to be a boolean value as oposed to "=" which just sets it
if tempreture == 30:
    print("it's a hot day")
else:
    print("it's not a hot day")
#"!=" mean not equals to
if tempreture != 30:
    print("it's not a hot day")
else:
    print("it's a hot day")
"""

"""COMPAIRISON OPERATORS e.g.for name length
name = input("enter name: ")
name_length= len(name)

if name_length >= 3 and name_length <=50:
    print("name looks good")
else:
    print("name must be 3 - 50 characters long")
"""

"""WEIGHT CONVERSION e.g. non case sensitive input
weight= input("enter your weight: ")
mass= input("Enter (L)bs or (K)gs: ")

if(mass.upper() == "L"):
    print("You are", float(weight) * 0.453592, "kg")
elif(mass.upper() == "K"):
    print("You are", float(weight) * 2.20462, "pounds")
"""

"""WHILE LOOPS
i = 1
while i <= 5:
    print("*" * i)
    i = 1 + i
print("Done")
"""

"""WHILE LOOPS e.g guessing game 
## user should have 3 chances to guess a secret number. if they get the number correctly
#let them know they got it correctly. if 

secret_number= 5
guess_count= 0
guess_limit= 3
#while loop will run until the conditon becomes false
while guess_count < guess_limit:
        guess= int(input("guess:"))
        #this will increment guess by 1
        guess_count+=1
        #if statement will check if the user guessed correctly
        if guess == secret_number:
                print("You won")
                #break ends the while loop 
                break
#if the while loop condtion becomes false the else statement will run
else:
        print("sorry, you failed")
"""

"""WHILE LOOPS e.g car game"""

''' Game description
when the code is run the user will see '>'
they then have to type "help" while to a menu being provided
"start" to start car
"stop" to stop car
"quit" to quit game 
any other input should tell the user "i dont understand that..." and 
give them a chance to make a new entry

Start: "Car started...ready to go"
stop: "Car stopped" 
quit: program ends
'''

'''
update:
if the car is stopped and the user enters stop again tell them the car is already stopped
if the car is started and the user enters start again tell them it's already started 



    
print("CAR GAME")

choice = ""
started = False
 
while True:
    choice= input(">").upper()
    if choice == "START":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car is started..")
    elif choice == "STOP":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif choice == "HELP":
        print("""
            start - to start car
            stop - to stop car
            quit - to quit game 
            """)       
    elif choice == "QUIT":
        break
    else:
        print("Sorry, I dont understand  that...")

        
'''

"""FOR LOOPS
#using lists[] 
for names in ["chis", "ugo", "agwuna"]:
    print(names)

#using range and inputs with formatted string
any_num= int(input("enter number: "))
#for number in range(1, 13):
  #  print(f"{any_num} *{number}= {any_num * number}")

#using range with steps(note: will skip every 2 number)
for num in range(1, 10, 2):
    print(num)
"""

"""FOR LOOPS e.g. total in list[]
use a for loop to calculate total cost of items in a shopping cart
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f"Total: {int(total)}")
"""

"""NESTED LOOPS
#x, y coordinates example
for x in range (3):
    for y in range (4):
        print(f"({x}, {y})")
"""

"""NESTED LOOP e.g print "L" made of x

#list will create L shape
numbers= [1, 1, 1, 1, 5]
#this will store the value in number on each interation
for x_count in numbers:
    #this
    output = ""
    #count will store the range of x_count on each itteration
    for count in range(x_count):
        output += 'x'
    print(output)
"""

"""LISTS
names= ["ugo", "chris", "agwuna"]
#prints all values in list
print(names)
#chages value at that index in list
names[0]= "ugochukwu" 
print(names)
"""

"""LISTS e.g finding largest number
numbers= [1, 3, 4, 6, 3, 2, 9, 5]
#assuming the first number in the list is the smallest
max = numbers[0]
#number is bascally a copy of numbers when used
#in this context
for number in numbers:
    if number > max:
        max = number
print(max)
"""

"""2D LISTS
#this a list thats made up of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#to access a specific item in the list 
matrix[0][1]

#to change that specific item
matrix[0][1]= 20
"""

"""LIST METHODS
number = [1, 5, 2, 8, 5, 9]
#to add new value a the end of the list
number.append(20)
#to add new value at a specic point in the list
#fist number is the index point it will take 
#second point is the value
number.insert(2, 10)
#to remove an item e.g 5
number.remove(10)
#to remove the last item in the list
number.pop()
#to return the number of duplicates e.g 5
number.count(5)
#to sort the list in ascending order
number.sort()
#to sort the list in decending order
number.reverse()
#to get copy of list that would be altered by changes
number2 =number.copy()
#to empty the list
number.clear()
"""

"""LIST e.g to remove deplicates in a list style 1
numbers = [1, 4, 5, 7, 4, 23, 44, 5, 2, 8, 5, 9, 5]
#number4 =numbers.copy()
for num9 in numbers:
    if numbers.count(num9) > 1:
        numbers.remove(num9) in numbers
print(numbers)
"""

"""LIST e.g to remove deplicates in a list style 2
numbers = [1, 4, 5, 7, 4, 23, 44, 5, 2, 8, 5, 9, 5]
unique = []
for unique in numbers:
    if numbers not in unique:
        unique.append(numbers)
print(unique)
"""
    
"""PROGRAM TO MAKE AND EDIT LIST e.g. with enumerate
to_do_list = []
count = 0

while True:
    print('''USER MENU
          1- Enter a task
          2- View tasks
          3- Mark task as compleated
          4- Close program
          ''')
    option = input("Enter your choice: ")
    if option == "1": 
        tasks = input("Enter a task: ")
        to_do_list.append(tasks)
      
    elif option == "2":
        print("Your to do list: ")
        for count, tasks in enumerate(to_do_list):
            count+=1
            print(f"{count}: {tasks}")

    elif option == "3":
        complete = int(input("What task is compleated: "))
        actual = complete - 1
        print(actual)
        to_do_list.pop(actual)
 
    elif option == "4":
        break
    else:
        print("please select an option on the menu")
"""

"""TUPLES 
#values in tuples can not be changed
coordindates = (1, 2, 3)
x = coordindates[0]
y = coordindates[1]
z = coordindates[2]

#same as
x, y, z = coordindates
"""

"""DICTIONARIES
coder = {
    "name": "UgoChris",
    "language": "Python",
    "age": 24,
    "favoured": True
}
#to display entire dictionary 
print(coder)
#to get a value in the dictionary
coder.get("name")
#to update a value on dictionary
coder["name"] = "Ugochukwu"
"""

"""DICTIONARIES e.g. Phone number to words

phone = input("Number: ")
digits_mapping = {
    "0": "Zero",
    "1": "0ne",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = " "
#this will loop through phone and store each value in ch
for ch in phone:
    #this will get the value for ch that stored in phone
    # this will also add each value in the strong output 
    output+= digits_mapping.get(ch, "!") + " "
print(output)
"""

"""DICTIONARIES e.g. converting ":)" to "😀" 

message = input (">")
#this will act a boundary to spererate strings into multiple words
#then it will return a list 
words = message.split(' ')
emoji = {
    ":)":  "😀",
    ":(": "☹️"
}
#where the final statement will be built
output = ""
for word in words:
    #will get an item with the key word and if it not there 
    #it will use the word already ther 
    output+= emoji.get(word, word) + " "
    print(output)
"""

"""FUNCTIONS
#defining a function
def greet_user():
    print("hey user")
    print("Welcome!")

print("Start")
greet_user()
print("Finish")

#passing parameters through functions
def user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

#positional arguements being passed
#positon matters for accuracy
user("Ugochukwu", "Agwuna")

#key word arguments. Position doesnt matter 
#function will be respected
#these are best for functions that take in numerical values
user(last_name="Agwuna", first_name="Ugochukwu")

#when mixing, positonal arguments should come before key word



#this function calculates square of a number
#return allow me return values to the caller of my function
    #without "return" python will return "none" by default 
def square(num):
    return num * num

result= square(3)
print(result)
#for shoter code is applicable
print(square(3))
"""

"""FUCNTION e.g. with emoji converter
def emoji_converter(message):

    words = message.split(' ')
    emoji = {
        ":)":  "😀",
        ":(": "☹️"
    }
    output = ""
    for word in words:
        output+= emoji.get(word, word) + " "
    return output

message = input(">")
print(emoji_converter(message))
"""

"""EXCEPTIONS
try:
    age  = int(input("Enter age: "))
    print(age)
    income = 125000
    risk  = income / age
    print|(age)
except ZeroDivisionError:
    print("age cannot be 0")
except ValueError:
    print("Invalid Value")
"""

"""CLASSES"""
#classes are the blueprint or template for creating objects
class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

#objects are an instance of a class
#creating object
point1 = Point()
point1.x= 10
print(point1.x)
point1.draw()






    






