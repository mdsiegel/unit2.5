#Matthew Siegel
#9/20/17
#olympics.py - Making the olympic rings

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xffff00,1)
white = Color(0xffffff,0)

blueOutline = LineStyle(10,blue)
greenOutline = LineStyle(10,green)
redOutline = LineStyle(10,red)
blackOutline = LineStyle(10,black)
yellowOutline = LineStyle(10,yellow)#pixels,color


blueCircle = CircleAsset(50, blueOutline, white)
yellowCircle = CircleAsset(50, yellowOutline, white)
blackCircle = CircleAsset(50, blackOutline, white)
greenCircle = CircleAsset(50, greenOutline, white)
redCircle = CircleAsset(50, redOutline, white)

Sprite(blueCircle, (100,100))
Sprite(blackCircle, (220,100))
Sprite(redCircle, (340,100))
Sprite(yellowCircle, (161,150))



App().run()
