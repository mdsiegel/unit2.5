#Matthew Siegel
#9/20/17
#germany.py - Making the german flag

from ggame import *

red = Color(0xFF0000,1)
yellow = Color(0xffff00,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) 
redRectangle = RectangleAsset(300,50,blackOutline,red)
yellowRectangle = RectangleAsset(300,50,blackOutline,yellow)
blackRectangle = RectangleAsset(300,50,blackOutline,black)

Sprite(blackRectangle)
Sprite(redRectangle, (0,50))
Sprite(yellowRectangle,(0,100))
App().run()

