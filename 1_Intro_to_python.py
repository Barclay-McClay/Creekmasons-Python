# This is a Python script 'filename.py'
# Read through it like normal. Then run it through your computer as code at the end.
# Once done, you can experiment with going back and altering the code to see how it changes the output.
# Within all this are the foundations you'll need for programming in Python, master it, and you've got a solid intro on:
    # Variable declaration
    # If statements
    # Basic syntax and codeblock indentation
    # Simple recursion with a 'while loop'
    # 'integer' and 'string' data types
    # defining and calling functions

print("As you read through, see if you can guess what each line of code (like this one here) will 'do'")
print("I'll give you a hint here: 'print()' will print anything inside the brackets to the terminal.")

# In Python, 'comments' are marked by a '#' character.
# Anything written after a '#' will be 'commented out', and not executed as code.
# This is handy for leaving quick notes for yourself or others within the code, to explain what stuff is for/how it works, etc.

"""
For a multi-line comment (a paragraph or so of info), you can use triple quotes before and after the text like this.
This way you don't need a '#' at the start of each line.

When I was learning to code; one thing that really helped me to keep in mind was this:
Your computer is going to start at the top of this page, and then read it one line at a time, top to bottom, really really really fast (potentially thousands of times a second).
So we can imagine the computer's 'attention' progressing through the code, like a human's eyes would move through a book, start -> finish.
We establish information, and then build upon it. Just like a regular narrative.
"""
# Now, a really simple script:
x = 1  # Here we define a variable 'x' as '1'
y = 2  # Same as above, but 'y' is '2'

if x + y == 3:
    # Anything here will happen if x + y is equal to 3
    print("Hello World")
    print("This demonstrates variable declaration, 'if' statements, and code-block indentation.")
else:
    # Anything here will happen if x + y is not equal to 3
    print("It didn't work.")

"""
Some things to take note of:
x = 1
With ONE equal '=', we make whatever is on the left into whatever is on the right. So 'x = 1' means, "When I say 'x', it can now be understood as '1'"
if x + y == 3:
Here we are using TWO equals '=='. We *compare* whatever is on the left into whatever is on the right. 'x + y == 3' means "Does 'x + y' evaluate to a three '3'?"

The "if" is telling the computer "Only do these things 'IF' they meet the following condition..." then the colon ':' marks the end of the condition.

Notice the next line down is indented a bit? In Python, code blocks are organised by indentation. I don't know the formal way this is taught, but think of it like:

This code will happen
This code will happen
if <primary condition>:
    This will happen if primary is true
    if <secondary condition>:
        This will happen if both primary and secondary are true
        This will happen if both primary and secondary are true
        This will happen if both primary and secondary are true
        if <third condition>:
            This will happen if primary, secondary and third is true
        else:
            This will happen if primary and secondary are true, but third is FALSE
    else:
        This will happen if primary is true, but secondary is FALSE
    This will happen if primary is true, *after* all the above has happened.
else:
    This will happen if primary is FALSE
This will happen after everything above

Notice how the different amounts of indentation organise the code into 'blocks'? 
This will become more apparent the more code statements you learn, and its not imperative you understand it straight away-
just be aware of it, and know that the indentation *matters* in Python.
"""

print("Now that we've glossed over the basics- let's demonstrate some other really simple functions")

# This will print the numbers 1-10
count = 0
while count < 10:
    # Whatever is here in this code-block will happen, and *keep happening* while 'count' is less than 10
    print(count)
    count += 1  # This is the same as count = count + 1, we are increasing the value of 'count' by 1.

print("Now we have a variable called 'count', with the value of "+str(count))

"""
In programming, you must be mindful of different datatypes.
Here, we combine a 'string' (words enclosed in quotation marks) with an integer (the value of 'count')
the 'str( )' function converts whatever into a string (or into 'writing'), so that it can be used for text (rather than math/computation/etc)

ie. A computer does not know the context of "1", 1 and 'one'.
As far as it understands,
1 is a number that holds a mathematical value.
"1" is just like any other symbol or 'string'; "a", "!", "3", "elephant"- it does not get any meaning from it.

Or think of it like this,

1 + 1 == 2

"1" + "1" == "11"

1 + "1" == TypeError: unsupported operation for '+', you are mixing an integer and a string.

cat = 1
dog = 1
cat + dog == 2

cat = "cat"
dog = "dog"
cat + dog == "catdog"

1 + "1" throws an error for the same reason you cant add 34 and "banana" together for a valid mathematical result. They are different types of information.
"""

# As your code gets more complex, you'll be defining 'functions'.

def add(foo, bar):      # We are defining 'add', a function which will take values 'foo' and 'bar'
    teapot = foo + bar  # Within 'add' (notice we are indented now), we are defining a new variable, 'teapot' as the sum of 'foo' and 'bar'
    return teapot       # 'add' will now 'return' whatever is stored in the variable 'teapot'.
#Simply defining a function does not run it. It just lets the computer know 'this is what I want you to do when I say 'add(55,14)'

# Lets use the new 'add()' function
poop = add(600,66) # makes poop = 666
print(poop) # We expect to see 666

# Lets use the function to condense the amount of code we have to write:
print(str(add(351,69)) + " blaze it!" ) # 420 blaze it!

"""
You've probably noticed I've used strange variable names, 'teapot' or 'poop', etc.
This is just to demonstrate that you can use whatever you want. They aren't special keywords.
There is common convention, but this differs between languages, company policy, and personal preference.

poop = 10
r = 10
flekwhjfg = 10
ten = 10
twenty = 10

All of these will evaluate to 10
Remember, we tell the computer we mean *text* when we enclose it in quote marks "" and make it a 'string'.
If it isn't in quote marks, it'll be evaluated as code.
"""
# Ok, now that we're at the end- let's execute this python script.
# We expect it to output the following in the terminal:
"""
As you read through, see if you can guess what each line of code (like this one here) will 'do'
I'll give you a hint here: 'print()' will print anything inside the brackets to the terminal.
Hello World
This demonstrates variable declaration, 'if' statements, and code-block indentation.        
Now that we've glossed over the basics- let's demonstrate some other really simple functions
0
1
2
3
4
5
6
7
8
9
Now we have a variable called 'count', with the value of 10
666
420 blaze it!
"""

# Enjoy
