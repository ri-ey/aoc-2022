import os
import sys
import time
import json
import numpy as np

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils


def check_move(x, y, canvas, directions):
    for way in directions:
        way = way + np.array([x, y])
        cand = [canvas[k[0], k[1]] for k in way]
        if sum(cand) > 0:
            continue
        else:
            return tuple(way[1])
    return tuple([x, y])

def solution_part_1():
    data = utils.read_input(script_path,0)
    data = data.split('\n')
    data = [list(map(int, k.replace('.','0').replace('#', '1'))) for k in data]
    rows, cols = len(data) + 22, len(data[0]) + 22 
    canvas = np.zeros((rows, cols))
    canvas[11:-11,11:-11] = data
    rounds = 10
    directions = [np.array([[-1,-1],[-1,0],[-1,1]]), np.array([[1,-1],[1,0],[1,1]]), np.array([[1,-1],[0,-1],[-1,-1]]), np.array([[1,1],[0,1],[-1,1]])]
    for _ in range(rounds):
        elfs_x, elfs_y = np.where(canvas == 1)
        moves = {}
        ignore = []
        for e_x, e_y in zip(elfs_x, elfs_y):
            if canvas[e_x - 1:e_x +2, e_y -1 :e_y + 2].sum() == 1:
                continue
            else:
                new_pos = check_move(e_x, e_y, canvas, directions)
                if new_pos not in ignore:
                    if new_pos[0] != e_x or new_pos[1] != e_y:
                        if new_pos in moves:
                            moves.pop(new_pos)
                            ignore.append(new_pos)
                        else:
                            moves[new_pos] = (e_x, e_y)
        for new_pos, old_pos in moves.items():
                canvas[old_pos[0], old_pos[1]] = 0
                canvas[new_pos[0], new_pos[1]] = 1 
        directions.append(directions.pop(0))
    
    elfs_x, elfs_y = np.where(canvas == 1)
    min_x, max_x, min_y, max_y = min(elfs_x), max(elfs_x), min(elfs_y), max(elfs_y)
    res = (canvas[min_x:max_x + 1, min_y:max_y+1] == 0).sum()
    return res

    
def solution_part_2():
    data = utils.read_input(script_path,0)
    data = data.split('\n')
    data = [list(map(int, k.replace('.','0').replace('#', '1'))) for k in data]
    val = 100
    rows, cols = len(data) + val, len(data[0]) + val 
    canvas = np.zeros((rows, cols))
    canvas[val//2:-val//2,val//2:-val//2] = data
    rounds = 100000
    canvas_at_4 = []
    directions = [np.array([[-1,-1],[-1,0],[-1,1]]), np.array([[1,-1],[1,0],[1,1]]), np.array([[1,-1],[0,-1],[-1,-1]]), np.array([[1,1],[0,1],[-1,1]])]
    for idx in range(rounds):
        elfs_x, elfs_y = np.where(canvas == 1)
        moves = {}
        ignore = []
        for e_x, e_y in zip(elfs_x, elfs_y):
            if canvas[e_x - 1:e_x +2, e_y -1 :e_y + 2].sum() == 1:
                continue
            else:
                new_pos = check_move(e_x, e_y, canvas, directions)
                if new_pos not in ignore:
                    if new_pos[0] != e_x or new_pos[1] != e_y:
                        if new_pos in moves:
                            moves.pop(new_pos)
                            ignore.append(new_pos)
                        else:
                            moves[new_pos] = (e_x, e_y)
        for new_pos, old_pos in moves.items():
                canvas[old_pos[0], old_pos[1]] = 0
                canvas[new_pos[0], new_pos[1]] = 1 
        directions.append(directions.pop(0))
        if len(canvas_at_4) < 4:
            canvas_at_4.append(canvas.copy())
        else:
            canvas_at_4.append(canvas.copy())
            check = canvas_at_4.pop(0)
            if (check == canvas).all():
                return idx - 2
    
    elfs_x, elfs_y = np.where(canvas == 1)
    min_x, max_x, min_y, max_y = min(elfs_x), max(elfs_x), min(elfs_y), max(elfs_y)
    res = (canvas[min_x:max_x + 1, min_y:max_y+1] == 0).sum()
    return res

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

