from collections import defaultdict, deque


def topological_sort(tasks):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # Initialize indegree
    for task in tasks:
        indegree[task["id"]] = 0

    # Build graph
    for task in tasks:
        for dep in task["dependencies"]:
            graph[dep].append(task["id"])
            indegree[task["id"]] += 1

    queue = deque([task_id for task_id in indegree if indegree[task_id] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) != len(tasks):
        raise ValueError("Circular dependency detected!")

    return sorted_order
