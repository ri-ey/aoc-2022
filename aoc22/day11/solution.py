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

# Monkey 0:
#   Starting items: 64
#   Operation: new = old * 7
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3
class Monkey:
    def __init__(self, data):
        data = data.split('\n')
        self.monkey_num = int(data[0][-2])
        self.items = [int(k) for k in data[1].split(': ')[1].split(', ')]
        if '+' in data[2]:
            self.operation = ['+', int(data[2].split(' ')[-1])]
        elif 'old * old' in data[2]:
            self.operation = ['s']
        else:
            self.operation = ['*', int(data[2].split(' ')[-1])]
        self.div_factor = int(data[3].split(' ')[-1])
        self.throw = [int(data[5].split(' ')[-1]), int(data[4].split(' ')[-1])] 
        self.items_handled = 0
    
    def update_count(self):
        self.items_handled += 1
    

def solution_part_1():
    data = utils.read_input(script_path)
    data = data.split('\n\n')
    monkeys_list = []
    for mk in data:
        monkeys_list.append(Monkey(mk))
    rounds = 20
    for _ in range(rounds):
        for mk in monkeys_list:
            mk_items = mk.items
            while mk_items:
                item = mk.items.pop(0)
                mk.update_count()
                if mk.operation[0] == '+':
                    item = item + mk.operation[1]
                    item = item//3

                elif mk.operation[0] == 's':
                    item = item ** 2
                    item = item//3
                else:
                    item = item * mk.operation[1]
                    item = item//3
                mk_num_to_throw = mk.throw[item%mk.div_factor == 0]
                monkeys_list[mk_num_to_throw].items.append(item) 

    return math.prod(sorted([k.items_handled for k in monkeys_list])[-2:]) 

    
def solution_part_2():
    data = utils.read_input(script_path)
    data = data.split('\n\n')
    monkeys_list = []
    for mk in data:
        monkeys_list.append(Monkey(mk))
    max_div = math.prod([mk.div_factor for mk in monkeys_list])
    rounds = 10000 
    for idx in range(rounds):
        for mk in monkeys_list:
            mk_items = mk.items
            while mk_items:
                item = mk.items.pop(0)
                mk.update_count()
                if mk.operation[0] == '+':
                    item = item + mk.operation[1]

                elif mk.operation[0] == 's':
                    item = item ** 2
                else:
                    item = item * mk.operation[1]
                item = item%max_div
                mk_num_to_throw = mk.throw[item%mk.div_factor == 0]
    
                monkeys_list[mk_num_to_throw].items.append(item) 

    return math.prod(sorted([k.items_handled for k in monkeys_list])[-2:]) 

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

