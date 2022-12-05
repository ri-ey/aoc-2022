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
    elfs = data.split('\n\n')
    max_calories = 0
    for elf in elfs:
        calories = list(map(int,elf.split('\n')))
        max_calories = max(max_calories,sum(calories))
    return max_calories
    
def solution_part_2():
    data = utils.read_input(script_path)
    elfs = data.split('\n\n')
    counter = 0
    total_calories = 0
    while counter < 3:

        max_calories = 0
        max_idx = -1
        for idx, elf in enumerate(elfs):
            calories = list(map(int,elf.split('\n')))
            if max_calories < sum(calories):
                max_calories = sum(calories)
                max_idx = idx        
        total_calories += max_calories
        counter += 1
        elfs.pop(max_idx)
    return total_calories


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
