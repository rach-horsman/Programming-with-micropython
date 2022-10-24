# Add your Python code here. E.g.
from microbit import *
# Servo control:
# 100 = 1 millisecond pulse all right
# 200 = 2 millisecond pulse all left
# 150 = 1.5 millisecond pulse center
# 10 is 10 milliseconds for period 1/100 Hz
while True:
 pin0.set_analog_period(10)
 pin0.write_analog(150)
 display.show(Image.ARROW_N)
 sleep(1000)
 pin0.write_analog(100)
 display.show(Image.ARROW_E)
 sleep(1000)
 pin0.write_analog(150)
 display.show(Image.ARROW_N)
 sleep(1000)
 pin0.write_analog(200)
 display.show(Image.ARROW_W)
 sleep(1000)
 pin0.write_analog(150)
 display.show(Image.ARROW_N)
 sleep(1000)