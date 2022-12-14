import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0)
# chan = AnalogIn(ads, ADS.P0, ADS.P1)  example with multiple pins being used
temp = chan.voltage * 100
print(temp)
