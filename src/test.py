# from m5stack import *
# from uiflow import *
# from m5ui import *
# import time

# setScreenColor(0x222222)

# label1 = M5TextBox(120, 103, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)

# while True:
#     label1.setText(str(time.ticks_ms()))
#     checkExit()

from m5stack import *
from m5ui import *
# color example
color = lcd.RED
color = lcd.YELLOW
# color: 0x000000 ~ 0xffffff
# note: used in text, circle, rect, img bg color
setScreenColor(color)
