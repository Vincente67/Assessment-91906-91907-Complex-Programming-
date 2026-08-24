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

    if len(points) == 0:
        return

    # Move to the first point
    pen.goto(points[0])
    pen.pendown()

    # Draw lines between each point
    for point in points[1:]:
        pen.goto(point)

    pen.penup()

# -------------------------------------------------------------------
# ADD POINT
# -------------------------------------------------------------------

def add_point(x, y):
    """
    Adds the position of the mouse click to the points list.
    """

    global shape_finished
    
    # Do not allow new points after finishing the shape
    if shape_finished:
        return

    # Store the mouse position as a coordinate tuple
    points.append((round(x), round(y)))

    # Draw the updated shape 
    redraw_shape()

    print("Point added:", (round(x), round(y)))


# -------------------------------------------------------------------
# FINISH SHAPE
# -------------------------------------------------------------------

def finish_shape():
    """
    Finishes the shape by connecting the last point 
    back to the first point.
    """

    global shape_finished
    
    if len(points) < 3:
        print("You need at least 3 points.")
        return

    shape_finished = True

    pen.penup()
    pen.goto(points[0])
    pen.pendown()

    # Connect the final point back to the first point 
    pen.goto(points[0])
    pen.penup()

    print("Shape finished.")
    print("Coordinates:")
    print(points)

# -------------------------------------------------------------------
# UNDO
# -------------------------------------------------------------------

def undo_point(): 
    """Remove the last point."""

    global shape_finished 

    if points:
        shape_finished = False
        points.pop()
        redraw_shape()
    else:
        print("No points to undo")


# -------------------------------------------------------------------
# CLEAR
# -------------------------------------------------------------------

def clear_shape():
    """Clear the drawing and coordinates"""

    global shape_finished 

    points.clear()
    shape_finished = False
    pen.clear()
    pen.penup()

# -------------------------------------------------------------------
# SAVE COORDINATES
# -------------------------------------------------------------------

def save_coordinates():
    """Saves the coordinates to a text file."""

    if len(points) < 3:
        print("Create a shape first.")
        return

    with open("coordinates.txt", "w") as file:
        file.write("Turtle Shape Coordinates\n")
        file.write(str(points))

    print("Coordinates saved!")

# -------------------------------------------------------------------
# GENERATE PYTHON CODE
# -------------------------------------------------------------------

