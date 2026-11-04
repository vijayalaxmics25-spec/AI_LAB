
import random
import math

def objective(x):
    return -(x - 5) ** 2 + 25

current = random.uniform(0, 10)
best = current

temperature = 100
cooling_rate = 0.95

while temperature > 0.1:

    neighbor = current + random.uniform(-1, 1)

    neighbor = max(0, min(10, neighbor))

    current_value = objective(current)
    neighbor_value = objective(neighbor)

    difference = neighbor_value - current_value

    if difference > 0:
        current = neighbor

    else:
        probability = math.exp(difference / temperature)

        if random.random() < probability:
            current = neighbor

    if objective(current) > objective(best):
        best = current

    temperature = temperature * cooling_rate

print("Best solution:", round(best, 4))
print("Maximum value:", round(objective(best), 4))
