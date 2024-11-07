import turtle
wn = turtle.Screen()
wn.bgcolor("white")
flower = turtle.Turtle()
flower.shape("circle")
flower.color("light pink")
flower.speed(10)
for _ in range(6):  
    flower.circle(100, 60) 
    flower.left(120)        
    flower.circle(100, 60)  
    flower.left(120)        
    flower.right(60)   

flower.color("black")
