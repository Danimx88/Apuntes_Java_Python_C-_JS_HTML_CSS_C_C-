import turtle as t
tim = t.Turtle()
for _ in range(20):
    tim.color("red")
    tim.forward(10)
    tim.penup()
    tim.color("blue")
    tim.forward(10)
    tim.pendown()
