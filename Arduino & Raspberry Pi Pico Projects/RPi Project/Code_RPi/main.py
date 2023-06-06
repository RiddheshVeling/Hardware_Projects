from machine import Pin, I2C                            #I2C is a useful bus that allows data exchange between microcontrollers and peripherals with a minimum of wiring.
from ssd1306 import SSD1306_I2C
 
import utime
 
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
  
def ultrasonnic():
    timepassed=0
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    
    return timepassed
 
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height
 
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)       # Initialize I2C using pins GP0 & GP1 
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Initialize oled display
 
while True:
   
    oled.fill(0)
    measured_time = ultrasonnic()     
    distance_cm = (measured_time * 0.0343) / 2
    distance_cm = round(distance_cm,2)
  
    oled.text("Distance",20,15)
    oled.text(str(distance_cm)+" cm",20,35)
    oled.show()
    utime.sleep(1)