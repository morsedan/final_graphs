"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            current_vertex = q.dequeue()
            print(current_vertex)
            if current_vertex not in visited:
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited:
                        q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            current_vertex = s.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited:
                        s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            current_path = q.dequeue()
            if current_path[-1] == destination_vertex:
                return current_path
            visited.add(current_path[-1])
            for neighbor in self.get_neighbors(current_path[-1]):
                new_path = current_path + [neighbor]
                q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            current_path = s.pop()
            ending_vertex = current_path[-1]
            if ending_vertex == destination_vertex:
                return current_path
            visited.add(ending_vertex)
            for neighbor in self.get_neighbors(ending_vertex):
                if neighbor not in visited:
                    new_path = current_path + [neighbor]
                    s.push(new_path)

    def bdfs_recursive(self, start_vert, taret_value, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(start_vert)

        path = path + [start_vert]

        if start_vert == taret_value:
            return path

        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                new_path = self.bdfs_recursive(child_vert, taret_value, visited, path)
                if new_path:
                    return new_path
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        return self.bdfs_recursive(starting_vertex, destination_vertex)
        # print(path)
        # if visited is None:
        #     visited = set()
        # if path is None:
        #     path = [starting_vertex]
        # ending_vertex = path[-1]
        # if ending_vertex == destination_vertex:
        #     return path
        #
        # visited.add(ending_vertex)
        #
        # # make path copy?
        #
        # for neighbor in self.get_neighbors(ending_vertex):
        #     # print(neighbor)
        #     if neighbor not in visited:
        #         visited.add(neighbor)
        #         new_path = path + [neighbor]
        #         path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
        # return path

    # path          visited     neighbor
    # 1             1           2
        # 1,2           1,2         3, 4
            # 123           123         5
                # 124           1234        6, 7
                    # 1235          12345       -
                        # 1246          return
    #

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
