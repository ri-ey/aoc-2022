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
    data = data.split('\n')
    set_dirs = set()
    for idx, command in enumerate(data):
        if '$ cd' in command and '..' not in command:
            temp_dir = command.split()[-1]
            while temp_dir in set_dirs:
                temp_dir = temp_dir + '1'
            
            data[idx] = data[idx].replace(command.split()[-1], temp_dir)
            set_dirs.add(temp_dir)
    active_dirs = []
    storage = {}
    max_size = 100000
    for command in data:
        if '$' in command:
            if 'cd ..' in command:
                active_dirs.pop()
            elif 'cd' in command:
                directory = command.split()[-1]
                active_dirs.append(directory)
                if directory not in storage:
                    storage[directory] = 0
        else:
            ls_res = command.split()
            if ls_res[0].isnumeric():
                for active_dir in active_dirs:
                    storage[active_dir] += int(ls_res[0])
    res = 0
    for key in storage:
        if storage[key] <= max_size:
            res += storage[key]
    return res

    
def solution_part_2():
    data = utils.read_input(script_path)
    data = data.split('\n')
    set_dirs = set()
    for idx, command in enumerate(data):
        if '$ cd' in command and '..' not in command:
            temp_dir = command.split()[-1]
            while temp_dir in set_dirs:
                temp_dir = temp_dir + '1'
            
            data[idx] = data[idx].replace(command.split()[-1], temp_dir)
            set_dirs.add(temp_dir)
    active_dirs = []
    storage = {}
    for command in data:
        if '$' in command:
            if 'cd ..' in command:
                active_dirs.pop()
            elif 'cd' in command:
                directory = command.split()[-1]
                active_dirs.append(directory)
                if directory not in storage:
                    storage[directory] = 0
        else:
            ls_res = command.split()
            if ls_res[0].isnumeric():
                for active_dir in active_dirs:
                    storage[active_dir] += int(ls_res[0])
    space_available = 70000000 - storage['/']
    needed_space = 30000000 - space_available
    smallest_dir = ''
    for key in storage:
        if smallest_dir == '':
            smallest_dir = key
        else:
            if storage[key] >= needed_space:
                if storage[smallest_dir] > storage[key]:
                    smallest_dir = key 
    return storage[smallest_dir]

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

