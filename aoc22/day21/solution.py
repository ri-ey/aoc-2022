import os
import sys
import time
import json

from sympy.solvers import solve
from sympy import Symbol

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils

def solution_part_1():
    data = utils.read_input(script_path,0)
    data = data.split('\n')
    numbers = {}
    not_found = []
    for k in range(len(data)):
        data[k] = data[k].split(': ')
        data[k][1] = data[k][1].replace(' ', '')
        if data[k][1].isdigit():
            numbers[data[k][0]] = int(data[k][1])
        else:
            not_found.append(data[k])
    
    while 'root' not in numbers:
        not_found_cp = not_found.copy()
        for idx, og_val in enumerate(not_found_cp):
            changed = 0
            val = og_val.copy()
            for key in numbers:
                if key in val[1]:
                    changed += 1
                    val[1] = val[1].replace(key, str(numbers[key]))
                    if changed == 2:
                        break
            if changed == 2:
                not_found.remove(og_val)
                numbers[val[0]] = eval(val[1])
        
    return int(numbers['root'])

    
def solution_part_2():
    data = utils.read_input(script_path,0)
    data = data.split('\n')
    numbers = {}
    not_found = []
    for k in range(len(data)):
        data[k] = data[k].split(': ')
        data[k][1] = data[k][1].replace(' ', '')
        if data[k][0] == 'humn':
            numbers[data[k][0]] = 'x'
        elif data[k][1].isdigit():
            numbers[data[k][0]] = int(data[k][1])
        else:
            if data[k][0] == 'root':
                data[k][1] = data[k][1].replace('+', '-')
            not_found.append(data[k])
    
    while 'root' not in numbers:
        not_found_cp = not_found.copy()
        for idx, og_val in enumerate(not_found_cp):
            changed = 0
            val = og_val.copy()
            for key in numbers:
                if key in val[1]:
                    changed += 1
                    val[1] = val[1].replace(key, str(numbers[key]))
                    if changed == 2:
                        break
            if changed == 2:
                not_found.remove(og_val)
                if 'x' not in val[1]:
                    val[1] = str(eval(val[1]))
                numbers[val[0]] = f'({val[1]})'
 
    x = Symbol('x')
    
    return int(solve(eval(numbers['root']), x)[0])

    
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

