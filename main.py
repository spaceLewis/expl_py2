# examples of Python 2.7 codes to migrate to Python >= 3

"""
This script contains a collection of Python programs and examples, primarily written for educational purposes. 
The programs demonstrate various Python concepts, including input/output, arithmetic operations, control structures, 
functions, loops, file handling, lists, strings, and recursion.
Key Features:
- Basic input/output operations using `raw_input` (Python 2.7) and `print` statements.
- Arithmetic operations and type conversions.
- Control structures: `if`, `elif`, `else`, and nested conditions.
- Looping constructs: `while` and `for` loops, including nested loops.
- Examples of using `break` and `continue` in loops.
- Functions: defining, calling, and importing functions from external modules.
- File handling: reading from and writing to files.
- Working with lists: indexing, slicing, appending, and list methods.
- String operations: concatenation, slicing, formatting, and escape sequences.
- Recursive functions and sorting algorithms (e.g., bubble sort).
- Demonstration of Boolean expressions and De Morgan's Laws.
Python 2.7 vs Python >= 3 Differences:
- `raw_input` is used for input in Python 2.7, while `input` is used in Python >= 3.
- Print statements in Python 2.7 use `print` without parentheses, whereas Python >= 3 requires parentheses (e.g., `print("Hello World!")`).
- The `<>` operator for inequality in Python 2.7 is replaced with `!=` in Python >= 3.
- Integer division in Python 2.7 truncates the result by default, while Python >= 3 requires `//` for floor division.
- Unicode strings in Python 2.7 are prefixed with `u` (e.g., `u"string"`), while all strings in Python >= 3 are Unicode by default.
Note:
- The examples in this script are written in Python 2.7 syntax. To run them in Python >= 3, modifications are required to align with the updated syntax and features.
"""

# Last updated: Sunday 22nd February 2009, 16:36 PT 

#01-01.py

print "Hello World!"

#01-02.py

thetext = raw_input("Enter some text ")
print "This is what you entered:"
print thetext

#01-03.py

# Note that \n within quote marks forces a new line to be printed
thetext = raw_input("Enter some text\n")
print "This is what you entered:"
print thetext

#01-04.py

prompt  = "Enter a some text "
thetext = raw_input(prompt)
print "This is what you entered:"
print thetext

#02-01.py

total = 0.0
number1=float(raw_input("Enter the first number: "))
total = total + number1
number2=float(raw_input("Enter the second number: "))
total = total + number2
number3=float(raw_input("Enter the third number: "))
total = total + number3
average = total / 3
print "The average is " + str(average)

#02-02.py

number1=float(raw_input("Enter the first number: "))
number2=float(raw_input("Enter the second number: "))
number3=float(raw_input("Enter the third number: "))
total = number1 + number2 + number3
average = total / 3
print "The average is " + str(average)

#02-03.py

total = 0.0
count = 0
while count < 3:
    number=float(raw_input("Enter a number: "))
    count = count + 1
    total = total + number
average = total / 3
print "The average is " + str(average)

#03-01.py

sum = 10

#03-02.py

sum = 10
print sum

#03-03.py

sum = 10
print sum
print type (sum)


#03-04.py

print 2 + 4
print 6 - 4
print 6 * 3
print 6 / 3
print 6 % 3
print 6 // 3 # floor division: always truncates fractional remainders
print -5
print 3**2   # three to the power of 2

#03-05.py

print 2.0 + 4.0
print 6.0 - 4.0
print 6.0 * 3.0
print 6.0 / 3.0
print 6.0 % 3.0
print 6.0 // 3.0 # floor division: always truncates fractional remainders
print -5.0
print 3.0**2.0   # three to the power of 2

#03-06.py

# mixing data types in expressions
# mixed type expressions are "converted up"
# converted up means to take the data type with the greater storage
# float has greater storage (8 bytes) than a regular int (4 bytes)
print 2 + 4.0
print 6 - 4.0
print 6 * 3.0
print 6 / 3.0
print 6 % 3.0
print 6 // 3.0 # floor division: always truncates fractional remainders
print -5.0
print 3**2.0   # three to the power of 2

#03-07.py

# these are Boolean expressions which result in a value of
# true or false
# Note that Python stores true as integer 1, and false as integer 0
# but outputs 'true' or 'false' from print statements
print 7 > 10
print 4 < 16
print 4 == 4
print 4 <= 4
print 4 >= 4
print 4 != 4
print 4 <> 4

#03-08.py

# these are string objects
print "Hello out there"
print 'Hello'
print "Where's the spam?"
print 'x'

#03-09.py

# these are string assignments
a = "Hello out there"
print a
b = 'Hello'
print b
c = "Where's the spam?"
print c
d = 'x'
print d

#03-10.py

a = 'Hello out there'
b = "Where's the spam?"
c = a + b
print c

#03-11.py

a = 'Hello out there'
b = "Where's the spam?"
c = a + b
print c
#d = c + 10
# you cannot concatenate a string and an integer
# you must convert the integer to a string first:
d = c + str(10)
print d

#03-12.py

a = "10"
b = '99'
c = a + b
print c
print type(c)
c = int(c)
print c
print type(c)

# 03-13.py
# How to round up a floating point number
# to the nearest integer

x = 1.6
print x
x = round(x)
print x
x = int(x)
print x

#  04-01.py 
#  Purpose:    Creating a string object
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 12:43 PT

number1 = raw_input("Enter first number:\n")
print number1, type(number1)

#  04-02.py 
#  Purpose:    Converting one data type to another
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 12:46 PT

number1 = raw_input("Enter first number:\n")
print number1, type(number1)
number1 = int(number1)
print number1, type(number1)

#  04-03.py 
#  Purpose:    Displaying an object's memory location 
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 12:48 PT

number1 = raw_input("Enter first number:\n")
print number1, type(number1), id(number1)
number1 = int(number1)
print number1, type(number1), id(number1)

#  04-04.py 
#  Purpose:    Examples of use of arithmetic operators
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:09 PT

print 2 + 4
print 6 - 4
print 6 * 3
print 6 / 3
print 6 % 3
print 6 // 3 # floor (integer) division: always truncates fractional remainders
print -5
print 3**2   # three to the power of 2

#  04-05.py 
#  Purpose:    Examples of use of arithmetic operators with float values
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:10 PT

print 2.0 + 4.0
print 6.0 - 4.0
print 6.0 * 3.0
print 6.0 / 3.0
print 6.0 % 3.0
print 6.0 // 3.0 # floor (integer) division: always truncates fractional remainders
print -5.0
print 3.0**2.0   # three to the power of 2

#  04-06.py 
#  Purpose:    Examples of use of arithmetic operators 
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:10 PT
# mixing data types in expressions
# mixed type expressions are "converted up"
# converted up means to take the data type with the greater storage
# float has greater storage (8 bytes) than a regular int (4 bytes)

print 2 + 4.0
print 6 - 4.0
print 6 * 3.0
print 6 / 3.0
print 6 % 3.0
print 6 // 3.0 # floor division: always truncates fractional remainders
print -5.0
print 3**2.0   # three to the power of 2

#  04-07.py 
#  Purpose:    Examples of use of Boolean expressions
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:12 PT
#  these are Boolean expressions which result in a value of
#  true or false
#  Note that Python stores true as integer 1, and false as integer 0
#  but outputs 'true' or 'false' from print statements
#  If you input Boolean values, you must input 1 or 0.

print 7 > 10
print 4 < 16
print 4 == 4
print 4 <= 4
print 4 >= 4
print 4 != 4
print 4 <> 4

#  04-08.py 
#  Purpose:    Displaying boolean values
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 12:54 PT

number = 10
isPositive = (number > 0)
print isPositive

#  04-09.py 
#  Purpose:    Combining boolean expressions with and
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:18 PT

age = 25
salary = 55000
print (age > 21) and (salary > 50000)

#  04-10.py 
#  Purpose:    The if statement
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:23 PT
#  The condition of the following if statement
#  follows the word if, and ends with a colon (:)
#  In this example, if x has a value equal to 'spam',
#  then 'Hi spam' will be printed.

x = 'spam'
if x == 'spam':
    print 'Hi spam'
else:
    print 'not spam'

# Notice the indentation (spacing out) of this code.
# The statement(s) following the if condition (i.e. boolean expression)
# must be indented to the next tab stop. This means you must press
# the Tab button before typing the word print.
# Try removing the tab spaces and see what happens when you attempt to run.


#  04-11.py 
#  Purpose:    The if statement with multiple statements
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:23 PT
#  The condition of the following if statement
#  follows the word if, and ends with a colon (:)
#  In this example, if x has a value equal to 'spam',
#  then 'Hi spam\n' will be printed followed by
#  "Nice weather we're having"
#  followed by 'Have a nice day!'

x = 'spam'
if x == 'spam':
    print 'Hi spam\n'
    print "Nice weather we're having"
    print 'Have a nice day!'
else:
    print 'not spam'

#  04-12.py 
#  Purpose:    The if statement with multiple statements
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 27th September 2004, 13:23 PT
#  The condition of the following if statement
#  follows the word if, and ends with a colon (:)
#  In this example, if x has a value equal to 'spammy',
#  then 'Hi spam\n' will be printed followed by
#  "Nice weather we're having"
#  followed by 'Have a nice day!'

x = 'spam'
if x == 'spammy':
    print 'Hi spam\n'
    print "Nice weather we're having"
    print 'Have a nice day!'
else:
    print 'not spam'
    print 'Not having a good day?'

#  Program:    04-13.py
#  Purpose:    A nested if example (an if statement within another if statement)
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 4th October 2004, 13:21 PT

score = raw_input("Enter score: ")
score = int(score)
if score >= 80:
    grade = 'A'
else:
    if score >= 70:
        grade = 'B'
    else:
	grade = 'C'
print "\n\nGrade is: " + grade

#  Program:    04-14.py
#  Purpose:    A nested if example - using if/else
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 4th October 2004, 13:25 PT

score = raw_input("Enter score: ")
score = int(score)
if score >= 80:
    grade = 'A'
else:
    if score >= 70:
        grade = 'B'
    else:
        if score >= 55:
            grade = 'C'
        else:
            if score >= 50:
                grade = 'Pass'
            else:
                 grade = 'Fail'
print "\n\nGrade is: " + grade

#  Program:    04-15.py
#  Purpose:    A nested if example - using if/elif/else
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 4th October 2004, 13:28 PT

score = raw_input("Enter score: ")
score = int(score)
if score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 55:
    grade = 'C'
elif score >= 50:
    grade = 'Pass'
else:
    grade = 'Fail'
print "\n\nGrade is: " + grade

#  04-16.py
#  Purpose:    Demo of DeMorgan's Laws:
#  1.  a Not And is equivalent to an Or with two negated inputs
#  2.  a Not Or is equivalent to an And with two negated inputs
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 21st March 2005, 05:53 PT
#  Test data: 0 0, 0 1, 1 0, 1 1
#  For ***any*** value of x and y, (not(x < 15 and y >= 3)) == (x >= 15 or y < 3)
#  Common uses of De Morgan's rules are in digital circuit design
#  where it is used to manipulate the types of logic gates.
#  Also, computer programmers use them to change a complicated statement
#  like IF ... AND (... OR ...) THEN ... into its opposite (and shorter) equivalent.
#  http://en.wikipedia.org/wiki/De_Morgan%27s_law
#  http://www.coquitlamcollege.com/adawson/DeMorgansLaws.htm

x = int(raw_input("Enter a value for x: "))
y = int(raw_input("Enter a value for y: "))
print (not(x < 15 and y >= 3))
print (x >= 15 or y < 3)

#  Program:    04-17.py
#  Purpose:    Decision using two conditions linked with an and or an or
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 20th February 2007, 11:20 PT

age = raw_input("Enter your age: ")
age = int(age)
have_own_car = raw_input("Do you own your own car (y/n): ")

if (age > 21) and (have_own_car == 'y'):
    print "You are over 21 years old and own your own car"
    
if (age > 21) and (have_own_car == 'n'):
    print "You are over 21 years old and you do NOT own your own car"

if (age == 21) and (have_own_car == 'y'):
    print "You are 21 years old and you own your own car"

if (age == 21) and (have_own_car == 'n'):
    print "You are 21 years old and you DO NOT own your own car"    

if (age < 21) and (have_own_car == 'y'):
    print "You are younger than 21 and you own your own car"

if (age < 21) and (have_own_car == 'n'):
    print "You are younger than 21 and you DO NOT own your own car"    


salary = float(raw_input("Enter your annual salary, (e.g. 50000): "))

if (salary > 50000) or (age > 21):
    print "you can join our club because you earn more than $50000 OR you are over 21 (or both)"
else:
    print "you need to be earning more than 50000 OR be over 21 (or both) to join our club"
    
#  05-01.py 
#  Purpose:    Examples of while loops
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 30th September 2004, 15:51 PT
#  You must remember to indent the statements to be repeated.
#  They must be repeated to the same level.
#  Use the Tab key to indent. The space bar can be used but
#  its easier (less typing) to use the space bar
#  Used like this, the while loop is said to be
#  'counter-controlled'. In this program, x is acting as a counter.

x = 1
while x < 5:
    print 'Hi spam'
    x = x + 1
print 'done'

#  05-02.py 
#  Purpose:    Examples of while loops
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 30th September 2004, 15:51 PT
#  Used like this, the while loop is said to be
#  'counter-controlled'. In this program, x is acting as a counter.
#  You may repeat one statement or multiple statements.

x = 1
while x < 5:
    print 'Hi spam'
    x = x + 1
    print 'I love spam'
print 'done'
print 'gone'

#  05-03.py 
#  Purpose:    Examples of while loops - the infinite loop
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 30th September 2004, 15:51 PT
#  An infinite loop.
#  Remember that 1 (or any value other than 0) represents true.
#  Press Ctrl-C to interupt this program run.

x = 1
while x:
    print 'Hi spam'
    x = x + 1
    print 'I love spam'
    print 'Press the Ctrl key and the C key together'
    print 'to interupt this program...'
print 'done'
print 'gone'

#  05-04.py 
#  Purpose:    Examples of while loops - another infinite loop
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 30th September 2004, 16:00 PT
#  An infinite loop.
#  Remember that 1 (or any value other than 0) represents true.
#  Press Ctrl-C to interupt this program run.


while 1:
    print 'Anyone for spam? '
    print 'Press the Ctrl key and the C key together'
    print 'to interrupt this program...'
print 'done'
print 'gone'

#  05-05.py 
#  Purpose:    Example: use of break to end an infinite loop
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 30th September 2004, 16:02 PT

while 1:
    print 'Spam'
    answer = raw_input('Press y to end this loop')
    if answer == 'y':
        print 'Fries with that?'
        break
print 'Have a '
print 'nice day!'

#  05-06.py 
#  Purpose:    Example: use of continue in a loop
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 30th September 2004, 16:07 PT

while 1:
    print 'Spam'
    answer = raw_input('Press y for large fries ')
    if answer == 'y':
        print 'Large fries with spam, mmmm, yummy '
        continue
    answer = raw_input('Had enough yet? ')
    if answer == 'y':
        break
print 'Have a '
print 'nice day!'

#  05-07.py 
#  Purpose:    Example: 'sentinel-controlled' while loop
#              Calculates average score of a class
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 5th October 2004, 6:31 PT

# initialization phase
totalScore = 0     # sum of scores
numberScores = 0   # number of scores entered

# processing phase
score = raw_input( "Enter score, (Enter -9 to end): " )   # get one score
score = int( score )   # convert string to an integer

while score != -9: # -9 is used as a sentinel ( a lookout or sentry value )
    totalScore = totalScore + score
    numberScores = numberScores + 1
    score = raw_input( "Enter score, (Enter -9 to end): " )  
    score = int( score )
   
# termination phase
if numberScores != 0: # division by zero would be a run-time error
   average = float( totalScore ) / numberScores
   print "Class average is", average
else:
   print "No scores were entered"

#  05-08.py 
#  Purpose:    Example: the counter-controlled for loop
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 5th October 2004, 6:53 PT

for c in range (10):  
    print c

# Note: range (10) is 0 through 9

#  05-09.py 
#  Purpose:    Example: the counter-controlled for loop
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 5th October 2004, 6:58 PT

for c in range (5,10):  
    print c

# Note: range (5,10) is 5 through 9
#  05-10.py 
#  Purpose:    Example: 'continue' with the for loop
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 5th October 2004, 6:58 PT

for c in range (1,6):
    if c == 3:
        continue
    print c

#  05-11.py 
#  Purpose:    Example: 'break' with the for loop
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 5th October 2004, 7:05 PT

for c in range (1,6):
    if c == 3:
        break
    print c

#  05-12.py 
#  Purpose:    Example: outputting strings and numbers
#              in a single print statement
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 5th October 2004, 7:21 PT

d = 10
c = 75
print 'Total is: ', d, 'dollars and', c, ' cents'

#  05-13.py 
#  Purpose:    Example: outputting strings and numbers
#              in a single print statement
#              using string formatting.
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 5th October 2004, 7:35 PT

x = 20
y = 75
print 'The sum of %d and %d is %d' % (x, y, x + y)

x = 20.512
y = 15.269
print 'The sum of %f and %f is %f' % (x, y, x + y)
x = 20.512
y = 15.269
print 'The sum of %0.2f and %0.2f is %0.2f' % (x, y, x + y)

#  05-14.py 
#  Purpose:    Example: how to repeat a program at the user's request
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 19th October 2006, 7:58 PT

print "This is the start of the program"
answer = 'y'
while (answer == 'y' or answer == 'Y'):
    print "This is a statement from within the while loop"
    print "This is another statement from within the while loop"
    answer = raw_input("Do you want to run this program again? y/n")
print "Goodbye!"

#  05-15.py 
#  Purpose:    Example: how to use a loop within a loop
#              a nested while loop
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 27th June 2007, 9:08 PT

print "This is the start of the program"

x = 1
while (x < 6):
    print # prints a new line
    print "x = " + str(x), # the , forces printing of the next item
                           # to be on the same line 
    x = x + 1
    y = 1
    while (y < 6):
        print "y = " + str(y), # the , forces printing on the same line
        y = y + 1

'''
Notice that with a loop repeating 5 times,
***within*** a loop that repeats 5 times
means that you can control 25 processes.
'''

#  05-16.py 
#  Purpose:    Example: how to use a loop within a loop
#              a nested while loop
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 27th June 2007, 9:44 PT

print "This is the start of the program"

x = 1
while (x < 6):
    print # prints a new line
    print "x = " + str(x) # the , forces printing of the next item
                           # to be on the same line 
    x = x + 1
    y = 1
    while (y < 6):
        print "y = " + str(y), # the , forces printing on the same line
        y = y + 1
        z = 1
        while (z < 6):
            print "z = " + str(z), # the , forces printing on the same line
            z = z + 1
        print # prints a new line
'''
Notice that with a loop repeating 5 times,
***within*** a loop that repeats 5 times
***within*** a loop that repeats 5 times
means that you can control 125 processes.
'''

#  05-17.py 
#  Purpose:    Example: how to use a loop within a loop
#              a nested for loop
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 27th June 2007, 9:45 PT

print "This is the start of the program"

for i in range (1,6):
    for j in range (1,6):
        print "i: " + str(i) + " j: " + str(j) 
    print        
'''
Notice that with a loop repeating 5 times,
***within*** a loop that repeats 5 times
means that you can control 25 processes.
'''

#  05-18.py 
#  Purpose:    Example: how to use a loop within a loop
#              a nested for loop
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 27th June 2007, 9:45 PT


print "This is the start of the program"

for i in range (1,6):
    for j in range (1,6):
        for k in range (1,6):
            print "i: " + str(i) + " j: " + str(j) + " k: " + str(k)
    print        
'''
Notice that with a loop repeating 5 times,
***within*** a loop that repeats 5 times
***within*** a loop that repeats 5 times
means that you can control 125 processes.
'''

#  06-01.py 
#  Purpose:    Example: using the built-in square root function math.sqrt
#              To use any math function, you have to include the statement:
#              import math
#              in your program - usually at the top, but can be anywhere.
#  Course:     CSCI120A, CSCI165
#  Date:       Friday 6th October 2006, 8:54 PT

import math
print math.sqrt(16)
print math.sqrt(16.5)
x = 144
print math.sqrt(x)

#  06-02.py 
#  Purpose:    Example: using the dir function to list out the names
#              of available functions in the math module
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 11th October 2004, 7:59 PT

import math
print math
print dir(math)

#  06-03.py 
#  Purpose:    Example: using a programmer-defined function
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 11th October 2004, 8:19 PT

# start of function definition
def cube( y ):
    return y * y * y
# end of function definition

# prints the cube of numbers 1 to 5
for x in range(1,6):
    print cube(x)

# the last value of x is 5 
print "last value of x is:",x

#  06-04.py 
#  Purpose:    Example: using two programmer-defined functions
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 11th October 2004, 8:45 PT

def cube( y ):
    return y * y * y

def doubleIt ( z ):
 return 2 * z

print "1 to 5 cubed"
for x in range(1,6):
    print cube(x),
print
print

print "1 to 5 doubled"    
for x in range(1,6):    
    print doubleIt(x),

#  myFunctions.py 
#  Purpose:    two programmer-defined functions
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 11th October 2004, 8:57 PT

def cube( y ):
    return y * y * y

def doubleIt ( z ):
 return 2 * z

#  06-05.py 
#  Purpose:    Example: importing programmer-defined functions
#              from its own module file
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 11th October 2004, 8:56 PT
#  IMPORTANT:  myFunctions.py should be in the same folder as this file

import myFunctions

print "1 to 5 cubed"
for x in range(1,6):
    print myFunctions.cube(x),
print
print

print "1 to 5 doubled"    
for x in range(1,6):    
    print myFunctions.doubleIt(x),
    
#  06-06.py 
#  Purpose:    Example: function with no return statement
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 12th October 2004, 6:30 PT

def times(x):
    for i in range(1,11):
        print "%d x %d = %d" % (i, x, i * x)

print "This is the 1 times tables:"
times(1)

print "This is the 2 times tables:"
times(2)

#  06-07.py 
#  Purpose:    Example: a function with two return statements
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 12th October 2004, 6:37 PT

def division(x,y):
    if (y == 0):
        print "division by zero not allowed"
        return
    else:
        " returning %f divided by %f " % (x, y)
        return x / y

print " 5.0 / 2  returns:"
result = division( 5.0 , 2 )
print result

print " 5.0 / 0  returns:"
result = division( 5.0 , 0 )
print result

#  06-08.py 
#  Purpose:    Example: a function with no arguments
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 12th October 2004, 7:18 PT

def greeting():
    print "Hello out there!"

greeting()
greeting()
greeting()

#  06-09.py 
#  Purpose:    Example: a program with a Boolean function
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 12th October 2004, 7:21 PT

def isPositive(x):
    if (x >= 0):
        return 1 # 1 is true
    else:
        return 0 # 0 is false
    
x = float(raw_input("Enter a positive or negative number: "))
result = isPositive(x)
print result
print isPositive(x)

#  06-10.py 
#  Purpose:    Example: a polymorphic function
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 12th October 2004, 7:34 PT

def doubleIt(x):
    return (2 * x)

y = 3
print doubleIt(y)
z = "Spam "
print doubleIt(z)

# This program works because the * operator can be used with
# numbers and with strings.  This is an example of Polymorphism.

# Poly means "many" and morph means "form"

# Polymorphism : the meaning of the operations depends on the objects
# being operated on. The * operator is said to be "overloaded"

# An overloaded operator behaves differently depending on
# the type of its operands.

#  06-11.py 
#  Purpose:    Demonstrates the use of Python functions
#  Course:     CSCI120A, CSCI165
#  Date:       Sunday 29th October 2006, 12:48 PT                                                               
                                             
'''
    Thanks to HW for the idea behind this program.

    Note that this is a multi-line comment which starts and ends with
    three single quote marks (')
    
    Note that functions can be defined anywhere,
    as long as they're defined before they're called.

    Note the use in this program of a simple pause function,
    to pause a program until a key is pressed.

    Note that when a function is called, all the lines in the
    function definition (def) are executed in order,
    then the program resumes at the point after the function call.

    Note that this program script starts executing at the line:
    startMessage()
    followed by the line:
    clearScreen()
    followed by the line:
    print "Testing this program"
'''

def pause():
    raw_input("\n\nPress any key to continue...\n\n")

def quitMessage():
    print "Thank you for using this program"
    print "Goodbye"
    
def printThreeLines():
    for i in range(1,4):
        print 'this is line ' + str(i)

def printNineLines():
    for i in range(1,4):
        printThreeLines()

def startMessage():
    print "This program demonstrates the use of Python functions"
    pause()
    
def blank_Line():
    print
    
def clearScreen():
    for i in range(1,26):
        blank_Line()
        
startMessage()
clearScreen()
print "Testing this program"
printNineLines()
pause()
clearScreen()
printNineLines()
blank_Line()
printNineLines()
pause()
clearScreen()
quitMessage()

#  07-01.py 
#  Purpose:    Example: creating and using a Python list
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:02 PT

result = [0,0,0,0,0,0,0,0]
print result
result[0]  =  75
result[1]  =  90
result[4]  =  72
print result
print result[0]
print result[1]
print result[2]
print result[3]
print result[4]
print result[5]
print result[6]
print result[7]

#  07-02.py 
#  Purpose:    Example: creating and printing an empty list
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:15 PT

list1 = []
print list1

# the following statement would generate an error
#print list1[0]

#  07-03.py 
#  Purpose:    Example: appending to an empty list
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:17 PT

list1 = []
print list1
list1.append(67)
print list1[0]
list1.append("spam")
print list1
print list1[0]
print list1[1]
# the following statement would generate an out-of-range error
#print list1[2]

#  07-04.py 
#  Purpose:    Example: a list of lists
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:22 PT

list1 = [1,2,3]
print list1
list2 = [4,5,6]
print list2
list3=[list1,list2]
print list3
print list3[0]
print list3[1]

#  07-05.py 
#  Purpose:    Example: accessing the last item in a list
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:27 PT

list1 = [1,2,3,6,7,8,9,10]
print list1
print list1[0]
print list1[1]
print list1[-1]
print list1[-2]

#  07-06.py 
#  Purpose:    Example: deleting items from a list
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:28 PT

list1 = [1,2,3,4,5,6,7,8,9,10]
print list1
del list1[0]
del list1[-1]
print list1

#  07-07.py 
#  Purpose:    Example: repeating lists
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 6:37 PT

list1 = [1,2,3]
print list1
print list1 * 3
print list1
list1 = list1 * 2
print list1

#  07-08.py 
#  Purpose:    Example: concatenating lists
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 6:55 PT

list1 = [1,2,3]
print list1
list2 = [4,5,6]
print list2
list1 = list1 + list2
print list1
list1 = list1 + list1
print list1

#  07-09.py 
#  Purpose:    Example: ist indexing
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:07 PT

list1 = ["Anne", "Dawson", 666]
print list1[0], list1[2]

#  07-10.py 
#  Purpose:    Example: list indexing
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:08 PT

list1 = [2,4,6,8,10,12,14,16,18,20] 
print list1[0:1],list1[5:7]

#  07-11.py 
#  Purpose:    Example: finding the length of a list 
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:20 PT

list1 = ["Anne","was",'here','testing',1,2,3] 
list2 = [1,2,3,4]
list3 = []
print len(list1),
print len(list2),
print len(list3)

#  07-12.py 
#  Purpose:    Example: list iteration
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:26 PT

list = [1,2,3,"Spam",4,5] 
for i in list:
    print i,

#  07-13.py 
#  Purpose:    Example: list membership
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:28 PT

list = [1,2,3,"Spam",4,5] 
print "Spam" in list

#  07-14.py 
#  Purpose:    Example: a selection of list methods
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:42 PT

list = ["B","C","A"]
print list
list.extend(["X","Y"]) # extends the list
print list
list.pop() # removes last item from the list
print list            
list.pop()
print list            
list.reverse() # reverses the order of the items in the list
print list                        
list.append("S")
print list            
list.sort() # sorts the list into ascending order
print list
list.reverse() # reverses the order of the items in the list
print list  

#  07-15.py 
#  Purpose:    Example: a 2D list
#  Course:     CSCI120A
#  Date:       Sunday 4th November 2007, 12:15 PT

tictactoe = [[1,2,3], [4,5,6], [7,8,9]]
print tictactoe[0]
print tictactoe[1]
print tictactoe[2]
print

row = 1
column = 0
print "row " + str(row) + " column " + str(column) + " has value"
print tictactoe[row][column]

row = 2
column = 2
print "row " + str(row) + " column " + str(column) + " has value"
print tictactoe[row][column]

print
print
tictactoe[2][2] = 0
print "After changing the value at row 2 and column 2 to 0: "
print
print tictactoe[0]
print tictactoe[1]
print tictactoe[2]

#  08-01.py 
#  Purpose:    Example: strings
#  Course:     CSCI120A, CSCI165
#  Date:       Saturday 30th October 2004, 16:14 PT

print 'Anne was here'
print "9396633"

# Note that you can print a string over several lines
# if you contain it within triple quotes marks:

print '''Anne was here 
     on Saturday 
     30th October 2004'''

#  08-02.py 
#  Purpose:    Example: using an apostrophe within a string
#              and using double quote marks within a string
#  Course:     CSCI120A, CSCI165
#  Date:       Saturday 30th October 2004, 16:14 PT

print "This is Anne's spam"
print "This is Anne's spam and these are Jake's eggs" 

# You can also print a " within a string enclosed in single quotes:

print 'Here is a double quote ", and "more"'

#  08-03.py 
#  Purpose:    Example: multiplying numbers and
#                       multiplying strings
#  Course:     CSCI120A, CSCI165
#  Date:       Saturday 30th October 2004, 16:38 PT

print 3 * 4
print 30 * 4
print "3" * 4
print "30" * 4

#  08-04.py 
#  Purpose:    Example: string concatenation
#  Course:     CSCI120A, CSCI165
#  Date:       Saturday 30th October 2004, 16:51 PT

print "Anne " + "was " + ("here " * 3)

#  08-05.py 
#  Purpose:    Example: string indexing
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 7:01 PT

s1 = "Anne Dawson" 
print s1[0],s1[5]

#  08-06.py 
#  Purpose:    Example: string slicing
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 7:07 PT

s1 = "Anne Dawson" 
print s1[0:1],s1[5:7]
print s1[6:9]

#  08-07.py 
#  Purpose:    Example: finding the length of a string
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 7:10 PT

s1 = "Anne" 
s2 = "Dawson"
s3 = ""
print len(s1),
print len(s2),
print len(s3)

#  08-08.py 
#  Purpose:    Example: the %s string formatting code
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 8:00 PT

print 'Python is a %s language.' % 'great'

#  08-09.py 
#  Purpose:    Example: finding a string within a string
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 8:11 PT


s1 = 'spamandeggs'
x = s1.find('and')
print x

#  08-10.py 
#  Purpose:    Example: finding a string within a string
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 8:34 PT

s1 = 'spam and eggs'
s1.replace('and','without')
print s1
# the above shows that strings are immutable (cannot change)

s2 = s1.replace('and','without')
print s2

#  08-11.py 
#  Purpose:    Example: escape sequences within a string 
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 2nd November 2004, 8:29 PT

s = 'one\ntwo\tthree'
print s

#  08-12.py 
#  Purpose:    Example: an escape sequence counts as one character
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 2nd November 2004, 8:31 PT

s = 'one\ntwo\tthree'
print s
print len(s)

#  08-13.py 
#  Purpose:    Example: iteration and membership with strings
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 3rd November 2004, 7:35 PT

s = 'Anne was here'
for c in s:
    print c,
print 'w' in s,
print ' ' in s,
print 'x' in s

# 08-14.py
# Anne Dawson
# Sunday 20th March 2005, 04:44 PT
# Demonstration of printing Unicode characters
# For explanation, see:
# http://www.network-theory.co.uk/docs/pytut/tut_17.html
# For character charts go to:
# http://www.unicode.org/charts/
# http://www.unicode.org/charts/PDF/U2580.pdf (Block Elements)
# \u2588 is a Full Block which can be used to build up a black square 
str1 = u'Hello\u2588out there' # solid black block within text
print str1
str1 = u'\u2588\u2588' #two full block characters
print str1
print
print
print "two lines of two full blocks"
print str1
print str1
print
print
# Note: a space is \u0020
print 'two lines of two full blocks, two spaces, two full blocks:'
str1 = u'\u2588\u2588\u2588\u2588\u0020\u0020\u0020\u0020\u2588\u2588\u2588\u2588'
print str1
print str1
print
print
print 'two lines of two full blocks, the number 17 and two full blocks:'
str1 = u'\u2588\u2588\u2588\u2588\u0020\u0020' + '17' + u'\u2588\u2588\u2588\u2588'
print str1
str1 = u'\u2588\u2588\u2588\u2588\u0020\u0020\u0020\u0020\u2588\u2588\u2588\u2588'
print str1

#  09-01.py 
#  Purpose:    Example: a program which uses a file
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 8:37 PT

file1 = open('C:\\temp\\file1.txt','r')
# the line above opens C:\temp\file1.txt for reading
string = file1.readline()
print string

#  09-02.py 
#  Purpose:    Example: a program which uses a file
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 10:38 PT

file1 = open("C:\\temp\\tester2.txt","w")
print file1 # prints out details about the file
file1.write("Today is Monday\n") 
file1.write("Tomorrow is Tuesday")
file1.close()

#  09-03.py 
#  Purpose:    Example: a program which uses a file
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 10:56 PT

file2 = open("C:\\temp\\tester2.txt","r")
print file2 # prints out details about the file
string1 = file2.read()
print string1
file2.close()
file2 = open("C:\\temp\\tester2.txt","r")
string1 = file2.read(5)
print string1
string1 = file2.read(5)
print string1
string1 = file2.read(5)
print string1
file2.close()

#  09-04.py 
#  Purpose:    Example: a program which uses a file
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 11:31 PT

def copyFile(oldFile, newFile): 
  f1 = open(oldFile, "r") 
  f2 = open(newFile, "w") 
  while 1: 
    text = f1.read(50) 
    if text == "": 
      break 
    f2.write(text) 
  f1.close() 
  f2.close() 
  return 

filecopy = "C:\\temp\\tester2copy.txt" #this file will be created
fileold = "C:\\temp\\tester2.txt" # existing file
copyFile(fileold, filecopy)

#  09-05.py 
#  Purpose:    Example: a program which uses a file
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 11:31 PT

filename = raw_input('Enter a file name: ') 
try: 
  f = open (filename, "r") 
except: 
  print 'There is no file named', filename 

#  10-01.py 
#  Purpose:    Example: sequential search of a list
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 11th November 2004, 14:05 PT

list1 = [11,27,36,44,51,22,65,1,78]
numbertofind = int(raw_input("Enter a number\n"))
found = 0
for i in list1:
    if numbertofind == i:
        print numbertofind, " at index: ",list1.index(numbertofind)
        found = 1
if found == 0:
    print "Number not found"

#  10-02.py 
#  Purpose:    Example: sequential search of a list
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 19th November 2008, 11:37 PT

mylist = [10,11,3,4,55,12,23,14,16]
n = len(mylist)
print n
for i in range(n):
    print mylist[i],

search = int(raw_input("\nPlease enter a number to search for: "))
    
print search

found = False
for i in range(n):
    if mylist[i] == search:
        found = True
        index = i
print

if found == True:
    print str(search) + " found at index " + str(index)
else:
    print str(search) + " not found"

#  bubblesort.py 
#  Purpose:    Example: a program which demonstrates a bubble sort on
#              a list of 10 random integers
#  Course:     CSCI120A, CSCI165
#  Date:       Sunday 14th November 2004, 9:17 PT

import random

# define the bubble sort function
def sort(values):
   length = len(values)
   for time in range(0, length-1):
      for position in range(0, (length-time-1)):
         if values[position] > values[position+1]:
            temp = values[position]
            values[position] = values[position+1]
            values[position+1] = temp

# generate a list of ten random numbers
numbers = []
number = 0
while number < 10:
   value = random.randint(1,100)
   if not(value in numbers):
      numbers.append(value)
      number = number + 1

# show unsorted list, sort the list, and show sorted list
print "Before:", numbers
sort(numbers)
print "After :", numbers

#  12-01.py 
#  Purpose:    Example: a recursive function
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 11th November 2004, 14:25 PT

def factorial(n): 
  if n == 0: 
    return 1 
  else: 
    return n * factorial(n-1) 

print " 5! has a value of: ",
result = factorial(5)
print result

print " 4! has a value of:",
result = factorial(4)
print result
