from turtle import *
speed(1)
shape("arrow")
color("yellow")
width(6.5)
forward(150)

left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(50)
color("brown")
left(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
right(90)
forward(50)
penup()
color("purple")
goto(150,150) #roof
begin_fill()
right(90)
left(40)
pendown()
forward(105)
left(95)
forward(110)
penup()
goto(150,150)
left(45)
right(90)
pendown()
forward(150)
end_fill()
exitonclick()
