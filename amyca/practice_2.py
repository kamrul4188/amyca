import turtle
import time

font = ('arial','18','bold')
turtle.ht()
for count in range(5):
    text = str(count)

    # Clear text
    turtle.setpos(0,0)
    turtle.color(turtle.bgcolor())
    turtle.begin_fill()
    turtle.fd(100)
    turtle.setheading(90)
    turtle.fd(30)
    turtle.setheading(180)
    turtle.fd(110)
    turtle.setheading(270)
    turtle.fd(30)
    turtle.setheading(0)
    turtle.fd(10)
    turtle.end_fill()

    # Write text
    turtle.color("blue")
    turtle.write(text,font=font,move=False)

    time.sleep(1)