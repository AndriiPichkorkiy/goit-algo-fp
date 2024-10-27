import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:

    def __init__(self, key, color="skyblue"):

        self.left = Node | None
        self.right = Node | None
        self.val = key
        self.color = color   # Додатковий аргумент для зберігання кольору вузла
        self.order = ""   # Додатковий аргумент для зберігання порядку проходження дерева
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph: nx.DiGraph, node: Node, pos, x=0, y=0, layer=1):

    if node is not None:

        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color,
                       label=str(node.val) + node.order)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors_list=None, title="Дерево"):

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(
        data=True)] if colors_list is None else colors_list
    # Використовуйте значення вузла для міток
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(label=title, loc="left")
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap, index=0):
    try:
        leaf = Node(heap[index])
        leaf.left = build_heap_tree(heap, index * 2 + 1)
        leaf.right = build_heap_tree(heap, index * 2 + 2)
        return leaf
    except:
        return None


heap_list = [0, 4, 5, 10, 1, 3]
heapq.heapify(heap_list)
print(heap_list)

root = build_heap_tree(heap_list)

if __name__ == "__main__":
    # # Відображення дерева
    draw_tree(root)
