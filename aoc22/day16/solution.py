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


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = None
 
    def minDistance(self, dist, sptSet):
        min_d = 1e7
        for v in range(self.V):
            if dist[v] < min_d and sptSet[v] == False:
                min_d = dist[v]
                min_index = v
        try:
            return min_index
        except:
            return None

    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            if u == None:
                continue
            sptSet[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        return dist

def parse_input(data):
    data = data.split('\n')
    nodes = {}
    for row in data:
        tmp_nodes = re.findall('[A-Z][A-Z]', row)
        flow = int(re.findall('\d+', row)[0])
        nodes[tmp_nodes[0]] = [flow, tmp_nodes[1:]]
    return nodes



def find_most_pressure(nodes_w_flow_distances, nodes_to_idx, nodes, current = 'AA', time = 30, visited = {}, targets = {}):
    visited = visited | {current}

    targets = targets - visited
    max_pressure = 0
    for target in targets:
        time_left = time - nodes_w_flow_distances[current][nodes_to_idx[target]] - 1
        if time_left > 0:
            flow = nodes[target][0] * time_left
            flow += find_most_pressure(nodes_w_flow_distances, nodes_to_idx, nodes, target, time_left, visited, targets)
            max_pressure = max(flow, max_pressure)
        if len(targets) == 0:
            return max_pressure
    return int(max_pressure)

def solution_part_1():
    data = utils.read_input(script_path,0)
    nodes = parse_input(data)
    nodes_to_idx = {}
    count = 0
    for nd in nodes:
        nodes_to_idx[nd] = count
        count+=1
    matrix = np.zeros((count, count))
    nodes_w_flow = []
    nodes_w_flow_distances = {}
    for nd in nodes:
        if nodes[nd][0] > 0 or nd == 'AA':
            nodes_w_flow.append(nd)
        for neigh in nodes[nd][1]:
            matrix[nodes_to_idx[nd], nodes_to_idx[neigh]] = 1
    g = Graph(count)
    g.graph = matrix
    for nd in nodes_w_flow:
        distances = g.dijkstra(nodes_to_idx[nd])
        nodes_w_flow_distances[nd] = distances
    targets = set(nodes_w_flow_distances.keys())
    return find_most_pressure(nodes_w_flow_distances, nodes_to_idx, nodes, current = 'AA', time = 30, visited = set(), targets = targets)


def part_2(targets, nodes_w_flow_distances, nodes_to_idx, nodes):
    best_26_mins_paths = {}
    og_targets = targets.copy()
    def compute_save_paths(targets, current="AA", pressure_now=0, time=26, visited=set()):
        visited = visited | {current}
        targets = targets - visited

        torecord = frozenset(visited - {"AA"})
        if torecord in best_26_mins_paths:
            best_26_mins_paths[torecord] = max(best_26_mins_paths[torecord], pressure_now)
        else:
            best_26_mins_paths[torecord] = pressure_now

        best_pressure = 0
        for target in targets:
            time_left = time - nodes_w_flow_distances[current][nodes_to_idx[target]] - 1
            if time_left > 0:
                new_pressure = nodes[target][0] * time_left
                new_pressure += compute_save_paths(targets, target, pressure_now + new_pressure, time_left, visited)
                best_pressure = max(new_pressure, best_pressure)
        return best_pressure 
    compute_save_paths(targets)

    og_targets = frozenset(og_targets - {"AA"})

    def compute_remaining_nodes_paths(current = og_targets):
        if current not in best_26_mins_paths:
            best_pressure = 0
            for node in current:
                subset = current-{node}
                new_pressure = compute_remaining_nodes_paths(subset)
                best_pressure = max(best_pressure, new_pressure)
            best_26_mins_paths[current] = best_pressure
        return best_26_mins_paths[current]
    
    compute_remaining_nodes_paths()

    overall_best = 0
    for path_1 in best_26_mins_paths:
        path_2 = og_targets - {"AA"} - path_1
        overall_best = max(overall_best, best_26_mins_paths[path_1] + best_26_mins_paths[path_2])
    return int(overall_best)

def solution_part_2():
    data = utils.read_input(script_path,0)
    nodes = parse_input(data)
    nodes_to_idx = {}
    count = 0
    for nd in nodes:
        nodes_to_idx[nd] = count
        count+=1
    matrix = np.zeros((count, count))
    nodes_w_flow = []
    nodes_w_flow_distances = {}
    for nd in nodes:
        if nodes[nd][0] > 0 or nd == 'AA':
            nodes_w_flow.append(nd)
        for neigh in nodes[nd][1]:
            matrix[nodes_to_idx[nd], nodes_to_idx[neigh]] = 1
    g = Graph(count)
    g.graph = matrix
    for nd in nodes_w_flow:
        distances = g.dijkstra(nodes_to_idx[nd])
        nodes_w_flow_distances[nd] = distances

    targets = set(nodes_w_flow_distances.keys())
    return part_2(targets, nodes_w_flow_distances, nodes_to_idx, nodes)





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

