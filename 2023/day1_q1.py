import pandas as pd


def find_first_last_number(df):
    # Remove all letters from the data
    df = df.replace(regex=r'[^0-9]', value='')

    # If only consists of one number, duplicate it
    df = df.replace(regex=r'^(\d)$', value=r'\1\1')

    # If it consists of more than two numbers, keep only the first and last
    df = df.replace(regex=r'^(\d)(\d+)(\d)$', value=r'\1\3')

    df = df.astype(int)

    return df


if __name__ == '__main__':
    # Read the data from the txt file
    data = pd.read_csv('data/day1.txt', sep=" ", header=None)
    data = find_first_last_number(data)

    print(data.sum())
