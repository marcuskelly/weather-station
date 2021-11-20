# Raspberry Pi Oracle Weather Station

## Installation

Follow the guides and tutorials at [https://github.com/raspberrypilearning/weather\_station\_guide](https://github.com/raspberrypilearning/weather_station_guide) (published at [www.raspberrypi.org/weather-station](https://www.raspberrypi.org/weather-station/))

## Files needed for final weather station
[bme280_sensor.py](https://github.com/marcuskelly/weather-station/blob/main/bme280_sensor.py)  # Humidity, Pressure, Temperature <br />
[ds18b20_therm.py](https://github.com/marcuskelly/weather-station/blob/main/ds18b20_therm.py)  # Ground temperature probe <br />
[wind.py](https://github.com/marcuskelly/weather-station/blob/main/wind.py)  # Wind speed/gusts <br />
[wind_direction_byo.py](https://github.com/marcuskelly/weather-station/blob/main/wind_direction_byo.py)  # Wind direction <br />
[rainfall.py](https://github.com/marcuskelly/weather-station/blob/main/rainfall.py)  # Rainfall measurement <br />
[weather_station_BYO_1.py](https://github.com/marcuskelly/weather-station/blob/main/weather_station_BYO_1.py)  # Main driver (Part 1 - Wind speed, gusts and direction) <br />
weather_station_BYO_2.py  # Main driver (Part 2 - Rainfall) <br />
weather_station_BYO_3.py  # Main driver (Part 3 - Temperature, pressure and humidity) <br />
weather_station_BYO_4.py  # Main driver (Part 4 - Ground temperature) <br />
weather_station_BYO_5.py  # Main driver (Part 5 - Storing measurements in a local database) <br />
[weather_station_BYO.py](https://github.com/marcuskelly/weather-station/blob/main/weather_station_BYO.py)  # Main driver (Final program)

## Version

This repo contains the updated version of the software, re-engineered for the [Stretch version of Raspbian](https://www.raspberrypi.org/blog/raspbian-stretch/). If you are an existing Weather Station owner and are using a Pi running the Jessie version of Raspbian, then this code will not work without modification. You should flash your SD card with the [latest Raspbian image](https://www.raspberrypi.org/downloads/raspbian/) and perform a fresh install of this software (you may wish to take a copy of your local MYSQL database first).

----------

