import re

pattern = r'Рейс (\d+) (?:прибыл|отправился) (из|в) (\w+) в (\d+:\d+:\d+)'

with open("input_travel.txt", "r", encoding="utf-8") as text:
    text = text.read()
    response = re.findall(pattern, text)

with open("output_travel.txt", "w", encoding="utf-8") as add_text:
    for num in response:
        add_text.write(f'[{num[3]}]: - Поезд № {num[0]} {num[1]} {num[2]}\n')
