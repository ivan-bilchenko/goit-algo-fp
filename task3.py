import heapq


def dijkstra(graph, start):
    """
    Dijkstra's algorithm using binary heap for finding shortest paths.
    Returns distances and paths from start vertex to all other vertices.
    """
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}

    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))

    return distances, previous


def get_path(previous, start, end):
    """Reconstructs the path from start to end vertex."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path if path[0] == start else []


if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1, "E": 3},
        "E": {"D": 3, "F": 2},
        "F": {"E": 2},
    }

    start_vertex = "A"
    distances, previous = dijkstra(graph, start_vertex)

    print(f"Shortest distances from vertex '{start_vertex}':")
    for vertex, distance in distances.items():
        path = get_path(previous, start_vertex, vertex)
        print(f"  {start_vertex} -> {vertex}: distance = {distance}, path: {' -> '.join(path)}")
