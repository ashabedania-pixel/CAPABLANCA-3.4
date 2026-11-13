r"""
capablanca_graph.py
Assessment 3.4: Non-linear Data Structure - GRAPH
Vertices come from the letters of the last name CAPABLANCA: C, A, P, B, L, N

   level 0:          C
                  /  |  \
   level 1:      A   P   B
                 |   |
   level 2:      L   N

BFS = Breadth-First Search (level by level, uses a queue)
DFS = Depth-First Search   (go deep first, uses recursion)
"""
from collections import deque

LAST_NAME = "CAPABLANCA"


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_edge(self, u, v):
        """Undirected edge between vertex u and vertex v."""
        self.adjacency.setdefault(u, [])
        self.adjacency.setdefault(v, [])
        self.adjacency[u].append(v)
        self.adjacency[v].append(u)

    def display(self):
        for vertex, neighbors in self.adjacency.items():
            print(f"  {vertex} -> {', '.join(neighbors)}")

    # ---------- BFS ----------
    def bfs(self, start):
        visited = {start}
        order = []
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self.adjacency[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    # ---------- DFS ----------
    def dfs(self, start):
        visited = set()
        order = []

        def visit(vertex):
            visited.add(vertex)
            order.append(vertex)
            for neighbor in self.adjacency[vertex]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return order

    # ---------- Search ----------
    def search(self, start, target):
        """Return True if target can be reached from start (uses BFS)."""
        return target in self.bfs(start)


def main():
    edges = [
        ("C", "A"), ("C", "P"), ("C", "B"),
        ("A", "L"), ("P", "N"),
    ]
    start = "C"

    graph = Graph()
    for u, v in edges:
        graph.add_edge(u, v)

    print(f"GRAPH of {LAST_NAME} (adjacency list)")
    graph.display()
    print()
    print("BFS from", start, ":", " - ".join(graph.bfs(start)))
    print("DFS from", start, ":", " - ".join(graph.dfs(start)))

    target = "N"
    print(f"Search '{target}'   :", "Found it!" if graph.search(start, target) else "Not found")


if __name__ == "__main__":
    main()