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
    n = len(data)
    for idx in range(n - 4):
        packet = data[idx:idx+4]
        if len(set(packet)) == 4:
            return idx+4
    return 

    
def solution_part_2():
    data = utils.read_input(script_path)
    n = len(data)
    for idx in range(n - 14):
        packet = data[idx:idx+14]
        if len(set(packet)) == 14:
            return idx+14
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

