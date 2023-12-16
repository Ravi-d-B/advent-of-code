from day4_q1 import get_card_numbers, check_matches


# Read file line by line
with open('data/day4.txt') as f:
    lines = f.read().splitlines()
    number_of_orignal_cards = len(lines)
    number_of_each_card = [1] * number_of_orignal_cards
    for i, line in enumerate(lines):
        winning_numbers, card_numbers = get_card_numbers(line)
        number_of_matches = check_matches(winning_numbers, card_numbers)
        for match_num in range(1, number_of_matches + 1):
            number_of_each_card[min(i + match_num, number_of_orignal_cards - 1)] += number_of_each_card[i]

print(sum(number_of_each_card))
