from distutils.filelist import glob_to_re
from turtle import *


#we want to paint a house

#step 1: draw a square
speed(50)
begin_fill()
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
end_fill()
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
penup()


begin_fill()
goto(-760,-385)
left(90)
pendown()
forward(1520)
left(90)
forward(380)
left(90)
forward(1520)
left(90)
forward(380)
end_fill()
penup()


color("yellow")
begin_fill()
goto(-670,390)
pendown()
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()
penup()

begin_fill()
goto(-500,0)
pendown()
color("black")
left(90)
forward(180)
right(90)
forward(50)
right(90)
forward(180)
right(90)
forward(50)
end_fill()
penup()

goto(-500,180)
begin_fill()
pendown()
color("brown")
forward(70)
right(90)
forward(150)
right(90)
forward(190)
right(90)
forward(150)
right(90)
forward(140)
end_fill()



exitonclick()