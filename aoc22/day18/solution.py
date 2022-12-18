import os
import sys
import time
import json
import numpy as np
import re
from collections import deque

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils

def parse_data(data):
    data = data.split('\n')
    max_coord = 0
    for idx in range(len(data)):
        coords = list(map(int, re.findall('-?\d+',data[idx])))
        max_coord = max(max_coord, max(coords))
        data[idx] = coords
    return data, max_coord    

def get_neigh_faces(coords):
    neigh_faces = []
    for delta in [(0,0,1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
        neigh = tuple([coords[0] + delta[0], coords[1] + delta[1], coords[2] + delta[2]])
        neigh_faces.append(neigh)
    return neigh_faces

def solution_part_1():
    data = utils.read_input(script_path,0)
    data, lim = parse_data(data)
    lim = lim + 4
    matrix = np.zeros((lim, lim, lim))
    for lava in data:
        matrix[tuple(lava)] = 1
    
    count = 0
    for lava in data:
        neighs = get_neigh_faces(lava)
        for neigh in neighs:
            if matrix[neigh] == 0:
                count += 1
    return count
    
def flood_fill_matrix(matrix, start = (0,0,0), max_coord = 24):
    to_do = deque()
    to_do.append(start)
    matrix[start] = 0
    while to_do:
        doing = to_do.popleft()
        neighs =  get_neigh_faces(doing)
        for neigh in neighs:
            if matrix[neigh] == -1:
                matrix[neigh] = 0
                to_do.append(neigh)
    return matrix
        
    
def solution_part_2():
    data = utils.read_input(script_path,0)
    data, lim = parse_data(data)
    lim = lim + 4
    matrix = np.zeros((lim, lim, lim))
    matrix = matrix - 1
    for lava in data:
        matrix[tuple(lava)] = 1
    count = 0

    matrix = flood_fill_matrix(matrix)
    for lava in data:
        neighs = get_neigh_faces(lava)
        for neigh in neighs:
            if matrix[neigh] == 0:
                count += 1
    return count

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

