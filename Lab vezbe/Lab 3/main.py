# zadatak 10
import queue


def dfs(graph, start, end):
    if start == end:
        return [start]

    stack = queue.LifoQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    stack.put(start)
    found_dest = False

    while (not found_dest) and (not stack.empty()):
        node = stack.get()
        for dest in graph[node]:
            if dest not in visited:
                prev_nodes[dest] = node
                if dest is end:
                    found_dest = True
                    break
                visited.add(dest)
                stack.put(dest)

    path = []
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()

    return path


def find_path(graph, start, through, end):
    if start == through and through == end:
        return [start]

    if start == through and through != end:
        return dfs(graph, start, end)
    if start != through and through == end:
        return dfs(graph, start, end)

    path1 = dfs(graph, start, through)
    path2 = dfs(graph, through, end)

    if not path1 or not path2:
        return None

    return path1 + path2[1:]


if __name__ == '__main__':

    graph1 = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E', 'G'],
        'C': ['A', 'F'],
        'D': ['B', 'E'],
        'E': ['B', 'D'],
        'F': ['C', 'I'],
        'G': ['B', 'H'],
        'H': ['G'],
        'I': ['F'],
        'J': []
    }

    zadati_graf = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'H'],
        'E': ['B', 'I', 'J'],
        'F': ['C'],
        'G': ['C', 'K'],
        'H': ['D'],
        'I': ['E'],
        'J': ['E'],
        'K': ['G', 'L'],
        'L': ['K', 'M', 'N'],
        'M': ['L'],
        'N': ['L']
    }

    print(find_path(zadati_graf, 'A', 'L', 'L'))
