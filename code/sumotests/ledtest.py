import board
import neopixel
import time
from guizero import App, PushButton




pixels = neopixel.NeoPixel(board.D18, 8, brightness=0.2)


pixels.fill((0,0,0))

time.sleep(1)

#pixels.brightness(0.6)




"""
def green():
    pixels.fill((0,255,0))

def red():
    pixels.fill((255,0,0))

def blue():
    pixels.fill((0,0,255))






app = App("LED Control", layout="auto")

button1 = PushButton(app, text="Green", command=green)
button2 = PushButton(app, text="Red", command=red)
button3 = PushButton(app, text="Blue", command=blue)



app.display()

"""
