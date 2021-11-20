import bme280
import smbus2

port = 1
address = 0x77
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)


def read_all():
    bme280_data = bme280.sample(bus, address)
    return bme280_data.humidity, bme280_data.pressure, bme280_data.temperature

# Uncomment below line for testing
# print(read_all())
