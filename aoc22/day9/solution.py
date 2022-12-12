import os
import sys
import time
import math

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils

# def for k in list('LRUD'):
#         counts = 0
#         for cmd in data:
#             if k in cmd:
#                 counts += int(cmd.split()[-1])
#         max_size = max(max_size, counts)


def move_as_coords(cmd):
    if 'R' in cmd:
        return [1, 0], int(cmd.split()[-1])
    elif 'L' in cmd:
        return [-1, 0], int(cmd.split()[-1])
    elif 'U' in cmd:
        return [0, 1], int(cmd.split()[-1])
    elif 'D' in cmd:
        return [0, -1], int(cmd.split()[-1])

def move_tracker(head_pos, tail_pos, move):
    if move:
        head_pos = [head_pos[0] + move[0], head_pos[1] + move[1]]
    tail_moves = []
    while max(abs(tail_pos[0] - head_pos[0]), abs(tail_pos[1] - head_pos[1])) > 1:
        if tail_pos[0] != head_pos[0] and tail_pos[1] != head_pos[1]:
            if abs(tail_pos[0] - head_pos[0]) == 1:
                tail_pos[0] = head_pos[0]
                tail_pos[1] += int(math.copysign(1,head_pos[1] - tail_pos[1]))
            else:
                tail_pos[1] = head_pos[1]
                tail_pos[0] += int(math.copysign(1,head_pos[0] - tail_pos[0]))
            tail_moves.append(tuple(tail_pos))
        else:
            if tail_pos[0] == head_pos[0]:
                tail_pos[1] += int(math.copysign(1,head_pos[1] - tail_pos[1]))
            else:
                tail_pos[0] += int(math.copysign(1,head_pos[0] - tail_pos[0]))
            tail_moves.append(tuple(tail_pos))

    return head_pos, tail_pos, tail_moves


def solution_part_1():
    data = utils.read_input(script_path)
    data = data.split('\n')
    tail_moves = set()
    head_pos = tail_pos = [0,0]
    tail_moves.add(tuple(tail_pos))
    for cmd in data:
        move, count = move_as_coords(cmd)
        for _ in range(count):
            head_pos, tail_pos, new_tail_moves = move_tracker(head_pos, tail_pos, move)
            if new_tail_moves:
                tail_moves.update(new_tail_moves)
    return len(tail_moves)

    
def solution_part_2():
    data = utils.read_input(script_path)
    data = data.split('\n')
    tail_moves = set()
    knots =  [[0,0] for _ in range(10)]
    tail_moves.add(tuple(knots[-1]))
    for cmd in data:
        move, count = move_as_coords(cmd)
        for _ in range(count):
            for idx in range(len(knots) - 1):
                if idx == 0:
                    head_pos, tail_pos = knots[idx], knots[idx + 1]
                    head_pos, tail_pos, new_tail_moves = move_tracker(head_pos, tail_pos, move)
                    knots[idx], knots[idx + 1] = head_pos, tail_pos
                else:
                    head_pos, tail_pos = knots[idx], knots[idx + 1]
                    head_pos, tail_pos, new_tail_moves = move_tracker(head_pos, tail_pos, None)
                    knots[idx], knots[idx + 1] = head_pos, tail_pos
                if idx == len(knots) - 2 and new_tail_moves:
                    tail_moves.update(new_tail_moves)
    return len(tail_moves)
    

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

