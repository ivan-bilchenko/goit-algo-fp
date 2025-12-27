import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"
        self.id = str(uuid.uuid4())


def build_heap_tree(heap, index=0):
    """Builds a tree from heap array representation."""
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node


def generate_colors(n):
    """Generates colors from dark to light blue."""
    colors = []
    for i in range(n):
        ratio = i / max(n - 1, 1)
        r = int(18 + ratio * (173 - 18))
        g = int(50 + ratio * (216 - 50))
        b = int(120 + ratio * (230 - 120))
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors


def collect_nodes(root):
    """Collects all nodes for counting."""
    nodes = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            nodes.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return nodes


def dfs_traversal(root):
    """Depth-first search using stack."""
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return order


def bfs_traversal(root):
    """Breadth-first search using queue."""
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return order


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500,
            node_color=colors, font_color="white", font_weight="bold")
    plt.title(title)
    plt.show()


def visualize_traversal(root, traversal_func, title):
    """Visualizes tree traversal with gradient colors."""
    order = traversal_func(root)
    colors = generate_colors(len(order))

    for i, node in enumerate(order):
        node.color = colors[i]

    draw_tree(root, title)


if __name__ == "__main__":
    heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("DFS (Depth-First Search) - using stack")
    root_dfs = build_heap_tree(heap)
    visualize_traversal(root_dfs, dfs_traversal, "DFS Traversal (dark → light)")

    print("BFS (Breadth-First Search) - using queue")
    root_bfs = build_heap_tree(heap)
    visualize_traversal(root_bfs, bfs_traversal, "BFS Traversal (dark → light)")
