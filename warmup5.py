#Matthew Siegel
#9/26/17
#warmup5.py - making a diamond with my name

from ggame import *

blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xffff00,1)


blackOutline = LineStyle(1,black) #pixels,color


yellowDiamond = PolygonAsset([(0,200), (200,0), (400,200),(200,400)], blackOutline, yellow)
text = TextAsset('Matthew',fill=blue,style='bold 40pt Times')

Sprite(yellowDiamond,)
Sprite(text,(100,150))
App().run()
