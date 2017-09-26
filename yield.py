#Matthew Siegel
#9/20/17
#yield.py - writing people's name

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xffff00,1)


blackOutline = LineStyle(10,black) #pixels,color
yellowTriangle = PolygonAsset([(0,0), (500,0), (250,500)], blackOutline, yellow)
yellowTriangle2 = PolygonAsset([(50,50), (450,50), (250,450)], blackOutline, yellow)

text = TextAsset('YIELD',fill=black,style='bold 40pt Times')

Sprite(yellowTriangle,)
Sprite(yellowTriangle2)
Sprite(text,(170,150))
App().run()
