import os
import sys
import time

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils


def solution_part_1():
    data = utils.read_input(script_path)
    mapping = {'A':'R', 'B':'P', 'C':'S', 'X':'R', 'Y':'P', 'Z':'S'}
    winning_hands = {'S':'P', 'R':'S', 'P':'R'}
    points = {'R':1,'P':2,'S':3}
    for char_encoded, char_decoded in mapping.items():
        data = data.replace(char_encoded, char_decoded)
    data = data.split('\n')
    score = 0
    for hand in data:
        player_a, player_b = hand.split(' ')
        score += points[player_b]
        if player_a == player_b:
            score += 3
        elif winning_hands[player_b] == player_a:
            score += 6
    return score

    
def solution_part_2():
    data = utils.read_input(script_path)
    mapping = {'A':'R', 'B':'P', 'C':'S'}
    winning_hands = {'S':'P', 'R':'S', 'P':'R'}
    losing_hands  = {'P':'S', 'S':'R', 'R':'P'}
    points = {'R':1,'P':2,'S':3}
    for char_encoded, char_decoded in mapping.items():
        data = data.replace(char_encoded, char_decoded)
    data = data.split('\n')
    score = 0
    for hand in data:
        player_a, player_b = hand.split(' ')
        if player_b == 'X':
            player_b = winning_hands[player_a]
        elif player_b == 'Y':
            player_b = player_a
        else:
            player_b = losing_hands[player_a]
        score += points[player_b]
        if player_a == player_b:
            score += 3
        elif winning_hands[player_b] == player_a:
            score += 6
    return score


def main():
    t0 = time.perf_counter()
    print('Part 1:', solution_part_1())
    print(f't(s) = {time.perf_counter() - t0:.3f}')
    t0 = time.perf_counter()
    print()
    print('Part 2:', solution_part_2())
    print(f't(s) = {time.perf_counter() - t0:.3f}')

if __name__ == '__main__':
    main()
