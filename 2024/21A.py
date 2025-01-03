import sys
import heapq
from functools import cache

numpad = {}
keypad = {}

DIR = {
    '^' : (-1, 0),
    'v' : (1, 0),
    '<' : (0, -1),
    '>' : (0, 1)
}

@cache
def get_new_pos(pos, dir):
    return (pos[0] + DIR[dir][0], pos[1] + DIR[dir][1])

def move(pad,start,stop):
    moves = []
    shortest = 1000000
    q = [(start,[])]
    while q:
        entry = q.pop(0)
        pos, dirs = entry
        if pos == stop:
            if len(dirs) <= shortest:
                shortest = min(len(dirs), shortest) 
                moves.append(dirs)
                continue
            else:
                return moves
        for dir in DIR.keys():
            pos2 = get_new_pos(pos,dir)
            if pos2 in pad.values():
                q.append((pos2, dirs + [dir]))
    return moves    

@cache
def move_numpad(start_command,stop_command):
    return move(numpad,numpad[start_command],numpad[stop_command])

@cache
def move_keypad(start_command,stop_command):
    return move(keypad,keypad[start_command],keypad[stop_command])

@cache
def robot_moves(commands, nbr_robots = 1):
    result = []
    current_command = 'A'
    for command in commands:
        moves = move_keypad(current_command,command)
        if nbr_robots == 1:
            result += min(moves,key=len)
            result.append('A')
        else:
            result += min([robot_moves(''.join(m) + 'A', nbr_robots - 1) for m in moves], key=len)
        current_command = command
    return result

def gridify(s):
    grid = {}
    for r, line in enumerate(s.splitlines()):
        for c, val in enumerate(line):
            if val != ' ':
                grid[val] = (r,c)
    return grid

def solve(input):
    global numpad
    global keypad

    numpad = gridify('''\
789
456
123
 0A''')
    
    keypad = gridify('''\
 ^A
<v>''')

    result = 0
    for code in input.splitlines():
        #print('--------',code)
        min_moves = 0
        full_move = ''
        prev = 'A'
        for num in code:
            numpad_moves = move_numpad(prev , num)
            min_moves_num = 1000000000
            full_move_num = ''
            #print('###', num)
            for numpad_move in numpad_moves:
                keypad_moves = robot_moves(''.join(numpad_move) + 'A', 2)
                if  len(keypad_moves) <= min_moves_num:
                    full_move_num = ''.join(keypad_moves)
                min_moves_num = min(min_moves_num,len(keypad_moves))
            min_moves += min_moves_num
            full_move += full_move_num
            prev = num  
        points = min_moves * int(code[:3])
        result += points
        #print(min_moves, int(code[:3]), points)
        #print(full_move)

    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))