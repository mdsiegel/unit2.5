#Matthew Siegel
#9/20/17
#house.py - making a house

from ggame import *



red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

blackOutline = LineStyle(1,black)
blackRectangle = RectangleAsset(200,100,blackOutline,black)
greenTriangle = PolygonAsset([(100,100), (190,50), (300,100)], blackOutline, green)
door = RectangleAsset(25,50,blackOutline, white)


Sprite(blackRectangle,(100,100))
Sprite(greenTriangle)
Sprite(door,(190,150))
App().run()