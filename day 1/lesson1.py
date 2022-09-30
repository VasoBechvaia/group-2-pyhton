from turtle import *


#we want to paint a house

#step 1: draw a square
speed(50)
width(8)
color("blue") 
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)  
#end of square

#drawing a door
begin_fill()
forward(70)
color("brown")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()  
#end of roof

#window

color("green")
begin_fill()
penup()
goto(20,140)
pendown()
left(120)
forward(35)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
#end of first window

#start of second window
begin_fill()
penup()
goto(175,140)
pendown()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


exitonclick()