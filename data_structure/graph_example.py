if __name__ == "__main__":
    edges = [(1, 2), (1, 4), (1, 6), (2, 3), (4, 5)]
    graph = {}
    for edge in edges:
        (n1, n2) = edge
        if (n1 in graph):
            graph[n1].append(n2)
        else:
            graph[n1] = [n2]
        if (n2 in graph):
            graph[n2].append(n1)
        else:
            graph[n2] = [n1]
