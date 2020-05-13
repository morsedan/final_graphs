from util import Stack

# def island_counter(matrix):
#
#     vertices = {}
#
#     height = len(matrix)
#     width = len(matrix[0])
#
#     for ew_index in range(width):
#         for ns_index in range(height):
#             point = (ew_index, ns_index)
#             if matrix[ns_index][ew_index] > 0:
#                 vertices[point] = set()
#
#     for vert in vertices:
#         x, y = vert[0], vert[1]
#         if x > 0:
#             if matrix[y][x-1] > 0:
#                 vertices[vert].add((x-1,y))
#         if x < width-1:
#             if matrix[y][x+1] > 0:
#                 vertices[vert].add((x+1, y))
#         if y > 0:
#             if matrix[y-1][x] > 0:
#                 vertices[vert].add((x, y-1))
#         if y < height-1:
#             if matrix[y+1][x] > 0:
#                 vertices[vert].add((x, y+1))
#     for vertex in vertices:
#         print(vertex, vertices[vertex])
#     # print(vertices)
#     total = 0
#     removed = set()
#     vertices_copy = vertices.copy()
#     print(len(vertices_copy))
#     for vert in vertices:
#         # if vert in checked:
#         #     continue
#         # checked.add(vert)
#         for addition in vertices[vert]:
#         #     if addition in checked:
#         #         continue
#         #     checked.add(addition)
#             if addition in vertices_copy and vert not in removed:
#                 removed.add(addition)
#                 print("Before", addition, vert, vertices_copy)
#                 for item in vertices_copy[addition]:
#                     if item != vert and item in vertices_copy:
#                         del vertices_copy[item]
#                 del vertices_copy[addition]
#                 print("After", vertices_copy)
#                 total += 1
#     for vert in vertices_copy:
#         print(vert, vertices_copy[vert])
#     print(len(vertices_copy))
#     total = len(vertices_copy)
#     print("Total:", total)
#     # for ew_index in width:
#     #     for ns_index in height:
#     #         if ns_index > 0:
#     #             if ew_index > 0:
#
# """
# keep track of visited verticies
#
# go through the matrix of island data
# if we see a 1, and it's not visited
#     DFT or BFT
#         keep marking each visited vertex as visited
#     once done, add 1 to island count
# """
#
# def good_island_counter(matrix):
#     visited = set()
#     s = Stack()
#     count = 0
#
#     vertices = {}
#
#     height = len(matrix)
#     width = len(matrix[0])
#
#     for ew_index in range(width):
#         for ns_index in range(height):
#             point = (ew_index, ns_index)
#             if matrix[ns_index][ew_index] > 0:
#                 vertices[point] = set()
#
#     for vert in vertices:
#         x, y = vert[0], vert[1]
#         if x > 0:
#             if matrix[y][x - 1] > 0:
#                 vertices[vert].add((x - 1, y))
#         if x < width - 1:
#             if matrix[y][x + 1] > 0:
#                 vertices[vert].add((x + 1, y))
#         if y > 0:
#             if matrix[y - 1][x] > 0:
#                 vertices[vert].add((x, y - 1))
#         if y < height - 1:
#             if matrix[y + 1][x] > 0:
#                 vertices[vert].add((x, y + 1))
#
#
#     for row in matrix:
#         for item in row:
#             visited.add(item)
#
#             if matrix[item[0]][item[1]] > 0 and item not in visited:
#                 s.push(item)
#                 while s.size() > 0:
#                     for neighbor in vertices[item]:
#                         visited.add(neighbor)
#                         if vertices[neighbor] > 1 and neighbor not in visited:
#                             s.push(neighbor)
#                 count += 1
#     return count

def get_neighbors(current_vertex, matrix):
    neighbors = set()
    row = current_vertex[0]
    col = current_vertex[1]
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.add((row-1, col))
    if row < len(matrix)-1 and matrix[row + 1][col] == 1:
        neighbors.add((row + 1, col))
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.add((row, col-1))
    if col < len(matrix[row])-1 and matrix[row][col+1] == 1:
        neighbors.add((row, col+1))
    return neighbors

def dft(row_index, col_index, matrix, visited):
    neighbors_to_visit = Stack()
    neighbors_to_visit.push((row_index, col_index))

    while neighbors_to_visit.size() > 0:
        current_vertex = neighbors_to_visit.pop()
        if current_vertex not in visited:
            visited.add(current_vertex)
            for neighbor in get_neighbors(current_vertex, matrix):
                neighbors_to_visit.push(neighbor)
    return visited

def artem_island_count(matrix):
    visited = set()
    count = 0

    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            if (row_index, col_index) not in visited and matrix[row_index][col_index] == 1:
                visited = dft(row_index, col_index, matrix, visited)
                count += 1
    return count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(artem_island_count(islands))

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(artem_island_count(islands))