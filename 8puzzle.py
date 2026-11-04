import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

def get_neighbors(state):
    neighbors = []
    pos = state.index(0)
    row, col = divmod(pos, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[pos], new_state[new_pos] = (
                new_state[new_pos], new_state[pos]
            )

            neighbors.append(tuple(new_state))

    return neighbors

def astar(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start))

    cost = {start: 0}
    parent = {start: None}

    while pq:
        f, g, current = heapq.heappop(pq)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        if g != cost[current]:
            continue

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in cost or new_g < cost[neighbor]:
                cost[neighbor] = new_g
                parent[neighbor] = current

                new_f = new_g + heuristic(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor))

    return None

path = astar(start, goal)

if path:
    print("Solution found!")
    print("Total moves:", len(path) - 1)

    for step in path:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution found!")