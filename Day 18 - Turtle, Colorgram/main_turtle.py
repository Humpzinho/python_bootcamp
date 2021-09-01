from turtle import Turtle, Screen, width
import random

t = Turtle()

screen = Screen()
screen.colormode(255)
t.hideturtle()

screen.tracer(False)

screen.setup (1100, 1100)

width = int(screen.textinput("Tamanho do(s) circulo(s).", "Qual será o tamanho do(s) circulo(s)?" ))
count = int(screen.textinput("Quantidade de circulos.", "Quantos circulos terá?" ))

def random_color():
    global colours
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255) 
    colours = (r, g, b)
    return colours

def draw():
    t.color(random_color())
    t.circle(width)
    t.right(360 / count)
    screen.update()

draw()

for a in range(count):
    draw()
    print(t.heading()); print(colours)

print("Concluido.")
screen.exitonclick()