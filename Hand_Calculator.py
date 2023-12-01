import time


def main():
    write_score(calculate_score(read_hand()))


def read_hand():
    """Reads hand.txt file and creates hand list"""

    with open('hand.txt', 'r') as f:
        hand = f.readline().split(',')
    return hand


def calculate_score(hand):
    """Takes in hand[] and returns hand calulated score"""

    score = 0
    high_ace_score = 0

    # Moves Aces to the end of the array
    if 'A' in hand:
        hand.remove('A')
        hand.append('A')

    # Iterate through hand adding to score
    for card in hand:
        if card == 'J' or card == 'K' or card == 'Q':
            score += 10
        elif card == 'A':
            high_ace_score = score
            score += 1
            high_ace_score += 11
        elif 2 <= int(card) <= 10:
            score += int(card)
        else:
            score = "Invalid Hand"
    return [score, high_ace_score]


def write_score(score_list):
    """Writes the hand score to hand_score.txt file"""

    score, high_ace_score = score_list

    if high_ace_score == 0:
        with open('hand_score.txt', 'w') as f:
            f.write(str(score))
    else:
        with open('hand_score.txt', 'w') as f:
            f.write(str(score))
            f.write(',')
            f.write(str(high_ace_score))


while True:
    write_score(calculate_score(read_hand()))
