#Matthew Siegel
#9/20/17
#name.py - writing people's name

from ggame import *

name = input('Enter you name: ')
colorCode = input('Enter a hex RGB code: ')
colorinput = Color(colorCode,1)
red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels,color

rectangle = RectangleAsset(1000,600,blackOutline,colorinput) #width height outline fill




text = TextAsset(name,fill = black,style='40pt Times')

Sprite(rectangle)
Sprite(text)
App().run()