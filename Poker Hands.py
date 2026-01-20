from collections import Counter

def process_card_lines(lines):
    first_half = []
    second_half = []

    for line in lines:
        cards = line.split()
        first_five = cards[:5]
        last_five = cards[5:]

        first_half.append(first_five)
        second_half.append(last_five)

    return first_half, second_half


def modified_unique_values(cards):
    value_counts = Counter(cards)

    three_of_a_kind = sorted([value for value in cards if value_counts[value] == 3], reverse=True)
    pairs = sorted([value for value in cards if value_counts[value] == 2], reverse=True)
    singles = sorted([value for value in cards if value_counts[value] == 1], reverse=True)

    return three_of_a_kind + pairs + singles



def get_hand_rank(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
              'A': 14}

    cards = sorted([values[card[:-1]] for card in hand], reverse=True)
    suits = [card[-1] for card in hand]

    value_counts = Counter(cards)
    count_values = sorted(value_counts.values(), reverse=True)
    unique_values = sorted(value_counts.keys(), reverse=True)

    is_flush = len(set(suits)) == 1
    is_straight = len(unique_values) == 5 and (unique_values[0] - unique_values[-1] == 4)

    if is_flush and is_straight and unique_values[0] == 14:
        return (10, modified_unique_values(cards))  # Royal Flush
    if is_flush and is_straight:
        return (9, modified_unique_values(cards))  # Straight Flush
    if count_values == [4, 1]:
        return (8, modified_unique_values(cards))  # Four of a Kind
    if count_values == [3, 2]:
        return (7, modified_unique_values(cards))  # Full House
    if is_flush:
        return (6, modified_unique_values(cards))  # Flush
    if is_straight:
        return (5, modified_unique_values(cards))  # Straight
    if count_values == [3, 1, 1]:
        return (4, modified_unique_values(cards))  # Three of a Kind
    if count_values == [2, 2, 1]:
        return (3, modified_unique_values(cards))  # Two Pairs
    if count_values == [2, 1, 1, 1]:
        return (2, modified_unique_values(cards))  # One Pair
    return (1, modified_unique_values(cards))  # High Card


def compare_hands(hand1, hand2):
    rank1, values1 = get_hand_rank(hand1)
    rank2, values2 = get_hand_rank(hand2)

    if rank1 > rank2:
        return "Hand 1 wins", rank1
    if rank2 > rank1:
        return "Hand 2 wins", rank2
    if values1 > values2:
        return "Hand 1 wins", rank1
    elif values2 > values1:
        return "Hand 2 wins", rank2
    else:
        return "It's a tie", rank1


input_text = []
print("Enter card hands (one per line, empty line to finish):")
while True:
    line = input().strip()
    if not line:
        break
    input_text.append(line)

first_half, second_half = process_card_lines(input_text)
print("First Half:", first_half)
print("Second Half:", second_half)


c = 0
for i in range(len(first_half)):
    result, winning_rank = compare_hands(first_half[i], second_half[i])
    print(f"Hand {i + 1}: {result} with rank {winning_rank}")
    if result == "Hand 1 wins":
        c = c + 1

print(f"Hand 1 won {c} times")
