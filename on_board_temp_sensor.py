import machine
import time
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

# version 1

# Check for updates
firmware_url = "https://raw.githubusercontent.com/Tolnari/pico-ota-testing/"
ota_updater = OTAUpdater(SSID, PASSWORD,firmware_url, "on_board_temp_sensor.py")
ota_updater.download_and_install_update_if_available()

# Do python things

adcpin = 4
sensor = machine.ADC(adcpin)

def ReadTemperature():
	adc_value = sensor.read_u16()
	volt = (3.3/65535) * adc_value
	temperature = 27 - (volt - 0.706)/0.001721
	return round(temperature, 1)
  
while True:
	temperature = ReadTemperature()
	time.sleep(1)
	print(f"farenheit {round(temperature * (9/5) + 32, 1)}")
	print(f"Celcius   {temperature}")
	print()
	time.sleep(4)
