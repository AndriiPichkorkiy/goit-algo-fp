import networkx as nx
import heapq

G = nx.Graph()

# Додаємо вершини
locations = [
    'Hogwarts', 'Hogsmeade', 'Ministry of Magic', 'Diagon Alley',
    'Platform 9¾', 'Forbidden Forest', 'Malfoy Manor',
    'The Burrow', 'Gringotts Bank', '12 Grimmauld Place'
]
G.add_nodes_from(locations)

# Додаємо ребра (шляхи між локаціями) з вагою (weight)
edges_with_weights = [
    ('Hogwarts', 'Hogsmeade', 5),
    ('Hogwarts', 'Forbidden Forest', 3),
    ('Hogwarts', 'Platform 9¾', 8),
    ('Hogsmeade', 'The Burrow', 7),
    ('The Burrow', 'Diagon Alley', 9),
    ('Diagon Alley', 'Ministry of Magic', 3),
    ('Ministry of Magic', 'Gringotts Bank', 3),
    ('Gringotts Bank', 'Malfoy Manor', 7),
    ('Platform 9¾', '12 Grimmauld Place', 4),
    ('12 Grimmauld Place', 'Ministry of Magic', 3)
]

# Додаємо ребра та ваги
G.add_weighted_edges_from(edges_with_weights)


def dijkstra(graph: dict[str, dict[str, dict[str, int]]], start: str) -> dict[str, float]:
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]  # Кортежі (відстань, вершина)

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, params in graph[current_vertex].items():
            weight = params.get("weight")
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def print_table(distances: dict[str, int]):
    # Верхній рядок таблиці
    print("{:<20} | {:<10}".format("Вершина", "Відстань"))
    print("-" * 30)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        print("{:<20} | {:<10}".format(vertex, distance))
    print("\n")


if __name__ == "__main__":
    print("Найкоротший шлях між всіма вершинами графа:")
    print_table(dijkstra(nx.to_dict_of_dicts(G), 'Hogwarts'))
