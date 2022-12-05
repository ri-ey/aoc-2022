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
    data = utils.read_input(script_path).split('\n')
    all_chars = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower() + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    for rucksack in data:
        comp_a, comp_b = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        for char in comp_a:
            if char in comp_b:
                score += all_chars.index(char)
                comp_b = comp_b.replace(char, '')
    return score

    
def solution_part_2():
    data = utils.read_input(script_path).split('\n')
    all_chars = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower() + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    n = len(data)
    for idx in range(0,n,3):
        comp_a, comp_b, comp_c = data[idx], data[idx+1], data[idx+2]

        for char in comp_a:
            if char in comp_b and char in comp_c:
                score += all_chars.index(char)
                comp_b = comp_b.replace(char, '')
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