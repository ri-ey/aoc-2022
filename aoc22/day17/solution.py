import os
import sys
import time
import json
from itertools import zip_longest
import numpy as np

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils
def falling_rock(i, height):
    options = list('-+LIS')
    curr = options[i]
    if curr == '-':
        shape = np.array([[height, 2], [height, 3], [height, 4], [height, 5]])
        left = np.array([[height, 2]])
        right = np.array([[height, 5]])
    elif curr == '+':
        shape = np.array([[height + 1, 2], [height, 3], [height + 1, 3], [height + 2, 3], [height+ 1, 4]])
        left = np.array([[height + 1, 2]])
        right = np.array([[height + 1, 4]])
    elif curr == 'L':
        shape = np.array([[height, 2], [height, 3], [height, 4], [height + 1, 4], [height+ 2, 4]])
        left = np.array([[height, 2]])
        right = np.array([[height, 4]])
    elif curr == 'I':
        shape = np.array([[height, 2], [height + 1, 2], [height + 2, 2], [height + 3, 2]])
        left = np.array([[height, 2]])
        right = np.array([[height, 2]])
    elif curr == 'S':
        shape = np.array([[height, 2], [height + 1, 2], [height, 3], [height + 1, 3]])
        left = np.array([[height, 2]])
        right = np.array([[height, 3]])
    return shape, left, right

def parse_input(data):
    data = list(data.split('\n')[0])
    for i in range(len(data)):
        data[i] = [-1, 1][data[i] == '>']
    return data

def solution_part_1():
    data = utils.read_input(script_path,0)
    gas = parse_input(data)
    gas_idx = 0
    gas_n = len(gas)
    max_rocks = 2022
    cave = np.zeros((max_rocks * 4, 7))
    cave[0,:] = 1
    max_h = 0
    for num_rocks in range(max_rocks):
        idx = num_rocks%5
        falling_rock_coords, left_edge, right_edge = falling_rock(idx, max_h + 4)
        while True:
            stop = False
            movement = np.array([0, gas[gas_idx]])
            if (left_edge + movement)[0,1] < 0 or (right_edge + movement)[0,1] > 6:
                movement = np.array([0,0])

            for rock_piece in falling_rock_coords:
                tmp = rock_piece + movement
                if cave[tmp[0], tmp[1]] == 1:
                    movement = np.array([0,0])
            gas_idx += 1 
            gas_idx  = gas_idx%gas_n  
            falling_rock_coords = falling_rock_coords + movement
            left_edge = left_edge + movement
            right_edge = right_edge + movement
            movement = np.array([-1,0])
            for rock_piece in falling_rock_coords:
                if cave[rock_piece[0] - 1, rock_piece[1]] == 1:
                    stop = True
                    break
            if stop:
                break
            falling_rock_coords = falling_rock_coords + movement
            left_edge = left_edge + movement
            right_edge = right_edge + movement
        for rock_piece in falling_rock_coords:
            cave[rock_piece[0], rock_piece[1]] = 1
        max_h = max(max_h, max(falling_rock_coords[:,0]))    
    return max_h

    
def solution_part_2():
    data = utils.read_input(script_path,0)
    gas = parse_input(data)
    gas_idx = 0
    gas_n = len(gas)
    max_rocks = 1000000000000
    cave = np.zeros((max_rocks//10000 * 4, 7))
    cave[0,:] = 1
    max_h = 0
    states = {}
    skip = True
    for num_rocks in range(max_rocks):
        idx = num_rocks%5
        falling_rock_coords, left_edge, right_edge = falling_rock(idx, max_h + 4)
        key = idx, gas_idx     
        if key in states:
            old_num_rocks, old_max_h = states[key]
            cycle = old_num_rocks - num_rocks
            num_cycles, left_to_simulate = (max_rocks-num_rocks)//(cycle), (max_rocks-num_rocks)%(cycle)
            print(num_cycles, left_to_simulate, num_rocks)
            if left_to_simulate == 0: 
                return (int(max_h + (old_max_h - max_h)*num_cycles)) 
        else: states[key] = num_rocks, max_h

        while True:
            stop = False
            movement = np.array([0, gas[gas_idx]])
            if (left_edge + movement)[0,1] < 0 or (right_edge + movement)[0,1] > 6:
                movement = np.array([0,0])

            for rock_piece in falling_rock_coords:
                tmp = rock_piece + movement
                if cave[tmp[0], tmp[1]] == 1:
                    movement = np.array([0,0])
            falling_rock_coords = falling_rock_coords + movement
            left_edge = left_edge + movement
            right_edge = right_edge + movement
            movement = np.array([-1,0])
            for rock_piece in falling_rock_coords:
                if cave[rock_piece[0] - 1, rock_piece[1]] == 1:
                    stop = True
                    break
            gas_idx += 1
            gas_idx = gas_idx%gas_n 
            if stop:
                break
            falling_rock_coords = falling_rock_coords + movement
            left_edge = left_edge + movement
            right_edge = right_edge + movement
        
        for rock_piece in falling_rock_coords:
            cave[rock_piece[0], rock_piece[1]] = 1
            
        max_h = max(max_h, max(falling_rock_coords[:,0]))    

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

