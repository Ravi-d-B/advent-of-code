import pandas as pd

from day1_q1 import find_first_last_number

# Read the data from the txt file
data = pd.read_csv('data/day1.txt', sep=" ", header=None)

digit_dict = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e',
              'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

# Replace the spelled out numbers with their corresponding digits
data = data.replace(digit_dict, regex=True)
data = find_first_last_number(data)

print(data.sum())
