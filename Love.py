import turtle
print("Propose someone using \n\t Python")

turtle.tracer(0, 0)

wn = turtle.Screen()
wn.bgcolor("#FFFF00")
wn.title("First Drawing")
height = 1000
width = 1700
wn.setup(width, height)
skk = turtle.Turtle()
skk.pensize(5)
skk.color("Red")
skk.shape("circle")

# I alpha
skk.fillcolor("#FF0000") 
skk.penup()
skk.goto(-700, 400)   
skk.pendown()
skk.begin_fill() 
skk.forward(200)
skk.right(90)
skk.forward(30)
skk.right(90)
skk.forward(80)
skk.left(90)
skk.forward(280)
skk.left(90)
skk.forward(80)
skk.right(90)
skk.forward(30)
skk.right(90)
skk.forward(200)
skk.right(90)
skk.forward(30)
skk.right(90)
skk.forward(80)
skk.left(90)
skk.forward(280)
skk.left(90)
skk.forward(80)
skk.right(90)
skk.forward(30)
skk.end_fill() 


# <3
skk.fillcolor("#FF00FF") 
skk.penup()
skk.goto(0, 0)   
skk.pendown()
skk.begin_fill()


for x in range(180):
    skk.forward(2)
    skk.right(1)
    
for x in range(78):
    skk.forward(5)
    skk.right(1)
    
skk.penup()
skk.goto(0, 0)   
skk.pendown()
skk.left(80)
for x in range(180):
    skk.backward(2)
    skk.left(1)

for x in range(78):
    skk.backward(5)
    skk.left(1)
    
skk.end_fill() 

# U alpha
    
skk.fillcolor("#FF0000")
skk.begin_fill()
skk.penup()
skk.goto(400, 400)     
skk.pendown()
skk.right(170)
skk.forward(50)
skk.right(90)
skk.forward(180)
skk.right(180)

for x in range(180):
    skk.backward(2)
    skk.left(1)
    
skk.right(180)
skk.forward(180)
skk.right(90)
skk.forward(50)
skk.right(90)
skk.forward(180)
skk.right(180)
for x in range(180):
    skk.backward(2.9)
    skk.right(1)
skk.right(180)
skk.forward(180)

skk.end_fill() 

skk.penup()
skk.goto(0, -470)     
skk.pendown()
skk.color('deep pink')
style = ('Courier', 40, 'italic')
skk.write('Made By :-\n', font=style, align='center')
skk.write('Sourabh', font=style, align='center')
skk.hideturtle()



turtle.update()

turtle.done()

