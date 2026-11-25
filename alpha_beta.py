
def alpha_beta(node, alpha, beta, maximizing):

    if isinstance(node, int):
        return node

    if maximizing:
        value = float('-inf')
        for child in node:
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)
            print("MAX: Alpha =", alpha)

            if alpha >= beta:
                print("Pruning remaining branches!")
                break
        return value

    else:
        value = float('inf')
        for child in node:
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)
            print("MIN: Beta =", beta)

            if alpha >= beta:
                print("Pruning remaining branches!")
                break
        return value


def create_tree(level):
    n = int(input("Number of children: "))
    tree = []

    for i in range(n):
        if level == 1:
            tree.append(int(input("Enter leaf value: ")))
        else:
            print("Node", i + 1)
            tree.append(create_tree(level - 1))

    return tree


print("===== ALPHA BETA PRUNING =====")

depth = int(input("Enter tree depth: "))
tree = create_tree(depth)

print("\nGame Tree:", tree)
print("\nSearching the best move...\n")

result = alpha_beta(tree, float('-inf'), float('inf'), True)

print("\nOptimal value:", result)
