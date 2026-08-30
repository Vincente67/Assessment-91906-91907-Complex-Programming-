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

# Screen used to display program 
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

# Displays the controls for the user 
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
# Coordinate Display
# -------------------------------------------------------------------

# Turtle used to display coordinates 
coordinate_writer = turtle.Turtle()
coordinate_writer.hideturtle()
coordinate_writer.penup()

def show_coordinates():
    """Displays coordinates underneath the shape."""

    coordinate_writer.clear()
    coordinate_writer.goto(-430, -300)

# Displays the saved coordinates 
    coordinate_writer.write(
        "Coordinates: " + " ".join(str(point) for point in points),
        font=("Arial", 11, "normal")
    )

    
# -------------------------------------------------------------------
# DRAW FUNCTION
# -------------------------------------------------------------------

# Redraws the shape using stored coordinates 
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

# Adds the mouse position to the list 
def add_point(x, y):
    """Adds the position of the mouse click to the points list."""

    global shape_finished

    # Do not allow points after finishing the shape
    if shape_finished:
        return

    # Store the mouse position as a coordinate tuple
    points.append((round(x), round(y)))

    # Draw the updated shape
    redraw_shape()

    # Update the coordinates shown on screen
    show_coordinates()

    print("Point added:", (round(x), round(y)))


# -------------------------------------------------------------------
# FINISH SHAPE
# -------------------------------------------------------------------

# Finishes the shape by connecting to the first point 
def finish_shape():    
    """
    Finishes the shape by connecting the last point 
    back to the first point.
    """

    global shape_finished

# Checks that there are enough points 
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

# Removes the last point from the list 
def undo_point():
    """Removes the last point."""

    global shape_finished

    if points:
        shape_finished = False
        points.pop()
        redraw_shape()
        show_coordinates()
    else:
        print("No points to undo.")

# -------------------------------------------------------------------
# CLEAR
# -------------------------------------------------------------------

# Clears the current shape 
def clear_shape():
    """Clears the drawing and coordinates."""

    global shape_finished

    points.clear()
    shape_finished = False

    pen.clear()
    pen.penup()

    coordinate_writer.clear()

# -------------------------------------------------------------------
# SAVE COORDINATES
# -------------------------------------------------------------------

# Save the coordinates to a text file 
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

# Creates a Python file for the shape 
def generate_python_code():
    """Create Python Turtle code for the shape."""

    if len(points) < 3:
        print("Create a shape first.")
        return

    with open("custom_shape.py", "w") as file:
        file.write(
            "import turtle\n"
            "screen = turtle.Screen()\n"
            "shape = turtle.Shape('compound')\n"
            "points = (\n"
        )

        # Writes each coordinate into the Python file 
        for point in points:
            file.write(f"    {point},\n")

        file.write(
            ")\n"
            "shape.addcomponent(points, 'blue', 'black')\n"
            "screen.register_shape('custom_shape', shape)\n"
            "t = turtle.Turtle()\n"
            "t.shape('custom_shape')\n"
            "turtle.done()\n"
        )

    print("Python code saved!")

# -------------------------------------------------------------------
# CONTROLS 
# -------------------------------------------------------------------

# Allows mouse click to add points
screen.onclick(add_point)

# Allows keyboard controls 
screen.listen()

screen.onkeypress(finish_shape, "Return")
screen.onkeypress(undo_point, "u")
screen.onkeypress(clear_shape, "c")
screen.onkeypress(save_coordinates, "s")
screen.onkeypress(generate_python_code, "g")
screen.onkeypress(screen.bye, "q")

# -------------------------------------------------------------------
# START 
# -------------------------------------------------------------------

print("Enter = Finish | U = Undo | C = Clear")
print("S = Save Coordinates | G = Generate Code")

# Keeps the Turtle window open
turtle.done()
