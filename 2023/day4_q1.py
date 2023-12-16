
def get_card_numbers(card):
    # Split line by spaces
    card = card.split(' ')
    # Remove all empty strings from list and the card/card number
    card = list(filter(None, card))[2:]
    line_sep = card.index('|')
    # Split the line into two lists
    winning_nums = card[:line_sep]
    card_nums = card[line_sep + 1:]

    return winning_nums, card_nums


def check_matches(winning_nums, card_nums):
    # Check how many card numbers are in the winning numbers
    return len(set(winning_nums).intersection(card_nums))


if __name__ == '__main__':
    total_count = 0

    # Read file line by line
    with open('data/day4.txt') as f:
        lines = f.read().splitlines()
        for current_card in lines:
            winning_numbers, card_numbers = get_card_numbers(current_card)

            # Check how many card numbers are in the winning numbers
            count = check_matches(winning_numbers, card_numbers)

            if count > 0:
                total_count += 2**(count-1)

    print(total_count)
