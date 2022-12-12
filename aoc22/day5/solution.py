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
    temp_stacks, moves_list = data.split('\n\n')
    temp_stacks = temp_stacks.split('\n')
    temp_stacks, stacks_positions = temp_stacks[:-1][::-1], temp_stacks[-1]
    stacks = [[] for _ in range(9)]
    for i in range(1,10):
        for crate in temp_stacks:
            char_idx = stacks_positions.index(str(i))
            if crate[char_idx] != ' ':
                stacks[i - 1].append(crate[char_idx])
    moves_list = [[int(k.split()[1]), int(k.split()[3]) -1, int(k.split()[5]) -1] for k in moves_list.split('\n')]
    for moves in moves_list:
        for _ in range(moves[0]):
            stacks[moves[2]].append(stacks[moves[1]].pop())
    solution = ''.join([k[-1] for k in stacks])
    return solution

    
def solution_part_2():
    data = utils.read_input(script_path)
    temp_stacks, moves_list = data.split('\n\n')
    temp_stacks = temp_stacks.split('\n')
    temp_stacks, stacks_positions = temp_stacks[:-1][::-1], temp_stacks[-1]
    stacks = [[] for _ in range(9)]
    for i in range(1,10):
        for crate in temp_stacks:
            char_idx = stacks_positions.index(str(i))
            if crate[char_idx] != ' ':
                stacks[i - 1].append(crate[char_idx])
    moves_list = [[int(k.split()[1]), int(k.split()[3]) -1, int(k.split()[5]) -1] for k in moves_list.split('\n')]
    for moves in moves_list:
        popped = []
        for _ in range(moves[0]):
            popped.append(stacks[moves[1]].pop())
        stacks[moves[2]] = stacks[moves[2]] + popped[::-1]
    solution = ''.join([k[-1] for k in stacks])
    return solution

def main():
    t0 = time.perf_counter()
    print('Part 1:', solution_part_1())
    print(f't(s) = {time.perf_counter() - t0:.3f}')
    print()
    t0 = time.perf_counter()
    print('Part 2:', solution_part_2())
    print(f't(s) = {time.perf_counter() - t0:.3f}')

if __name__ == '__main__':
    main()