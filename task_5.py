from collections import deque
from task_4 import root, Node, draw_tree
from task_2 import Color


def get_colors_DFS(tree_root: Node):
    colors = Color()
    color_list = []

    def recursion_dfs(node: Node):
        if node is None:
            return
        color_list.append(colors.get())

        node.order = f"\nVisited: №{len(color_list)}"
        recursion_dfs(node.left)
        recursion_dfs(node.right)

    recursion_dfs(tree_root)
    return color_list


def get_colors_BFS(tree_root: Node):
    colors = Color()
    color_list = []

    # Ініціалізація черги з початковою вершиною
    queue = deque([tree_root])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()

        # Пропускаємо порожні листки
        if vertex is None:
            continue

        # Якщо не була відвідана, додаємо колір
        color_list.append(colors.get())

        vertex.order = f"\nVisited: №{len(color_list)}"

        # Додаємо всіх невідвіданих сусідів вершини до кінця черги
        # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
        queue.extend([vertex.left, vertex.right])

    return color_list


if __name__ == "__main__":
    # # DFS
    colors_DFS = get_colors_DFS(root)
    draw_tree(root, colors_DFS, "Пошук у глибину (DFS)")

    # BFS
    colors_BFS = get_colors_BFS(root)
    draw_tree(root, colors_BFS, "Пошук у ширину (BFS)")
