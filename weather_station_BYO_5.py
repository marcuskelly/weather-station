from gpiozero import Button
import time
import math
import statistics
import database
import datetime

import bme280_sensor
import wind_direction_byo
import ds18b20_therm

CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600
ADJUSTMENT = 1.18
BUCKET_SIZE = 0.2794

wind_count = 0  # Counts how many half-rotations
radius_cm = 9.0  # Radius of your anemometer
wind_interval = 5  # Hpw often (secs) to report speed
interval = 25  # How long in seconds to collect data
rain_count = 0
gust = 0
store_speeds = []
store_directions = []


# Every halsf-rotation, add 1 to count
def spin():
    global wind_count
    wind_count = wind_count + 1
    # print("spin" + str(wind_count))


# Calculate the wind speed
def calculate_speed(time_sec):
    global wind_count
    circumference_cm = (2 * math.pi) * radius_cm
    rotations = wind_count / 2.0

    # Calculate distance traveled by a cup in cm
    dist_km = (circumference_cm * rotations) / CM_IN_A_KM
    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * SECS_IN_AN_HOUR

    return km_per_hour * ADJUSTMENT


def bucket_tipped():
    global rain_count
    rain_count = rain_count + 1
    print(rain_count * BUCKET_SIZE)


def reset_wind():
    global wind_count
    wind_count = 0


def reset_rainfall():
    global rain_count
    rain_count = 0


def reset_gust():
    global gust
    gust = 0

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin
temp_probe = ds18b20_therm.DS18B20()

rain_sensor = Button(6)
rain_sensor.when_pressed = bucket_tipped

db = database.weather_database()

while True:
    start_time = time.time()
    while time.time() - start_time <= interval:
        wind_start_time = time.time()
        reset_wind()
        # time.sleep(wind_interval)
        while time.time() - wind_start_time <= wind_interval:
            store_directions.append(wind_direction_byo.get_value())

        final_speed = calculate_speed(wind_interval)
        store_speeds.append(final_speed)
    created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    wind_average = wind_direction_byo.get_average(store_directions)
    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    rainfall = rain_count * BUCKET_SIZE
    ground_temp = temp_probe.read_temp()
    humidity, pressure, ambient_temp = bme280_sensor.read_all()
    reset_rainfall()
    store_speeds = []
    store_directions = []
    
    print('Wind direction:\t\t' + str(wind_average))
    print('Wind speed:\t\t' + str(wind_speed))
    print('Wind gust:\t\t' + str(wind_gust))
    print('Ambient Temperature:\t' + str(ambient_temp))
    print('Ground Temperature:\t' + str(ground_temp))
    print('Humidity:\t\t' + str(humidity))
    print('Pressure:\t\t' + str(pressure))
    print('Rainfall:\t\t' + str(rainfall))
    
    print("Inserting into database...")
    db.insert(ambient_temp, ground_temp, 0, pressure, humidity, wind_average, wind_speed, wind_gust, rainfall, created)
