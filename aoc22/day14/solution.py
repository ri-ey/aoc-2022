import os
import sys
import time
import json
import numpy as np
import matplotlib.pyplot as plt

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils

def add_sand(cave, source = [0, 500]):
    sand_pos = source
    new_sand_pos = None
    try:
        while new_sand_pos != sand_pos:
            if new_sand_pos is not None:
                sand_pos = new_sand_pos
            if cave[sand_pos[0] + 1, sand_pos[1]] == 0:
                new_sand_pos = [sand_pos[0] + 1, sand_pos[1]]
            elif cave[sand_pos[0] + 1, sand_pos[1]] in [1, -1] and cave[sand_pos[0] + 1, sand_pos[1] - 1] == 0:
                new_sand_pos = [sand_pos[0] + 1, sand_pos[1] - 1]
            elif cave[sand_pos[0] + 1, sand_pos[1]] in [1, -1] and cave[sand_pos[0] + 1, sand_pos[1] + 1] == 0:
                new_sand_pos = [sand_pos[0] + 1, sand_pos[1] + 1]
            elif cave[sand_pos[0] + 1, sand_pos[1]] in [1, -1] and cave[sand_pos[0] + 1, sand_pos[1] + 1] != 0 and cave[sand_pos[0] + 1, sand_pos[1] - 1] != 0:
                return sand_pos
            else:
                return new_sand_pos
    except IndexError:
        return -1
    return new_sand_pos

def solution_part_1():
    data = utils.read_input(script_path,0)
    data = data.split('\n')
    cave = np.zeros((200, 600))
    for cmd in data:
        cmd = cmd.split(' -> ')
        n_scans = len(cmd)
        for i in range(n_scans - 1):
            draw_from = [int(k) for k in cmd[i].split(',')]
            draw_to   = [int(k) for k in cmd[i + 1].split(',')]
            draw_x = sorted([draw_from[1], draw_to[1]])
            draw_y = sorted([draw_from[0], draw_to[0]])
            cave[draw_x[0]:draw_x[1] + 1, draw_y[0]:draw_y[1] + 1] = 1
    temp_cave = None
    while not np.array_equal(temp_cave, cave):
        temp_cave = cave.copy()
        new_sand_pos = add_sand(cave)
        if new_sand_pos == -1:
            return (cave == -1).sum()
        else:
            cave[new_sand_pos[0], new_sand_pos[1]] = -1
        if new_sand_pos == [0,500]:
            return (cave == -1).sum()
    return (cave == -1).sum()

    
def solution_part_2():
    data = utils.read_input(script_path,0)
    data = data.split('\n')
    cave = np.zeros((200, 1000))
    max_h = 0
    for cmd in data:
        cmd = cmd.split(' -> ')
        n_scans = len(cmd)
        for i in range(n_scans - 1):
            draw_from = [int(k) for k in cmd[i].split(',')]
            draw_to   = [int(k) for k in cmd[i + 1].split(',')]
            draw_x = sorted([draw_from[1], draw_to[1]])
            draw_y = sorted([draw_from[0], draw_to[0]])
            max_h = max(max_h, max(draw_x))
            cave[draw_x[0]:draw_x[1] + 1, draw_y[0]:draw_y[1] + 1] = 1
    floor_coords = max_h + 2

    cave[floor_coords] = 1
    
    temp_cave = None
    while not np.array_equal(temp_cave, cave):
        temp_cave = cave.copy()
        new_sand_pos = add_sand(cave)
        if new_sand_pos == -1:
            return (cave == -1).sum()
        else:
            cave[new_sand_pos[0], new_sand_pos[1]] = -1
        if new_sand_pos == [0,500]:
            return (cave == -1).sum()

    return (cave == -1).sum()

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

