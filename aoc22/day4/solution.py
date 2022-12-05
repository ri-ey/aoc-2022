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
    score = 0
    for elf_pair in data:
        elf_a, elf_b = elf_pair.split(',')
        elf_a_lb, elf_a_ub = [int(k) for k in elf_a.split('-')]
        elf_b_lb, elf_b_ub = [int(k) for k in elf_b.split('-')]
        elf_a_set = set([k for k in range(elf_a_lb, elf_a_ub + 1)])
        elf_b_set = set([k for k in range(elf_b_lb, elf_b_ub + 1)])
        if elf_b_set.issubset(elf_a_set) or elf_a_set.issubset(elf_b_set):
            score += 1
    return score

    
def solution_part_2():
    data = utils.read_input(script_path).split('\n')
    score = 0
    for elf_pair in data:
        elf_a, elf_b = elf_pair.split(',')
        elf_a_lb, elf_a_ub = [int(k) for k in elf_a.split('-')]
        elf_b_lb, elf_b_ub = [int(k) for k in elf_b.split('-')]
        elf_a_set = set([k for k in range(elf_a_lb, elf_a_ub + 1)])
        elf_b_set = set([k for k in range(elf_b_lb, elf_b_ub + 1)])
        if len(elf_b_set.intersection(elf_a_set)) > 0:
            score += 1
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
