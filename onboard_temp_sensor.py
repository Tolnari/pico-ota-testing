import machine
import time
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

# firmware_url = "https://https://raw.githubusercontent.com/Tolnari/pico-ota-testing/refs/heads/main/<file_name>"

# Do python things

adcpin = 4
sensor = machine.ADC(adcpin)
LED = machine.Pin(25, machine.Pin.OUT)
foo = True
roo = False
  
def ReadTemperature():
	adc_value = sensor.read_u16()
	volt = (3.3/65535) * adc_value
	temperature = 27 - (volt - 0.706)/0.001721
	return round(temperature, 1)
  
while True:
	temperature = ReadTemperature()
	#LED.toggle()
	LED.value(foo)
	time.sleep(1)
	LED.value(roo)
	print(f"Celcius {temperature}")
	print(f"farenheit {round(temperature * (9/5) + 32, 1)}")
	time.sleep(4)
	print("Foo")