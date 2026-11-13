r"""
capablanca_binary_tree.py
Assessment 3.4: Non-linear Data Structure - BINARY TREE
Built from the last name  C A P A B L A N C A  (placed level by level, left to right)

                    C                     level 0
                /       \
              A           P               level 1
            /   \       /   \
          A       B   L       A           level 2
         / \     /
        N   C   A                         level 3

BFS = Breadth-First Search (level by level, uses a queue)
DFS = Depth-First Search   (go deep first, uses recursion)
"""
from collections import deque

LAST_NAME = "CAPABLANCA"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build(self, values):
        """Build the tree level by level, left to right."""
        if not values:
            return
        self.root = Node(values[0])
        queue = deque([self.root])
        i = 1
        while queue and i < len(values):
            current = queue.popleft()
            if i < len(values):
                current.left = Node(values[i])
                queue.append(current.left)
                i += 1
            if i < len(values):
                current.right = Node(values[i])
                queue.append(current.right)
                i += 1

    # ---------- BFS ----------
    def bfs(self):
        order = []
        if self.root is None:
            return order
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            order.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return order

    # ---------- DFS (three variations) ----------
    def dfs_preorder(self, node, order):      # Root - Left - Right
        if node:
            order.append(node.data)
            self.dfs_preorder(node.left, order)
            self.dfs_preorder(node.right, order)
        return order

    def dfs_inorder(self, node, order):       # Left - Root - Right
        if node:
            self.dfs_inorder(node.left, order)
            order.append(node.data)
            self.dfs_inorder(node.right, order)
        return order

    def dfs_postorder(self, node, order):     # Left - Right - Root
        if node:
            self.dfs_postorder(node.left, order)
            self.dfs_postorder(node.right, order)
            order.append(node.data)
        return order

    # ---------- Search ----------
    def search(self, target):
        """Return True if target is in the tree (uses BFS)."""
        return target in self.bfs()


def main():
    tree = BinaryTree()
    tree.build(list(LAST_NAME))

    print(f"BINARY TREE of {LAST_NAME}")
    print("BFS (level order)  :", " - ".join(tree.bfs()))
    print("DFS (preorder)     :", " - ".join(tree.dfs_preorder(tree.root, [])))
    print("DFS (inorder)      :", " - ".join(tree.dfs_inorder(tree.root, [])))
    print("DFS (postorder)    :", " - ".join(tree.dfs_postorder(tree.root, [])))

    target = "L"
    print(f"Search '{target}'         :", "Found it!" if tree.search(target) else "Not found")


if __name__ == "__main__":
    main()