import re
from datetime import datetime
import ssl
import urllib.request

now = datetime.now()
current_time = now.strftime('%H:%M:%S')

ssl._create_default_https_context = ssl._create_unverified_context

town = input('Введите город на английском: ')

data = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={town}&units=metric&lang=ru&appid"
                              f"=c341e34f9b7c327502cde34aa7817c5f").read().decode()

name_pattern = r'(?:"name":")([^\d"]*)'
temp_pattern = r'(?:"temp":)([^\,]*)'
humidity_pattern = r'(?:"humidity":)([^\,]*)'
wind_pattern = r'(?:"speed":)([^\,]*)'
description_pattern = r'(?:"description":")([^\,]*)"'
pressure_pattern = r'(?:"pressure":)([^\,]*)'

print(current_time, sep='')


with open("test.txt", mode='w', encoding='UTF-8') as file:
    file.write(f'[{current_time}] ')
    file.write(f'Запрос погоды в городе: {re.findall(name_pattern, data)[0]}\n')
    file.write(f'Температура: {re.findall(temp_pattern, data)[0]}°C, {re.findall(description_pattern, data)[0]}\n')
    file.write(f'Влажность воздуха: {re.findall(humidity_pattern, data)[0]}%\n')
    file.write(f'Скорость ветра: {re.findall(wind_pattern, data)[0]} м/с\n')
    file.write(f'Атмосферное давление: {re.findall(pressure_pattern, data)[0]} мм рт. ст.\n')

print(f'Запрос погоды в городе: {re.findall(name_pattern, data)[0]}')
print(f'Температура: {re.findall(temp_pattern, data)[0]}°C, {re.findall(description_pattern, data)[0]}')
print(f'Влажность воздуха: {re.findall(humidity_pattern, data)[0]}%')
print(f'Скорость ветра: {re.findall(wind_pattern, data)[0]} м/с')
print(f'Атмосферное давление: {re.findall(pressure_pattern, data)[0]} мм рт. ст.')