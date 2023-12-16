import pandas as pd
import re


def check_color(color_array, max_color):
    for color in color_array:
        amount = int(color.split(' ')[0])
        if amount > max_color:
            return False

    return True


max_red = 12
max_blue = 14
max_green = 13

count = 0
with open('data/day2.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        game_number = int(line[5:line.find(':')])

        reds = re.findall(r'\d+ red', line)
        blues = re.findall(r'\d+ blue', line)
        greens = re.findall(r'\d+ green', line)
        if check_color(reds, max_red) and check_color(blues, max_blue) and check_color(greens,
                                                                                       max_green):
            count += game_number


print(count)
