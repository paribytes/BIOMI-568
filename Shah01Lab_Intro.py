#Python Lab 01

"""
NOTE: First thing to do: Rename this file with your last name like this:

Kelley01Lab_Intro_81319.py

Instructions: Read the information and try the examples in the interpreter.
Once you understand the concepts, answer the EXERCISES using variables and
the print statement. (See example answer for EXERCISE 1).

To test your answers, save the file and run it (F5 key) in IDLE.

For this lab, we will ONLY grade the answers for the EXERCISE portions.

"""
print("A. PYTHON AS A CALCULATOR")
#
#There are four different mathematical operators to
#add, subtract, multiply and divide: +, -, *, and /.
#Here are a few examples to try in the interpreter.
#
#>>> 2+2	#addition
#>>> 4*4	#multiplication
#>>> 16/4	#division
#>>> 2-2	#subtraction

#Python has 2 other operation symbols:
#Exponentiation: **
#5 ** 2 == 25
#and
#Remainder: %
#14 % 3 == 2

#
print('EXERCISE 1: Calculations')
#"""
#A1.   Add 17 and 383

x1=17+383
print("x1 = ", x1)

#A2.   Divide 222 by 11

x2=222/11
print("x2 = ", x2)

#A3.   Multiply 20 by 0.5

x3= 20*0.5
print("x3 = ", x3)


print("B. USING PARENTHESES ( ) FOR CALCULATIONS")

#When parentheses are used in calculations, they tell python what to calculate first
#just like in math class. Python works on the calculation in ( ) before it does anything else. 
#
#>>> 5*(3+2) 	#First Python adds 3 and 2, then multiplies this by 5
#25
#>>> (5*3) +2	#First Python multiplies 5 and 3 then adds 2
#17
#
#Try the following:
#
y1 = 5*3+2
print("y1 =", y1)

y2 = 3+2*5
print("y2 =", y2)

#
#Can you see the difference? 
#
print('C. ASSIGNING VALUES TO VARIABLES')
#The equal sign ("=") is used to assign a value to a variable.
#The value of an assignment is not written: 

width = 20
height = 5*9
width * height
#
#EXERCISE
#
#C1. Assign a new variable named area that is equal to width multiplied by height.
#then print the value of area:

area= width*height
print("Area is", area)

print('D. PRINTING')

#Now here is a more complicated program. Save and run the following printing programs
#in a file called YourName.py, where YourName is your first and last name like this: ScottKelley.py

#NOTE: Parts D and E are for PRACTICE ONLY.
#You do not need to turn in this file, only the Lab file.
#
#print("Jack and Jill went up a hill")
#print("to fetch a pail of water;")
#print("Jack fell down, and broke his crown,")
#print("and Jill came tumbling after.")
#
#When you run this program it prints out: 
#
#Jack and Jill went up a hill
#to fetch a pail of water;
#Jack fell down, and broke his crown,
#and Jill came tumbling after.
#
print('E. ORDER OF OPERATIONS')
#
#Expressions 
#
#Here is another program. Add this to the end of the previous Jack and Jill printing program. 
#
#sum_this=2+2
#multiply_that=3*4
#
#print ("2 + 2 is", sum_this)
#print ("3 * 4 is", multiply_that)
#print (100 - 1, " = 100 - 1")
#print ("(33 + 2) / 5 + 11.5 = ",(33 + 2) / 5 + 11.5)
#
#And here is the output when the program is run: 
#
#2 + 2 is 4
#3 * 4 is 12
#99 = 100 - 1
#(33 + 2) / 5 + 11.5 = 18.5
#
print('F. VARIABLES IN PYTHON')
#
#Learning to use variables is one of the most important parts of programming.
#Fortunately, Python makes using variables very easy. In math class, variables
#represent numbers or values and the same can be true in python. They can also
#represent numbers or letters, or even more complex things that we will get to later.
#
#1. Numbers
#
#Variables are like expandable boxes that can hold values of all sizes.
#Begin by setting variables to different number values.
#In Python, variable names are always letters or words that you set equal to something else:
#
x=5 	#Here I set a variable called x equal to the number 5
#>>> x		#Entering x at the prompt, Python tells me x equals 5
#5
x=10	#Here I changed the value of x to 10.
#>>> x
#10
y=200	#Now I made a new variable, y, equal to 200
#
#Once you create variables, you can start to play with them in different ways.
#For instance you can add, multiply, divide or subtract them just like numbers.
#Here are a few examples to try out. Set the variables to the values above.
#See what answers you get:
#
y+x
print("y+x is", y+x)

x*y
print("x*y is", x*y)

x*(x+y)
print("x*(x+y) is", x*(x+y))

x*(y+y)
print("x*(y+y) is", x*(y+y))

z = x+y #You can assign a variable equal to other variables.
print("Y is", y)

#EXERCISES
#F1a. What is x after the following operation?
x=x+1
print("x is", x)
#F1b. And again?
x=x+1
print("x is", x)
#F1c. What about this?
x+=1
print("x is", x)

#But x, y and z are really boring variable names.
#In fact, you can make variable names as long and complicated as you like! 
#
width = 200
jorge_is_terrific = 3000
small_one = 0.000003
BIG_ONE = 40000000000
#
#Names to Avoid:
#Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
#or 'I' (uppercase letter eye) as single character variable names.
#In some fonts, these characters are indistinguishable from the numerals one and zero.
#When tempted to use 'l', use 'L' instead.

#MORE EXERCISES	
#F1d. What happens when you do this? IT GENERATES A NAME ERROR 
#BIG_ONE == big_one
#print(BIG_ONE)

#
#Python does not like spaces in the names, which is why I use the underscore _ character to connect words.  If you put a space in there you will get a SyntaxError like this:
#
#>>> small one = 003
#  File "<string>", line 1
#     small one = 003
#             ^
# SyntaxError: invalid syntax
#
#Python also does not like funny characters like percentage signs (%) and asterisks (*). 
#
#>>> big% = 90
#  File "<string>", line 1
#     big% = 90
#          ^
# SyntaxError: invalid syntax
#>>> big*=90
#  File "<string>", line 1
#     big*=90
#         ^
# SyntaxError: invalid syntax
#
#MORE EXERCISES

#F1d. Set x to a value of 2000. Set y to a value of 0.25. Multiply x and y.
x = 2000
y = 0.25
z=x*y
print("z is", z)

#F1e. Make the variable SPAM equal to x minus y.
SPAM = x-y
print("SPAM is", SPAM)

#F1f. Divide SPAM by x and then add y.
spam = (SPAM/x) + y
print("spam is", spam)
#
#One more thing you should know about variable names is that Python really cares about uppercase
#and lowercase letters in names.
#For instance, the variable names SPAM, spam, Spam, and SpaM are all different variables to Python
#even though they are spelled the same. This is why I like to keep all my variable names in lower
#case letters so I do not get mixed up.
#
#HELPFUL HINT: A value can be assigned to several variables simultaneously: 
#
x = y = z = 0  # Zero x, y and z
print("x,y and z:", x)
#
#2. Strings (Letters and Words)
#
#Python also has many ways to manipulate and play with letters and words. In Python, words are
#called Strings because you can string letters together to form words.
#
#For example, my name is "Scott", but you can also think of this word as a bunch of letter
#strung together:
#			S C O T T
#
#Of course, Scott could also be a very nice name for a variable:
#
Scott = 31
print(Scott)
#31
#
#So we have to distinguish strings from variable names using quotation marks ("").
#
a= "Scott" 	#Here is a string of my name
print(a)

b='does not'
print(b)

c= 'like'
print(c)

d= 'spam'		#And here is a food I dislike
print(d)
#
#Just like with numbers, we can make variables hold strings as values.
#Here are a few examples you can try out at the prompt:
#
name = 'scott'	#Here I set a variable name
print("name is", name)
## equal the string 'scott'

food = 'spam!'
print("food is", food)

emotion = 'hate'
print("emotion is", emotion)

#
print('G. MANIPULATING STRINGS')
#
#1. Concatenation and Multiplication of Strings
#
#In Python, you can concatenate strings with the + operator.
#Concatenation is the process of tying or gluing strings together to make longer strings. 
#
#Here are a few examples to try: 
#
str1= 'CATTACG' + 'AATGC'
str2='CATTACG' + ' ' + 'AATGC'	#Notice the empty ' ' space character
print("str2 is", str2)
str3='CATTACG' + 'AATGC' + ' '
print("str3 is", str3)
#
#You can also concatenate variables together if they hold strings as values:
#
DNA1 = 'AGAGAGAG'
DNA2 = 'GATGGACT'
print("DNA1 + DNA2 is", DNA1 +DNA2)

#
#You can also print out very long strings:
#
long_string = 'Can you help me find the cat?\n I think she ran out of the house!'
print (long_string)

#EXCERCISES
#G1a. Create a new variable called new_DNA that equals the concatenation of DNA1 and DNA2. ?????
new_DNA = DNA1 + DNA2
print(new_DNA)

#G1b. Add the string '\n' to new_DNA and print new_DNA. What happens when you do this? ?????
new_DNA = DNA1+ DNA2
print("new_DNA \nis", new_DNA)
#
#
#By now you have probably noticed that the \n character is an enter character and returns to the
#next line. This is an example of a hidden character you do not see them when you print the string
#out, but they are there anyway. Another hidden character is \t, which is a tab character.
#
#Not only can you concatenate (or add) strings together, you can also multiply (or repeat)
#strings with the * operator. Try a few examples to see what this does:
#
DNA1*2
print("DNA1*2", DNA1*2)

DNA2*7
print("DNA2*7", DNA2*7)

new_DNA*10
print("new_DNA*10",new_DNA*10)
# 
#Strings can be concatenated (glued together) with the + operator, and repeated with *: 
#
word = 'Help' + ' Me'
print(word)
#'Help Me'

word_new= '<' + word*5 + '>'
print("word_new is", word_new)

#'<Help MeHelp MeHelp MeHelp MeHelp Me>'
#
#2. Cool Python Trick #1: SLICING 
#
#MORE EXERCISES

#G2a. Can you figure out what the following code is doing?????
word='HelpMe'
print(word[4])

print(word[0:2])
print(word[2:4])

my_word=word[4:6]
print("my_word is", my_word)

#G2b. What happens if you do word[0:8]
print( word[0:8])

#G2c. What about word[8]
#print(word[8])
#STRING INDEX OUT OF RANGE

#G2d. What about word[:-1]
print(word[:-1])

#G2e. What about word[:-2]
print(word[:-2])
#
#Try out the following string slices:
#
print(word[:2])   # The first two characters
#'He'
print(word[2:])   # All but the first two characters
#'lpA'
#
#NOTE: Strings are immutable. They cannot be changed!
#
#Assigning to an indexed position in the string results in an error: 
#
#>>> word[0] = 'x'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in ?
#TypeError: object doesn't support item assignment
#
#>>> word[:1] = 'Splat'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in ?
#TypeError: object doesn't support slice assignment
#
#However, creating a new string with the combined content is easy and efficient: 
#
str_new= 'x' + word[1:]
print(str_new)
#'xelpA'

str_new2= 'Splat' + word[4]
print(str_new2)
#'SplatA'
#
#Here's a useful invariant of slice operations: s[:i] + s[i:] equals s. 
#
print(word[:2] + word[2:])

#'HelpMe'

print(word[:3] + word[3:])

#'HelpMe'
#
#Degenerate slice indices are handled gracefully: an index that is too large
#is replaced by the string size, an upper bound smaller than the lower bound returns an empty string. 
#
print(word[1:100])
#'elpAMe'

print(word[10:])
#''

print(word[2:1])
#''
#3. Going Backwards
#
#Indices may be negative numbers, to start counting from the right. For example: 
#
print(word[-1])    # The last character
#'A'
print(word[-2])    # The last-but-one character
#'p'
print(word[-2:])    # The last two characters
#'pA'
print(word[:-2])   # All but the last two characters
#'Hel'
#
#But note that -0 is really the same as 0, so it does not count from the right! 
#
print(word[-0])     # (since -0 equals 0)
#'H'
#
#Out-of-range negative slice indices are truncated, but don't try this for single-element
#(non-slice) indices: 
#
print(word[-100:])
#'HelpA'
#>>>>word[-10]   # error
#Traceback (most recent call last):
#  File "<stdin>", line 1, in ?
#IndexError: string index out of range
#
#
#FINAL EXERCISES 
#G3a. Make a new variable Total_DNA that concatenates DNA1 and DNA2 and multiplies them 10 times.
Total_DNA = (DNA1 + DNA2)*10
print(Total_DNA)

#G3b. Make a new variable called Microsat that equals a slice of Total_DNA that includes the first copy of DNA1 (see Cool Python Trick #1: SLICING).
Microsat = Total_DNA[0:8]
print(Microsat)

#G3c. Make a new variable called PrimeEnd equal to a slice of the last 10 bases of Total_DNA.
PrimeEnd = Total_DNA[-10:]
print(PrimeEnd)
#

