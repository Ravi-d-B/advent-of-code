total_count = 0

# Read file line by line
with open('data/day4.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        # Split line by spaces
        line = line.split(' ')
        # Remove all empty strings from list and the card/card number
        line = list(filter(None, line))[2:]
        line_sep = line.index('|')
        # Split the line into two lists
        winning_numbers = line[:line_sep]
        card_numbers = line[line_sep + 1:]

        # Check how many card numbers are in the winning numbers
        count = len(set(winning_numbers).intersection(card_numbers))

        if count > 0:
            total_count += 2**(count-1)

print(total_count)
