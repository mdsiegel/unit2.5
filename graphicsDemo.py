#Matthew Siegel
#9/20/17
#graphicsDemo.py - making graphic stuff

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels,color

redRectangle = RectangleAsset(200,100,blackOutline,red) #width height outline fill
blueCircle = CircleAsset(50, blackOutline, blue)

Sprite(redRectangle)
Sprite(blueCircle, (50,50))
App().run()
