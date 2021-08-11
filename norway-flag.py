from turtle import *

speed(2)
setup(800,500)
bgcolor("red")

#White Cross
up()
goto(-400,-50)
down()

color("white")
begin_fill()
forward(800)
left(90)
forward(100)
left(90)
forward(800)
end_fill()

#Move to next position
up()
goto(-100,-250)
down()

begin_fill()
forward(100)
right(90)
forward(500)
right(90)
forward(100)
end_fill()

#Blue Cross
up()
goto(-400,-25)
down()

color("midnightblue")
begin_fill()
forward(800)
left(90)
forward(50)
left(90)
forward(800)
end_fill()

#New position 2
up()
goto(-125,-250)
down()

begin_fill()
forward(50)
right(90)
forward(500)
right(90)
forward(50)
end_fill()

hideturtle()
