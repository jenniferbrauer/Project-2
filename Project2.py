import turtle
import math

# Function to draw a rectangle
def draw_rectangle(t, color, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw grass
def draw_grass(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("darkseagreen")
    t.begin_fill()
    t.goto(x + 10, y)
    t.goto(x + 5, y + 30)
    t.goto(x, y)
    t.end_fill()

# Function to draw swirly clouds
def draw_swirly_clouds(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.pensize(40)
    t.color(color)
    for size in range(5, 30, 2):
        t.forward(size)
        t.right(40)

# Function to draw a circle
def draw_circle(turt, x, y, radius, color):
    turt.penup()
    turt.goto(x, y - radius)
    turt.pendown()
    turt.color(color)
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()

# Sine waves
def draw_sine_wave(curve, x_offset, y_offset):
    curve.penup()
    curve.goto(-750, -100 + y_offset)
    curve.pendown()
    for x in range(-750, 750):
        y = math.sin(math.radians(x))
        curve.goto(x + x_offset, y * 20 - 100 + y_offset)

waves = turtle.Turtle()
waves.shape('blank')
waves.color('lightsteelblue')
waves.pensize(80)
waves.speed(0)

x_offset = 0
y_offset = 0

# Turtle descriptions
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.setup(width=1.0, height=1.0)

fill_turtle = turtle.Turtle()
fill_turtle.speed(0)
fill_turtle.hideturtle()

pen_turtle = turtle.Turtle()
pen_turtle.speed(0)
pen_turtle.shape("blank")

cloud_positions = [
    (-300, 250), (-350, 400), (450, 350), (300, 150), (200, 400), (260, 400),
    (-200, 375), (-400, 400), (-500, 175), (-550, 185), (550, 175), (600, 175)
]

sun_turtle = turtle.Turtle()
sun_turtle.speed(0)
sun_turtle.shape("blank")

ocean_turtle = turtle.Turtle()
ocean_turtle.speed(0)
ocean_turtle.color("lightblue")
ocean_turtle.hideturtle()

grass_turtle = turtle.Turtle()
grass_turtle.speed(-500)
grass_turtle.hideturtle()

draw_circle(sun_turtle, 0, 150, 500, "paleturquoise")
draw_circle(sun_turtle, 0, 150, 400, "thistle")
draw_circle(sun_turtle, 0, 150, 300, "coral")
draw_circle(sun_turtle, 0, 150, 200, "lightsalmon")
draw_circle(sun_turtle, 0, 150, 90, "lemonchiffon")

draw_sine_wave(waves, 0, 0)

draw_rectangle(fill_turtle, "lightsteelblue", -screen.window_width() / 2, -500, screen.window_width(), 400)
draw_rectangle(fill_turtle, "darkseagreen", -screen.window_width() / 2, -500, screen.window_width(), 300)

for i in range(-700, 700, 20):
    draw_grass(grass_turtle, i, -200)

for x, y in cloud_positions:
    draw_swirly_clouds(pen_turtle, x, y, 0, "aliceblue")

screen.exitonclick()
