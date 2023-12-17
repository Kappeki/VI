def is_safe(node, graph, colors, color):
    for adjacent in graph[node]:
        if color == colors[adjacent]:
            return False
    return True


def graph_coloring(graph, num_of_colors, colors, node, num_of_nodes):
    if node == num_of_nodes:
        return True

    for color in range(1, num_of_colors + 1):
        if is_safe(node, graph, colors, color):
            colors[node] = color
            if graph_coloring(graph, num_of_colors, colors, node + 1, num_of_nodes):
                return True
            colors[node] = 0

    return False


def forward_checking(graph, colors, node, num_of_colors):
    for adjacent in graph[node]:
        if colors[adjacent] == 0:
            safe = False
            for color in range(1, num_of_colors + 1):
                if is_safe(adjacent, graph, colors, color):
                    safe = True
                    break
            if not safe:
                return False
    return True


def forward_checking2(graph, colors, node, num_of_colors):
    for adjacent in graph[node]:
        if colors[adjacent] == 0:
            safe_adjacent = False
            for color in range(1, num_of_colors + 1):
                if is_safe(adjacent, graph, colors, color):
                    safe_adjacent = True
                    safe_depth_2 = True
                    for next_adjacent in graph[adjacent]:
                        if colors[next_adjacent] == 0:
                            for next_color in range(1, num_of_colors + 1):
                                if not is_safe(next_adjacent, graph, colors, next_color):
                                    safe_depth_2 = False
                                    break
                    if not safe_depth_2:
                        return False
            if not safe_adjacent:
                return False
    return True


def graph_coloring_with_forward_checking(graph, num_of_colors, colors, node, num_of_nodes):
    if node == num_of_nodes:
        return True

    for color in range(1, num_of_colors + 1):
        if is_safe(node, graph, colors, color):
            colors[node] = color
            if (forward_checking(graph, colors, node, num_of_colors) and
                    graph_coloring_with_forward_checking(graph, num_of_colors, colors, node + 1, num_of_nodes)):
                return True
            colors[node] = 0

    return False


if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [0, 2, 4],
        2: [0, 1, 3, 4],
        3: [2, 4],
        4: [1, 2, 3]
    }
    num_of_nodes = len(graph)
    num_of_colors = 3
    colors = [0] * num_of_nodes  # 0 - neobojeni, 1 - crvena, 2 - zelena, 3 - plava

    result = graph_coloring_with_forward_checking(graph, num_of_colors, colors, 0, num_of_nodes)

    print(result, colors)
