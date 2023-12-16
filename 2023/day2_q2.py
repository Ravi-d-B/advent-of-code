import pandas as pd
import re


def check_color_power(color_array):
    max = 0
    for color in color_array:
        amount = int(color.split(' ')[0])
        if amount > max:
            max = amount
    return max


count = 0
with open('data/day2.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        game_number = int(line[5:line.find(':')])

        reds = re.findall(r'\d+ red', line)
        blues = re.findall(r'\d+ blue', line)
        greens = re.findall(r'\d+ green', line)
        count += check_color_power(reds) * check_color_power(blues) * check_color_power(greens)


print(count)
