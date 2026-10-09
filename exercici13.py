'''
Please write a function named box_of_hashes, which prints out a rectangle of hash characters. 
The function takes one argument, which specifies the height of the rectangle. The rectangle 
should be ten characters wide.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change 
anything in your line function.

Some examples of how the function should work:
box_of_hashes(5)
print()
box_of_hashes(2)

Sample output:
##########
##########
##########
##########
##########

##########
##########
'''


def line(number, text):
    if text == "":
        text = "*"

    print(text * number)

def box_of_hashes(height):
    numlines = height

    while numlines > 0:
        line(10, "#")
        numlines -= 1

#box_of_hashes(5)
#box_of_hashes(2)



'''
Please write a function named square_of_hashes, which draws a square of hash characters. 
The function takes one argument, which determines the length of the side of the square.
The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change 
anything in the line function.

Some examples:
square_of_hashes(5)
print()
square_of_hashes(3)

Sample output:
#####
#####
#####
#####
#####

###
###
###
'''


def square_of_hashes(height):
    numlines = height

    while numlines > 0:
        line(height, "#")
        numlines -= 1



#square_of_hashes(5)


'''
Please write a function named square, which prints out a square of characters, and takes two arguments. 
The first parameter specifies the length of the side of the square. The second parameter specifies 
the character used to draw the square.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything 
in the line function.

Some examples:
square(5, "*")
print()
square(3, "o")

Sample output:
*****
*****
*****
*****
*****

ooo
ooo
ooo
'''

def square(size, character):
    numlines = size

    while numlines > 0:
        line(size, character)
        numlines -= 1

# square(5, "*")
# square(3, "o")


'''
Please write a function named triangle, which draws a triangle of hashes, and takes one argument. 
The triangle should be as tall and as wide as the value of the argument.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything 
in the line function.

Some examples:
triangle(6)
print()
triangle(3)

Sample output:
#
##
###
####
#####
######

#
##
###
'''

def triangle(height, character = ""):
    numlines = height
    count = 0

    if character == "":
        character = "#"

    while numlines >= 0:
        line(count, character)
        numlines -= 1
        count +=1

#triangle(6)


'''
Please write a function named shape, which takes four arguments. The first two parameters specify 
a triangle, as above, and the character used to draw it. The first parameter also specifies the 
width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies 
the filler character of the rectangle. The function prints first the triangle, and then the rectangle 
below it.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything 
in the line function.

Some examples:
shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")

Sample output:
X
XX
XXX
XXXX
XXXXX
*****
*****
*****

o
oo
++
++
++
++

.
..
...


'''

def shape(height_triangle, character_triangle, width_square, character_square):
    triangle(height_triangle, character_triangle)
    square(width_square, character_square)

#shape(5, "X", 3, "*")
shape(3, ".", 0, ",")