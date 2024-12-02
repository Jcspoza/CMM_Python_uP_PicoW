# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 7 - 12
# Goal : Visualizar Tiempo en LCD 16x2 sincronizado por NTP
# Ref https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/4.openweather.html

# 0- Import the required libraries
import urequests
import utime, ntptime
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from do_connect import *      
from secrets import *

# Informative block - start
p_ucontroler = "Pico W ONLY"
p_keyOhw = "LCD I2c 16x2 - sda=GPIO0, scl=GPIO1 & vcc lcd on VBUS"
p_project = "LCD weather OpenWeather - sinchronised by NTP"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# TIMEZONE = 2 # sPAIN IS gmt +2
LCD_ADDR = 0x3F
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16
FREQ = 400000   # Try lowering this value in case of "Errno 5"
CH_SMILE = [0x00, 0x00, 0x11, 0x04, 0x04, 0x11, 0x0E, 0x00]

i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)

print('Scanning I2C bus.')
devices = i2c.scan() # this returns a list of devices
device_count = len(devices)
if device_count == 0:
    print('No i2c device found.')
else:
    print(device_count, 'devices found.')
for device in devices:
    print('Decimal address:', device, ", Hex address: ", hex(device))

lcd = I2cLcd(i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

print("Llenar display con mensaje de prueba")
lcd.clear()
lcd.custom_char(0, CH_SMILE)
linea0 = chr(0)+' BM Makers '+chr(0)
lcd.move_to((LCD_NUM_COLS - len(linea0))//2, 0) # centra la cadena de claracteres
lcd.putstr(linea0)
lcd.move_to(0,1)
lcd.putstr("PicoW+LCD->"+str(hex(devices[0])))
utime.sleep(4)

lcd.clear()
lcd.putstr("BM Makers weather")
lcd.move_to(0,1)
lcd.putstr("Connec. wifi=")
do_connect()
lcd.putstr("OK")
utime.sleep(4)

# syncing the time
import ntptime
while True:
    try:
        ntptime.settime()
        print('Time Set Successfully')
        break
    except OSError:
        print('Time Setting...')
        continue

# Open Weather
TEMPERATURE_UNITS = {
    "standard": "K",
    "metric": "°C",
    "imperial": "°F",
}

SPEED_UNITS = {
    "standard": "m/s",
    "metric": "m/s",
    "imperial": "mph",
}

units = "metric"

def get_weather(city, api_key, units='metric', lang='en'):
    '''
    Get weather data from openweathermap.org
        city: City name, state code and country code divided by comma, Please, refer to ISO 3166 for the state codes or country codes. https://www.iso.org/obp/ui/#search
        api_key: Your unique API key (you can always find it on your openweather account page under the "API key" tab https://home.openweathermap.org/api_keys)
        unit: Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default. More: https://openweathermap.org/current#data
        lang: You can use this parameter to get the output in your language. More: https://openweathermap.org/current#multi
    '''
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}&lang={lang}"
    print(url)
    res = urequests.post(url)
    return res.json()

def print_weather(weather_data):
    print(f'Timezone: {int(weather_data["timezone"] / 3600)}')
    sunrise = time.localtime(weather_data['sys']['sunrise']+weather_data["timezone"])
    sunset = time.localtime(weather_data['sys']['sunset']+weather_data["timezone"])
    print(f'Sunrise: {sunrise[3]}:{sunrise[4]}')
    print(f'Sunset: {sunset[3]}:{sunset[4]}')   
    print(f'Country: {weather_data["sys"]["country"]}')
    print(f'City: {weather_data["name"]}')
    print(f'Coordination: [{weather_data["coord"]["lon"]}, {weather_data["coord"]["lat"]}]')
    print(f'Visibility: {weather_data["visibility"]}m')
    print(f'Weather: {weather_data["weather"][0]["main"]}')
    print(f'Temperature: {weather_data["main"]["temp"]}{TEMPERATURE_UNITS[units]}')
    print(f'Temperature min: {weather_data["main"]["temp_min"]}{TEMPERATURE_UNITS[units]}')
    print(f'Temperature max: {weather_data["main"]["temp_max"]}{TEMPERATURE_UNITS[units]}')
    print(f'Temperature feels like: {weather_data["main"]["feels_like"]}{TEMPERATURE_UNITS[units]}')
    print(f'Humidity: {weather_data["main"]["humidity"]}%')
    print(f'Pressure: {weather_data["main"]["pressure"]}hPa')
    print(f'Wind speed: {weather_data["wind"]["speed"]}{SPEED_UNITS[units]}')
#     print(f'Wind gust: {weather_data["wind"]["gust"]}{SPEED_UNITS[units]}')
    print(f'Wind direction: {weather_data["wind"]["deg"]}°')
    if "clouds" in weather_data:
        print(f'Cloudiness: {weather_data["clouds"]["all"]}%')
    elif "rain" in weather_data:
        print(f'Rain volume in 1 hour: {weather_data["rain"]["1h"]}mm')
        print(f'Rain volume in 3 hour: {weather_data["rain"]["3h"]}mm')
    elif "snow" in weather_data:
        print(f'Snow volume in 1 hour: {weather_data["snow"]["1h"]}mm')
        print(f'Snow volume in 3 hour: {weather_data["snow"]["3h"]}mm')    


while True:
    # get weather
    weather_data = get_weather('madrid', secrets['openweather_api_key'], units=units)
    weather=weather_data["weather"][0]["main"]
    t=weather_data["main"]["temp"]
    rh=weather_data["main"]["humidity"]

    # get time
    hours=utime.localtime()[3]+int(weather_data["timezone"] / 3600)
    mins=utime.localtime()[4]

    # LCD print
    lcd.clear() 
    utime.sleep_ms(200)
    string = f'{hours:02d}:{mins:02d} {weather}'
    lcd.putstr(string)
    lcd.move_to(0,1)
    string = f'{t}{TEMPERATURE_UNITS[units]} {rh}%rh'
    lcd.putstr(string)
    

    # shell print
    print_weather(weather_data)

    # refresh every 30s
    utime.sleep(30)




# weather data example:
# {
#     'timezone': 28800,
#     'sys': {
#         'type': 2,
#         'sunrise': 1659650200,
#         'country': 'CN',
#         'id': 2031340,
#         'sunset': 1659697371
#     },
#     'base': 'stations',
#     'main': {
#         'pressure': 1008,
#         'feels_like': 304.73,
#         'temp_max': 301.01,
#         'temp': 300.4,
#         'temp_min': 299.38,
#         'humidity': 91,
#         'sea_level': 1008,
#         'grnd_level': 1006
#     },
#     'visibility': 10000,
#     'id': 1795565,
#     'clouds': {
#         'all': 96
#     }, 
#     'coord': {
#         'lon': 114.0683,
#         'lat': 22.5455
#     },
#     'name': 'Shenzhen',
#     'cod': 200,
#     'weather':[{
#         'id': 804,
#         'icon': '04d',
#         'main': 'Clouds',
#         'description': 'overcast clouds'
#     }],
#     'dt': 1659663579,
#     'wind': {
#         'gust': 7.06,
#         'speed': 3.69,
#         'deg': 146
#     }
# }
