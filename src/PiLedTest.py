from hal import hal_input_switch as switch
from hal import hal_led as led
from time import sleep

led.init()
switch.init()
while True:
   

    if switch.read_slide_switch() == 0:
      for i in range (25):
         led.set_output(24, 1)
         sleep(0.05)
         led.set_output(24, 0)
         sleep(0.05)
         if switch.read_slide_switch() == 1 :
             break
      led.set_output(24, 0)


    elif switch.read_slide_switch() == 1:
     led.set_output(24, 0)
