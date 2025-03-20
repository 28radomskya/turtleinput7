import turtle
import random

screen = turtle.Screen()
screen.screensize( 500,  500)
t = turtle.Turtle()
screen.bgcolor('black')

# menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write('Background Color', font=("arial",30,"normal"),align='center')

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor("tan")
t.write('1. Tan', font=("arial",20,"normal"),align='left')

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor("azure")
t.write('2. Azure', font=("arial",20,"normal"),align='left')

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor("aquamarine")
t.write('3. AquaMarine', font=("arial",20,"normal"),align='left')

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor("darkkhaki")
t.write('4. DarkKhaki', font=("arial",20,"normal"),align='left')

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor("white")
t.write('Select a Color', font=("arial",30,"normal"),align='center')

choose = int(input('Pick a Color: '))
if choose == 1:
    screen.bgcolor('tan')
elif choose == 2:
    screen.bgcolor('azure')
elif choose == 3:
    screen.bgcolor('aquamarine')
else:
    screen.bgcolor('darkkhaki')

t.clear()

t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("Black")
t.write('Enter Your Name: ', font=("arial",30,"normal"),align='center')

name = input("Enter a name: ")
t.clear()
# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))

operation = random.randint (1,4)
if operation  == 1:
    num1 = random.randint(-10,10)
    num2 = random.randint(-10,10)
    solution = num1 + num2
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor("black")
    t.write('+', font=("arial", 30, "normal"), align='center')
elif operation == 2:
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    solution = num1 - num2
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor("black")
    t.write('-', font=("arial", 30, "normal"), align='center')
elif operation == 3:
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    solution = num1 * num2
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor("black")
    t.write('*', font=("arial", 30, "normal"), align='center')
else:
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    solution = num1 / num2
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.pencolor("black")
    t.write('/', font=("arial", 30, "normal"), align='center')

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("blue")
t.write(name, font=("arial",30,"normal"),align='center')

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("green")
t.write(num1, font=("arial",30,"normal"),align='center')

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("hotpink")
t.write(num2, font=("arial",30,"normal"),align='center')

# t.penup()
# t.goto(-100,0)
# t.pendown()
# t.pencolor("black")
# t.write(operation, font=("arial",30,"normal"),align='center')

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("black")
t.write('=', font=("arial",30,"normal"),align='center')

ans =  float(input("Enter the answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor("violet")
t.write(ans, font=("arial",30,"normal"),align='center')

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('black')
t.write(solution, font=("arial",30,"normal"),align='center')

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write('Your answer: '+str(ans), font=("arial",30,"normal"),align='center')

# if
if ans == solution:
    screen.bgcolor('dodgerblue')
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.write('Correct', font=("arial", 30, "normal"), align='center')
if ans != solution:
    screen.bgcolor('red')
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.write('incorrect', font=("arial", 30, "normal"), align='center')

turtle.done()