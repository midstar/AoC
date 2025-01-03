import sys
from functools import cmp_to_key

def calc_strength(hand):
    cards = ''.join(sorted(hand))
    equals = [1, 1]
    equal_index = 0
    prev = '-'
    for i in range(0, len(cards)):
        card = cards[i]
        if card == prev:
            equals[equal_index] += 1
        elif equals[0] > 1 and equal_index == 0:
            equal_index = 1
        prev = card

    equals.sort(reverse=True)

    if (equals[0] == 5):
        return 7
    if (equals[0] == 4):
        return 6
    if (equals[0] == 3 and equals[1] == 2):
        return 5
    if (equals[0] == 3 and equals[1] == 1):
        return 4
    if (equals[0] == 2 and equals[1] == 2):
        return 3
    if (equals[0] == 2 and equals[1] == 1):
        return 2

    return 1

def cardValue(c):
    if c == 'A':
        return 14
    if c == 'K':
        return 13
    if c == 'Q':
        return 12
    if c == 'J':
        return 11
    if c == 'T':
        return 10
    return int(c)

def compare(game1, game2):
    if game1['strength'] != game2['strength']:
        return game1['strength'] - game2['strength']
    # Equals
    for i in range(0, len(game1['hand'])):
        c1 = cardValue(game1['hand'][i])
        c2 = cardValue(game2['hand'][i])
        if c1 != c2:
            return c1 - c2
    

    print("WARNING EQUAL %s %s" % (game1, game2))
    return 0



def solve(input):
    lines = input.splitlines()
    games = []
    for line in lines:
        hand_bid = line.split()
        game = {
            'hand' : hand_bid[0],
            'bid'  : int(hand_bid[1]),
            'strength' : calc_strength(hand_bid[0])
        }
        games.append(game)
    
    compare_key = cmp_to_key(compare)
    gamesRanked = sorted(games, key=compare_key)

    result = 0
    for i in range (0, len(gamesRanked)):
        result += gamesRanked[i]['bid'] * (i + 1)

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))