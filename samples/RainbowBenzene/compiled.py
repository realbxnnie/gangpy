# < THIS FILE WAS AUTOMATICALLY COMPILED BY Gangpy COMPILER. >
# < https://github.com/realbxnnie/gangpy >

import turtle 
import random
цвета = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
черепаха = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    черепаха.pencolor(цвета[random.randint(0, 5)]) 
    черепаха.width(x//100 + 1) 
    черепаха.back(x) 
    черепаха.left(59) 
