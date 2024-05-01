# Python 

## History


Python is an interpreted, object-oriented programming language that is widely used in web applications, software development, data science, and machine learning (ML). 


- Guido Van Russom (1991) created Python.

- Some advantages include Readability, Productivity, Reusability, and Community. Interoperability, Portability

- Use Cases: Can be used for server-side web development, automation, data science and ML, S/W test automation

## IDE

- An IDE is an integrated development environment because it provides a central environment for common developer tools, making s/w development process more efficient.
  
- The default IDE for Python is IDLE(Integrated Development and Learning Environment).
  
-  Python operates in two modes: script and interactive. Script involves adding code into a script that Python can run. Interactive is a convenient way to run code and see the results in real-time.

- Example of interactive mode ![image](https://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/dd3878d6-d5a9-4a7f-a7a8-1f168faf6100)


-  IDE's help with compiling, testing, and debugging. System integration and collaboration. Syntax highlighting and correction.

## AWS Cloud9

AWS Cloud9 is a cloud-based IDE that supports several programming languages and runtime debuggers and has a built-in terminal. It can be accessed through a browser and configured based on your preferences. 

## Syntax 

Syntax refers to the rules that define the structure of a language. 

An indentation consists of the spaces at the beginning of a code line. 

## Variables 

A variable is a container for storing data values. 

Using variables makes your code flexible and reusable. 

Some rules to be followed while declaring a variable:

- They can have letters, digits, and underscores.

- They cannot have whitespace and symbols such as +, -, !, @,$,#,%

- They must start with a letter or the underscore character.

- They cannot start with a number

- They cannot be a Python keyword.

## Operators

Operators are used to operate on variables and values. 

- Arithmetic operators include addition (+), subtraction (-), multiplication (*), modulus (%), exponentiation (**), division (/), and floor division ( // ).

- Comparison operators include equal (==), not equal (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).

- Assignment operators are special symbols that combine the assignment operator (=) with another operator, such as addition (+) or subtraction (-).

- Logical operators include and, or, and not. Used to combine conditional statements.

- Bitwise operators include AND (&), OR (|), NOT (~), zero fill left shift (<<), signed right shift (>>), and Exclusive OR, also known as XOR (^). used when working with low- level programming languages.

- Membership operators include in and not in. used to test whether a value is a member of a sequence or collection.

- Identity operators include is and is not. used if values are of same data type and share the same memory location.

Operators Precedence in Python follows the PEMDAS rule 

P - Parentheses

E - Exponentiation

M - Multiplication and D - Division 

A- Addition and S - Subtraction 


## Data Types

https://docs.python.org/3/library/stdtypes.html#string-methods


Strings, Integer, Float, list, tuple, dict, set, frozenset, bool, bytes, bytearray, NoneType

- Use the + operator to concatenate strings

- f-strings are used to include variables in your strings.
  example- print(f'Hello, {name}. You are {age}.')

  Working with strings

  Indexing - a method to access individual elements in a sequence. Python assigns each element an index number starting from 0 to the first element.

  Slicing - to reference a specific element
  
starting index(included) and ending index (excluded) 

  to return a range of characters specify the start and end indexes.
  print (mystring[2:5])

  print (mystring[:5]) - prints everything from 0 -5

  print (mystring[2:]) - prints everything from 2 to the end


- upper() - makes everything upper case

- lower() - makes everything lower case

- strip() - removes any extra white space      - "Hello, World " & "Hello, World" are both diff and it changes it to second one

- replace() - replace a string with another string

- format() - allows you to format strings by replacing the placeholder '{}' with the values you want to insert. 

![image](https://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/9b632545-ef60-4feb-8f71-18a010a04055)


- Escape characters - used to represent special characters. Use a backlash to represent (\)

- \n - newline, \t inserts a tab space in a string, \\ inserts a backlash, \' inserts a single quote, \xhh hexadecimal represents a character using its hexadecimal value.

- input() - allows you to pause your program and prompt a user to enter text.

- ![image](httop[pps://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/d31b752a-6a8e-4d69-8bec-35539fbdd221)

- int() function - changes a string to an integer number.

## Conditionals

- If statements

  if condition:
    #do something

- elif - can test multiple conditions with different actions. 

![image](https://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/231c5b66-1a33-409d-b02b-6724ee667d3e)

- else - use it to address anything that does not match the preceding conditions. 
![image](https://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/ebeb88e7-a66f-4872-b9cd-6c60c2209793)

## Loops 

Loops are instructions that repeat for as long as a condition is met. Python has for loops and while loops. 

- for loops

  For loops iterate over a sequence of items, such as a list or a string and perform an action on each element in the sequence.

- range() function - used to generate a sequence of numbers for a for loop. Range does not include the end number.

- while Loops
  A while loop is a control flow statement that allows you to execute code repeatedly while a specified condition is True.

- break statement
  It is a control flow statement you use to immediately stop running a for or while loop statement. 
  
## Data Structures 

Data structures provide an organized way to store data. 

Python has built-in non-primitive data structures that can help store and access a collection of data. They are lists, sets, tuples and dictionaries. 

### Iterables 

An iterable is a collection of elements that you can loop. or iterate, through one at a time.

- Ordered - if the elements are stored and retrieved in a predictable sequence.
- Mutable - if you can change the elements it holds.

## List 

A list is an ordered, mutable collection of elements that might include duplicate values. 

It is defined by square brackets. [ ]  It can accessed by position. 

## Sets

A set is an unordered, mutable collection of unique elements. { }

Since it is unordered, you cannot access elements by position. 

## Tuple 

A tuple is an ordered, unmutable collection of elements that can store duplicate values. (   )

Can access elements based on position. 

## Dictionary 

A dict is an ordered, mutable collection of key-value pairs that cannot store duplicate keys. 

----------------------------------------------------------------------------------------------

## Python Lists ------ check List.py for practice 

Lista are used to store a wide variety of elements in a single variable. Are mutable, can hold data of any type, and can hold repeat values. Each element in a list is called an item. 

List can have zero elements 

Ex: scores = [ ]

- len() function
The length function returns the number of elements in a list.

- Lists follow indexing so items in a list are positioned from 0
Accessing something from a list can be done by indexing

![image](https://github.com/chandanab12/AWS-Cloud-Inst./assets/54497878/cabd6b2c-0116-47bc-9b67-dfff5059ab38)


You can access a range of elements by specifying, in brackets, where to start and end. 
It is called slicing. list[1:3] or list[-1:-3]

** The first number is included in the output but the second/last is always excluded.

## List methods

Adding list elements

- Append() - adds an element to the end of the list
- insert() - adds an element to the position specified
- extend() - adds a list of elements to an existing list
- "+" adds a list of elements kind off like concatenation
- pop() - removes elements from a list. If no index is specified the last element is popped. 
- remove() - you must identify the item to remove. Be it specifying its value or its index position.
- clear() - just clears everything from the list.

Copying lists 

- copy() - used to create a copy of a list so that you can modify one while maintaining the original.
- using slicing [:] - copied_list = original_list[:]

Changes made to one list do not affect the other. 

- assignment operator '=' - you can copy a list by assigning a new variable to the existing list.

List constructor - by using a list constructor function we can convert a sequence to a list. 
Ex: new_list = list((1, 2, 3))  # converts a tuple to a list

- sort() - method lists them in ascending order/ alphabetical order - numbers > Capital letters> alphabetical order based on ASCII standards. 
- reverse() - lists elements in descending order/ reverse alphabetical order.
- count() - to find the number of times an item appears on a list
- in and not in - give out true or false based on your statement

---------------------------------------------------------------------------------------------

## Python Sets ------- check set.py for practice 
Sets are unordered collections of unique elements. Can be used to drop duplicate values and to find common elements across data sets. 

Sets are declared using curly braces { } 

example: farm_animals = {"dog", "cat", "hen", "duck", "Sheep", "cow"}

cannot use indexing since they are unordered. 

can use set constructor to convert a list to a set and eliminate duplicates 

Example: new_set = set(my_list)

## Set methods 

some similar methods like 
- copy()
- clear()
- in - membership operator - determines if an element belongs to a set - o/p - T/F
- not in - membership operator - determines if an element is not in the set - o/p - T/F

## Boolean Set methods 

- isdisjoint() - returns true if indicated sets have no elements in common.
- issubset() - returns true if the first set contains all elements of the second set.

- 
