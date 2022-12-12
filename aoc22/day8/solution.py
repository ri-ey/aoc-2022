import os
import sys
import time
import math
try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils

def is_visible(data, row, col):
    rows, cols = len(data), len(data[0])
    tree_h = data[row][col]
    directions = [[-1, 0], [1,0], [0,1], [0,-1]]
    for direction in directions:
        visible = True
        temp_row, temp_col = row, col
        while temp_row < rows - 1 and temp_col < cols - 1 and temp_row > 0 and temp_col > 0:
            temp_row += direction[0]
            temp_col += direction[1]
            if data[temp_row][temp_col] >= tree_h:
                visible = False
                break
        if visible:
            return 1
    return 0

def solution_part_1():
    data = utils.read_input(script_path)
    data = data.split('\n')
    data = [[int(k) for k in row] for row in data]
    rows, cols = len(data), len(data[0])
    visible_count = 2*rows + 2*cols - 4 
    for i in range(1, rows - 1):
        for j in range(1,cols - 1):
            visible_count += is_visible(data, i, j)
    return visible_count


def scenic_score_calc(data, row, col):
    rows, cols = len(data), len(data[0])
    tree_h = data[row][col]
    directions = [[-1, 0], [1,0], [0,1], [0,-1]]
    scores = []
    for direction in directions:
        temp_row, temp_col = row, col
        temp_score = 0
        while temp_row < rows - 1 and temp_col < cols - 1 and temp_row > 0 and temp_col > 0:
            temp_row += direction[0]
            temp_col += direction[1]
            if data[temp_row][temp_col] < tree_h:
                temp_score += 1
            if data[temp_row][temp_col] >= tree_h:
                temp_score += 1
                break
        scores.append(temp_score)
    return math.prod(scores)
    
def solution_part_2():
    data = utils.read_input(script_path)
    data = data.split('\n')
    data = [[int(k) for k in row] for row in data]
    rows, cols = len(data), len(data[0])
    max_score = 0
    for i in range(1, rows - 1):
        for j in range(1,cols - 1):
            max_score = max(max_score, scenic_score_calc(data, i, j))
    return max_score

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

