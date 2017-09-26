#Matthew Siegel
#9/20/17
#olympics.py - Making the olympic rings

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xffff00,1)
white = Color(0xffffff,1)

blueOutline = LineStyle(1,black)
greenOutline = LineStyle(1,black)
redOutline = LineStyle(1,black)
blackOutline = LineStyle(1,black)
yellowOutline = LineStyle(1,black)#pixels,color


blueCircle = CircleAsset(50, blueOutline, white)
yellowCircle = CircleAsset(50, yellowOutline, white)
blackCircle = CircleAsset(50, blackOutline, white)
GreenCircle = CircleAsset(50, blackOutline, white)
RedCircle = CircleAsset(50, blackOutline, white)

Sprite(blueCircle, (50,50))
=Sprite(yellowCircle, (100,100))

App().run()
