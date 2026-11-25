
import re

def parse(exp):
    tokens = re.findall(r'~|[A-Za-z][A-Za-z0-9_]*|[&|()]', exp.replace(" ", ""))
    if ''.join(tokens) != exp.replace(" ", ""):
        raise ValueError("Invalid expression")

    pos = [0]

    def atom():
        if pos[0] >= len(tokens):
            raise ValueError("Invalid expression")

        if tokens[pos[0]] == '(':
            pos[0] += 1
            node = expr()
            if pos[0] >= len(tokens) or tokens[pos[0]] != ')':
                raise ValueError("Missing bracket")
            pos[0] += 1
            return node

        if tokens[pos[0]] == '~':
            pos[0] += 1
            if pos[0] >= len(tokens) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', tokens[pos[0]]):
                raise ValueError("Invalid NOT")
            node = ('lit', '~' + tokens[pos[0]])
            pos[0] += 1
            return node

        if re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', tokens[pos[0]]):
            node = ('lit', tokens[pos[0]])
            pos[0] += 1
            return node

        raise ValueError("Invalid expression")

    def and_expr():
        node = atom()
        while pos[0] < len(tokens) and tokens[pos[0]] == '&':
            pos[0] += 1
            node = ('and', node, atom())
        return node

    def expr():
        node = and_expr()
        while pos[0] < len(tokens) and tokens[pos[0]] == '|':
            pos[0] += 1
            node = ('or', node, and_expr())
        return node

    result = expr()

    if pos[0] != len(tokens):
        raise ValueError("Invalid expression")

    return result


def is_literal(node):
    return node[0] == 'lit'


def is_clause(node):
    if node[0] == 'lit':
        return True
    if node[0] == 'or':
        return is_clause(node[1]) and is_clause(node[2])
    return False


def is_cnf(node):
    if node[0] == 'and':
        return is_cnf(node[1]) and is_cnf(node[2])
    return is_clause(node) 


try:
    exp = input("Enter logical expression: ")
    tree = parse(exp)

    if is_cnf(tree):
        print("Expression is in CNF")
    else:
        print("Expression is not in CNF")

except ValueError:
    print("Invalid logical expression")


