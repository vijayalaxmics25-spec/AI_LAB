import random

def heuristic(state):
    conflicts = 0

    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def get_neighbors(state):
    neighbors = []

    for col in range(4):
        for row in range(4):
            if state[col] != row:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)

    return neighbors

def hill_climbing():
    state = [random.randint(0, 3) for i in range(4)]

    while True:
        h = heuristic(state)
        print("State:", state, "Heuristic:", h)

        if h == 0:
            print("Solution found!")
            return state

        neighbors = get_neighbors(state)
        best = min(neighbors, key=heuristic)

        if heuristic(best) >= h:
            print("Local minimum reached. Restarting...")
            return hill_climbing()

        state = best

solution = hill_climbing()

print("\nFinal Chessboard:")
for row in range(4):
    for col in range(4):
        if solution[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()