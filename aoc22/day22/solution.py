import os
import sys
import time
import json
import re

import numpy as np
try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils

def parse_input(data):
    maze, instruction = data.split('\n\n')
    instruction = 'R' + instruction
    maze = maze.split('\n')
    rows= len(maze)
    cols = max([len(k) for k in maze])
    canvas = np.empty((rows, cols)).astype(str)
    canvas.fill(' ') 
    for i in range(rows):
        canvas[i,:len(maze[i])] = list(maze[i])
    move_units = re.findall('\d+', instruction)
    move_directions = re.findall('[A-Z]', instruction)
    return canvas, move_units, move_directions
    
def rotate(coords, way):
    if way == 'L':
        coords = [-coords[1],coords[0]]
    else:
        coords = [coords[1],-coords[0]]
    return np.array(coords)


def find_next_coords(canvas, pos, delta):
    new_pos = pos + delta
    rows, cols =  canvas.shape
    stop = False

    if new_pos[0] >= rows or new_pos[0]<0:
        if new_pos[0] < 0:
            tmp_new_pos = np.where(canvas[:,new_pos[1]] != ' ')[0][-1]
            new_pos = np.array([tmp_new_pos, new_pos[1]])
        else:
            tmp_new_pos = np.where(canvas[:,new_pos[1]] != ' ')[0][0]
            new_pos = np.array([tmp_new_pos, new_pos[1]])

    if new_pos[1] >= cols or new_pos[1]<0:
        if new_pos[1] < 0:
            tmp_new_pos = np.where(canvas[new_pos[0], :] != ' ')[0][-1]
            new_pos = np.array([new_pos[0], tmp_new_pos])
        else:
            tmp_new_pos = np.where(canvas[new_pos[0], :] != ' ')[0][0]
            new_pos = np.array([new_pos[0], tmp_new_pos])
    
    new_val = canvas[new_pos[0], new_pos[1]]

    if new_val == ' ':
        if delta[0] == 1:
            new_pos[0] = np.where(canvas[:,new_pos[1]] != ' ')[0][0]
        elif delta[0] == -1:
            new_pos[0] = np.where(canvas[:,new_pos[1]] != ' ')[0][-1]
        elif delta[1] == 1:
            new_pos[1] = np.where(canvas[new_pos[0], :] != ' ')[0][0]
        elif delta[1] == -1:
            new_pos[1] = np.where(canvas[new_pos[0], :] != ' ')[0][-1]
         
    new_val = canvas[new_pos[0], new_pos[1]]

    if new_val == '#':
        stop = True
        return pos, stop
    else:
        return new_pos, stop

def solution_part_1():
    data = utils.read_input(script_path,0)
    canvas, move_units, move_directions = parse_input(data)
    delta_direction = [-1, 0]
    position = np.array([0, np.where(canvas[0] == '.')[0][0]])
    for units, direction in zip(move_units, move_directions):
        delta_direction = rotate(delta_direction, direction)
        for _ in range(int(units)):
            new_pos, stop = find_next_coords(canvas, position, delta_direction)
            position = new_pos            
            if stop:
                break
    if delta_direction[1] == 1:
        factor = 0
    elif delta_direction[1] == -1:
        factor = 3
    elif delta_direction[0] == 1:
        factor = 2
    elif delta_direction[0] == -1:
        factor = 1
    position = position + 1

    return 1000*position[0] + 4*position[1] + factor


def find_next_coords_2(canvas, pos, delta):
    direction = delta.copy()
    new_pos = pos + delta
    rows, cols =  canvas.shape
    stop = False

    if new_pos[0] >= rows or new_pos[0] < 0:
        if new_pos[0] < 0:
            if new_pos[1] <= 99:
                new_pos = np.array([100 + new_pos[1], 0])
                direction = np.array([0,1])
            else:
                new_pos = np.array([199, new_pos[1] - 100])
                direction = np.array([-1,0])
        else:
            new_pos = np.array([0, 100 + new_pos[1]])
            direction = np.array([1,0])
        new_val = canvas[new_pos[0], new_pos[1]]
        if new_val == '#':
            stop = True
            return pos, stop, delta
        else:
            return new_pos, stop, direction
    if new_pos[1] >= cols or new_pos[1] < 0:
        if new_pos[1] < 0:
            if 100 <= new_pos[0] <= 149:
                new_pos = np.array([49 - (new_pos[0] - 100), 50])
                direction = np.array([0,1])
            else:
                new_pos = np.array([0, 50 + (new_pos[0] - 150)])
                direction = np.array([1,0])
        else:
            new_pos = np.array([99 + (50 - new_pos[0]), 99])
            direction = np.array([0,-1]) 

        new_val = canvas[new_pos[0], new_pos[1]]
        if new_val == '#':
            stop = True
            return pos, stop, delta
        else:
            return new_pos, stop, direction

    new_val = canvas[new_pos[0], new_pos[1]]

    if new_val == ' ':
        if direction[1] == 1:
            if new_pos[0] <=99:
                new_pos = np.array([49, 100 + (new_pos[0] - 50)])
                direction = np.array([-1,0])
            elif new_pos[0] <= 149:
                new_pos = np.array([49 - (new_pos[0] - 100), 149])
                direction = np.array([0,-1])
            else:
                new_pos = np.array([149, 50 + (new_pos[0] - 150)])
                direction = np.array([-1,0])
        elif direction[1] == -1:
            if new_pos[0] <=49:
                new_pos = np.array([100 + (49 - new_pos[0]), 0])
                direction = np.array([0,1])
            else:
                new_pos = np.array([100, new_pos[0] - 50])
                direction = np.array([1,0])
        elif direction[0] == 1:
            if new_pos[1] <=99:
                new_pos = np.array([150 + (new_pos[1] - 50), 49])
                direction = np.array([0,-1])
            else:
                new_pos = np.array([50 + (new_pos[1] - 100) ,99])
                direction = np.array([0,-1])
        elif direction[0] == -1:
            new_pos = np.array([50 + new_pos[1], 50])
            direction = np.array([0,1])
    
    new_val = canvas[new_pos[0], new_pos[1]]

    if new_val == '#':
        stop = True
        return pos, stop, delta
    else:
        return new_pos, stop, direction

def solution_part_2():
    data = utils.read_input(script_path,0)
    canvas, move_units, move_directions = parse_input(data)
    delta_direction = [-1, 0]
    position = np.array([0, np.where(canvas[0] == '.')[0][0]])
    last = (move_units[-1], move_directions[-1])
    for units, direction in zip(move_units, move_directions):
        save = False
        delta_direction = rotate(delta_direction, direction)
        if (units, direction) == last:
            save = True
        for idx in range(int(units)):
            if idx == int(units) -1 and save:
                save_delta_direction = delta_direction.copy()
            new_pos, stop, delta_direction = find_next_coords_2(canvas, position, delta_direction)
            position = new_pos
            if stop:
                break
    if save_delta_direction[1] == 1:
        factor = 0
    elif save_delta_direction[0] == -1:
        factor = 1
    elif save_delta_direction[0] == 1:
        factor = 2
    elif save_delta_direction[1] == -1:
        factor = 3
    position = position + 1
    return 1000*position[0] + 4*position[1] + factor

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