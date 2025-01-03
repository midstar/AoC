import sys

def solve(input):
    sum = 0
    game = 0
    card_points = []
    card_nbrs = []
    for line in input.splitlines():
        game += 1
        game_str = line.split(':')[1].split('|')
        win_numbers = game_str[0].split()
        numbers = game_str[1].split()
        points = 0
        for win_number in win_numbers:
            if win_number in numbers:
                points += 1
        card_points.append(points)
        card_nbrs.append(1)

    for i in range (0, len(card_points)):
        points = card_points[i]
        if points > 0:
            end = min(len(card_points), i + 1 + card_points[i])
            for j in range (i + 1, end):
                card_nbrs[j] += card_nbrs[i]

    #print(card_nbrs)
    sum = 0
    for card_nbr in card_nbrs:
        sum += int(card_nbr)
    return sum

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))