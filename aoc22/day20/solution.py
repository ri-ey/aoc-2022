import os
import sys
import time
import json

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils

def solution_part_1():
    data = utils.read_input(script_path, 0)
    data = data.split('\n')
    for idx in range(len(data)):
        tmp = data[idx]
        data[idx] = (int(tmp), idx)    
    original_order = data.copy()
    N = len(data)
    for num in original_order:
        idx = data.index(num)
        value = data.pop(idx)[0]
        new_idx = (idx + value)%(N -1)
        data.insert(new_idx, num)

    data = [k[0] for k in data]
    number_idx = data.index(0)
    val = sum([number for number in [data[(number_idx + 3000)%N], data[(number_idx + 2000)%N], data[(number_idx + 1000)%N]]])
    return val



def solution_part_2():
    data = utils.read_input(script_path, 0)
    data = data.split('\n')
    for idx in range(len(data)):
        tmp = data[idx]
        data[idx] = (int(tmp)*811589153, idx)    
    original_order = data.copy()
    N = len(data)
    for _ in range(10):
        for num in original_order:
            idx = data.index(num)
            value = data.pop(idx)[0]
            new_idx = (idx + value)%(N -1)
            data.insert(new_idx, num)

    data = [k[0] for k in data]
    number_idx = data.index(0)
    val = sum([number for number in [data[(number_idx + 3000)%N], data[(number_idx + 2000)%N], data[(number_idx + 1000)%N]]])
    return val

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