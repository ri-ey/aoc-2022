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

def decode_cmd(cmd):
    if cmd == 'noop':
        return 1, 0
    else:
        return 2, int(cmd.split()[-1])

def solution_part_1():
    data = utils.read_input(script_path)
    data = data.split('\n')
    cycle = 0
    splits = [220, 180, 140, 100, 60, 20]
    score = 0
    X = 1
    for cmd in data:
        add_cycle, delta_x = decode_cmd(cmd)
        for _ in range(add_cycle):
            cycle += 1
            if cycle == splits[-1]:
                score += splits.pop() * X
            if not splits:
                return score
        X += delta_x
    return score

    
def solution_part_2():
    data = utils.read_input(script_path,1)
    data = data.split('\n')
    output = ['.'*41 for _ in range(6)]
    cycle = 0
    sprite_pos = [0, 1, 2]
    X = 1
    for cmd in data:
        row = cycle//40
        add_cycle, delta_x = decode_cmd(cmd)
        for _ in range(add_cycle):
            cycle += 1
            pxl = cycle%40
            print(pxl, sprite_pos)
            if pxl in sprite_pos:
                output[row] = output[row][:pxl] + '#' + output[row][pxl+1:]
        X += delta_x 
        sprite_pos = [X - 1, X, X + 1]
        if cycle == 240:
            return '\n'+ '\n'.join(output)
    return

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

