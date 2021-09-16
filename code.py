# light fixture prototype by Julia L. Wang
import board
import digitalio
import time

# Configure the internal GPIO connected to the 3 LEDs as a digital outputs
led = digitalio.DigitalInOut(board.GP16) # red light
led.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP17) # white light
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.GP18) # blue light
led3.direction = digitalio.Direction.OUTPUT

# Configure the internal GPIO connected to the 2 buttons as a digital inputs
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Sets the internal resistor to pull-up

button2 = digitalio.DigitalInOut(board.GP14)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

# Loop so the code runs continuously
toggle = 0 #0 is off, 1 is plant only, 2 is plant and worker
whitelight = False
while True:
    if not button.value and toggle == 0: #when button 1 is pressed
        # switch to plant only
        toggle = 1
        time.sleep(1) #otherwise it'll toggle through all of them on 1 press
    elif not button.value and toggle == 1:
        #switch to worker and plant
        toggle = 2
        time.sleep(1)
    elif not button.value and toggle==2:
        toggle=0
        time.sleep(1)

    if toggle == 1: #plant only mode
        led.value = 1 #red+blue lights are on
        led3.value = 1
    elif toggle == 2: #plant and worker
        led.value = 1 #red+blue lights are on
        led3.value = 1
        if not button2.value:
            whitelight= not whitelight
            time.sleep(1)
        led2.value = whitelight #white light controlled by workers button
    else: #off mode
        led.value= 0
        led2.value=0
        led3.value = 0
