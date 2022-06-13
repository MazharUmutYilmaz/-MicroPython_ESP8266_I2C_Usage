# Code for I2C Usage with SSD1306 and DHT11 for Weather Station on ESP8266 with MicroPython
from machine import Pin, I2C 
import ssd1306 
import dht  
from time import sleep_ms

sensor_value=dht.DHT11(Pin(12)) 
i2c=I2C(sda=Pin(4),scl=Pin(5))
screen=ssd1306.SSD1306_I2C(128,64,i2c)

while True:
  sensor_value.measure()
  sleep_ms(2000)
  value_of_temperature=sensor_value.temperature()
  value_of_humidity=sensor_value.humidity()
  screen.fill(0) 
  screen.text("Weather Station",10, 0, 1)
  screen.hline(10, 10, 120, 1)   
  screen.text("Temperature:",0, 20, 1)
  screen.text(str(value_of_temperature),96, 20, 1)
  screen.text(" C",108, 20, 1)
  screen.text("Humidity:",0, 40, 1)
  screen.text(str(value_of_humidity),72, 40, 1)
  screen.text(" %RH",84, 40, 1)  
  screen.show()
