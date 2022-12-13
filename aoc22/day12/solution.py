import os
import sys
import time

try:
    script_path = os.path.dirname(__file__)
except NameError:
    script_path = os.getcwd()
sys.dont_write_bytecode = True
lib_path = (os.path.dirname(script_path) + "\\utils").replace('\\', '/')
sys.path.insert(0, lib_path)

import utils
def decode_input(data, reverse = False):
    data = [list(row) for row in data]
    rows, cols = len(data), len(data[0]) 
    for i in range(rows):
        for j in range(cols):
            if data[i][j] in ['S', 'E']:
                if  data[i][j] == 'S':
                    start = [i,j]

                    data[i][j] = (ord('a') - [96, 123][reverse])*[1, -1][reverse]
                else:
                    end = [i,j]  
                            
                    data[i][j] = (ord('z') - [96, 123][reverse])*[1, -1][reverse]
            else:
                data[i][j] = (ord(data[i][j]) - [96, 123][reverse])*[1, -1][reverse]
    return data, start, end

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = None
 
    def printSolution(self, dist, end):
        return dist[end]
 
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
    def dijkstra(self, src, end):
 
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
 
        return self.printSolution(dist, end), dist
 
def coords_to_idx(rows, cols, i, j):
    return (cols)*(i) + j
    
def solution_part_1():
    data = utils.read_input(script_path, 0)
    data = data.split('\n')
    data, start, end = decode_input(data)
    rows, cols = len(data), len(data[0]) 
    distance_mat = [[0]*rows*cols for _ in range(rows*cols)]#
    for i in range(rows):
        for j in range(cols):
            neighs = [[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
            out_neighs = neighs.copy()
            for neigh in neighs:
                if (neigh[0] < 0) or (neigh[0] >= rows) or (neigh[1] < 0) or (neigh[1] >= cols):
                    out_neighs.remove(neigh)
            neighs = out_neighs
            for neigh in neighs:
                current_idx = coords_to_idx(rows, cols, i, j)
                current_h = data[i][j]
                neigh_h = data[neigh[0]][neigh[1]]
                neigh_idx = coords_to_idx(rows, cols, neigh[0], neigh[1])
                if neigh_h - current_h <= 1:
                    distance_mat[current_idx][neigh_idx] = 1
    g = Graph(rows*cols)
    g.graph = distance_mat
    source_idx = coords_to_idx(rows, cols, start[0], start[1])
    end_idx = coords_to_idx(rows, cols, end[0], end[1])

    solution, _ = g.dijkstra(source_idx, end_idx)
    return solution


    
def solution_part_2():
    data = utils.read_input(script_path, 0)
    data = data.split('\n')
    data, start, end = decode_input(data, True)
    rows, cols = len(data), len(data[0]) 
    distance_mat = [[0]*rows*cols for _ in range(rows*cols)]
    possible_starts = []
    for i in range(rows):
        for j in range(cols):
            neighs = [[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
            out_neighs = neighs.copy()
            for neigh in neighs:
                if (neigh[0] < 0) or (neigh[0] >= rows) or (neigh[1] < 0) or (neigh[1] >= cols):
                    out_neighs.remove(neigh)
            neighs = out_neighs
            for neigh in neighs:
                current_idx = coords_to_idx(rows, cols, i, j)
                current_h = data[i][j]
                neigh_h = data[neigh[0]][neigh[1]]
                neigh_idx = coords_to_idx(rows, cols, neigh[0], neigh[1])
                if neigh_h - current_h <= 1:
                    distance_mat[current_idx][neigh_idx] = 1
            if current_h == 26:
                possible_starts.append(current_idx)
    g = Graph(rows*cols)
    g.graph = distance_mat
    source_idx = coords_to_idx(rows, cols, start[0], start[1])
    end_idx = coords_to_idx(rows, cols, end[0], end[1])

    solution, all_distances = g.dijkstra(end_idx, source_idx)
    min_distance = 1e7
    for start in possible_starts:
        if all_distances[start] < min_distance:
            min_distance = all_distances[start] 
    return min_distance

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

