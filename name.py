#Matthew Siegel
#9/20/17
#name.py - writing people's name

from ggame import *

name = input('Enter you name: ')
colorCode = input('Enter a hex RGB code: ')
colorinput = Color(colorCode,1)

text = TextAsset(name,fill=colorinput,style='40pt Times')

Sprite(text)
App().run()