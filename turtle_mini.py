import turtle

def my_initail():
	window = turtle.Screen()
	window.bgcolor("red")

	abu = turtle.Turtle()

	abu.color("yellow")
	abu.speed(2)
	abu.left(60)
	abu.forward(100)
	abu.right(120)
	abu.forward(100)
	abu.backward(50)

	#second
	umar = turtle.Turtle()

	umar.color("yellow")
	umar.speed(2)
	umar.left(60)
	umar.forward(50)
	umar.right(60)
	umar.forward(50)
   
	window.exitonclick()
my_initail()