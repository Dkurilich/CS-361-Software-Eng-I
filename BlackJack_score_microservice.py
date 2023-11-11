while True:
    with open('card_hand.txt', 'r+', encoding="utf-8") as card_hand:
        cards = card_hand.read()
    card_hand.close()
    if cards == '':
        continue
    else:

        # this section calculates score based on an Ace = 1
        card_score_list = list(cards.split(" "))
        score = 0
        for card in card_score_list:
            score += int(card)
        score = str(score)

        # this section calculates score based on an Ace = 11
        score_ace = 0
        if "1" in card_score_list:
            score_ace = 10
            for card in card_score_list:
                score_ace += int(card)

        # 2 scores are written every time, in case there is an Ace with two scoring options
        cards_values = [score, score_ace]
        cards_values = ' '.join(str(card) for card in cards_values)
        with open('card_hand_score.txt', 'w', encoding="utf-8") as card_score_file:
            card_score_file.write(cards_values)
        card_score_file.close()
