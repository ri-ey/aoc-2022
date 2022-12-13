import os
import sys
import time
import json
from itertools import zip_longest

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils


def compare_list(packet_a, packet_b):
    # print(packet_a,  '------', packet_b)
    for left, right in zip_longest(packet_a, packet_b):
        if isinstance(left,int) and isinstance(right, int):
            if left > right:
                return 0
            elif left < right:
                return 1
        elif (isinstance(left,list) and isinstance(right, list)):
            if compare_list(left, right) is None:
                continue
            else:
                return  compare_list(left, right)
        elif (isinstance(left,int) and isinstance(right, list)):
            if compare_list([left], right) is None:
                continue
            else:
                return  compare_list([left], right)
        elif (isinstance(left,list) and isinstance(right, int)):
            if compare_list(left, [right]) is None:
                continue
            else:
                return  compare_list(left, [right])
        elif left is None:
            return 1
        elif right is None:
            return 0

def bubble_sort(data):
    n = len(data)
    for i in range(n-1):
        changed = False
        for j in range(0, n-i-1):
            if not compare_list(data[j],data[j + 1]):
                changed = True
                data[j], data[j + 1] = data[j + 1], data[j]
        if not changed:
            return data

def solution_part_1():
    data = utils.read_input(script_path,0)
    data = data.split('\n\n')
    solution = 0
    for idx, values  in enumerate(data):
        packet_a, packet_b = [json.loads(k) for k in values.split('\n')]
        if compare_list(packet_a, packet_b):
            solution += idx + 1 
    return solution

    
def solution_part_2():
    data = utils.read_input(script_path,0)
    data = data.split('\n\n')
    packet_list = [[[2]], [[6]]]
    sorted_packer = []
    for values  in data:
        packet_a, packet_b = [json.loads(k) for k in values.split('\n')]
        packet_list.append(packet_a)
        packet_list.append(packet_b)
    res = bubble_sort(packet_list)
    return (res.index([[2]]) + 1) * (res.index([[6]]) + 1)

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

