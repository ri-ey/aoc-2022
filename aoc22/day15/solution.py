import os
import sys
import time
import json
import re

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils
def manhattan_dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def merge_sectors(sec_list):
    sec_list = list(set(sec_list))
    new_sec = []
    while new_sec != sec_list:
        new_sec = sec_list.copy()
        for element in sec_list:
            for other in sec_list:
                if other != element and not isinstance(other, int) and element in sec_list:
                    if isinstance(element, int):
                        if other[0] <= element and other[1] >= element:
                            sec_list.remove(element)
                    else:
                        if other[0] - 1 <= element[0] <= other[1] - 1:
                            new = (other[0], max(element[1], other[1]))
                            sec_list.remove(other)
                            sec_list.remove(element)
                            sec_list.append(new)
                        elif other[0] - 1 <= element[1] <= other[1] - 1:
                            new = (min(element[0], other[0]), other[1])
                            sec_list.remove(other)
                            sec_list.remove(element)
                            sec_list.append(new)
    return sec_list


def solution_part_1():
    data = utils.read_input(script_path,0)
    data = data.split('\n')
    sensosrs = []
    beacons  = []
    no_bcn_coords = set()
    for cmd in data:
        xs = [(int(k.split('=')[1])) for k in re.findall('x=-?\d+',cmd)]
        ys = [(int(k.split('=')[1])) for k in re.findall('y=-?\d+',cmd)]
        snsr = [ys[0], xs[0]]
        beac = [ys[1], xs[1]]
        sensosrs.append(snsr)
        beacons.append(beac)

    row_to_check = 2000000
    for sns, bcn in zip(sensosrs, beacons):
        distance =  manhattan_dist(sns, bcn)
        for i in range(sns[0] - distance, sns[0] + distance + 1):
            if i == row_to_check:        
                for j in range(sns[1] - distance, sns[1] + distance + 1):
                    if manhattan_dist(sns, [i,j]) <= distance:
                        if [i,j] not in beacons:
                            no_bcn_coords.add((i,j))
    
    return len(no_bcn_coords)

    
def solution_part_2():
    data = utils.read_input(script_path,0)
    data = data.split('\n')
    sensosrs = []
    beacons  = []
    for cmd in data:
        xs = [(int(k.split('=')[1])) for k in re.findall('x=-?\d+',cmd)]
        ys = [(int(k.split('=')[1])) for k in re.findall('y=-?\d+',cmd)]
        snsr = [ys[0], xs[0]]
        beac = [ys[1], xs[1]]
        sensosrs.append(snsr)
        beacons.append(beac)

    coord_min, coord_max = 0, 4000000
    rows = [[] for _ in range(coord_max + 1)]
    for sns, bcn in zip(sensosrs, beacons):
        distance =  manhattan_dist(sns, bcn)
        lines_w     = [k for k in range(0, distance + 1)] + [k for k in range(0, distance)][::-1]
        lines_coord = [k for k in range(sns[0] - distance, sns[0] + distance + 1)]
        for lc, lw in zip(lines_coord, lines_w):
            if not coord_min <= lc <= coord_max:
                continue
            if lw == 0:
                rows[lc].append((sns[1]))
                rows[lc] = merge_sectors(rows[lc])
            else:
                rows[lc].append((sns[1]-lw, sns[1]+lw))
                rows[lc] = merge_sectors(rows[lc])
    for idx, rw in enumerate(rows):
        if len(rw) > 1:
            for k in rw:
                if k[0] < 0:
                    return idx + (k[1] + 1)*4000000
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

