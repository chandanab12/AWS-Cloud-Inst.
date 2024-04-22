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

Loops are instructions that repeat for as lomg as a condition is met. Python has for loops and while loops. 

- for loops

  For loops iterate over a sequence of items, such as a list or a string and perform an action on each element in the sequence.

- range() function - used to generate a sequence of numbers for a for loop. Range does not include the end number.

- while Loops
  A while loop is a control flow statement that allows you to execute code repeatedly while a specified condition is True.

- break statement
  It is a control flow statement you use to immediately stop running a for or while loop statement. 
  
