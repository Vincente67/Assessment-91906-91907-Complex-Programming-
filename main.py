# -------------------------------------------------------------------
# Turtle Shape Designer 
# AS91906 / AS91907
# 
# This program allows Year 10 students to draw their own 
# Turtle shapes using mouse clicks.
#
# Complex techniques used:
# 1. Graphical User Interface (GUI)
# 2. Writing data to files 
#
# Additional techniques 
# - Turtle non-core library` 
# - List of coordinate tuples 
# -------------------------------------------------------------------

import turtle 


# -------------------------------------------------------------------
# Setup
# -------------------------------------------------------------------

screen = turtle.Screen()
screen.title("Turtle Shape desinger")
screen.setup(width = 900, height=700)
screen.bgcolor("white")


# Turtle used to draw the shape
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.color("blue")
pen.penup()


# Turtle used to display instructions 
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-430, 300)

writer.write(
    "TURTLE SHAPE DESIGNER",
    font=("Arial", 18, "bold")
)

writer.goto(-430, 265)
writer.write(
    "Left Click = Add Point",
    font=("Arial", 12, "normal")
)

writer.goto(-430, 240)
writer.write(
    "Enter = Finish Shape",
    font=("Arial", 12, "normal")
)

writer.goto(-430, 215)
writer.write(
    "U = Undo Last Point",
    font=("Arial", 12, "normal")
)

writer.goto(-430, 190)
writer.write(
    "C = Clear Shape",
    font=("Arial", 12, "normal")
)

writer.goto(-430, 165)
writer.write(
    "S = Save Coordinates",
    font=("Arial", 12, "normal")
)

writer.goto(-430, 140)
writer.write(
    "G = Generate Python Code",
    font=("Arial", 12, "normal")
)

writer.goto(-430, 115)
writer.write(
    "Q = Quit",
    font=("Arial", 12, "normal")
)

# -------------------------------------------------------------------
# DATA STORAGE
# -------------------------------------------------------------------

# Stores every coordinate clicked by the user.
# Each coordinate is stored as a tuple.
points = []


# Keeps track of whether the shape has been completed.
shape_finished = False

# -------------------------------------------------------------------
# DRAW FUNCTION
# -------------------------------------------------------------------

def redraw_shape():
    """
    Redraws the current shape using coordinates 
    stored in the points list.
    """

    pen.clear()
    pen.penup()
