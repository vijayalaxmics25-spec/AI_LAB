
facts = {
    "American(Robert)",
    "Enemy(A,America)",
    "Owns(A,T1)",
    "Missile(T1)"
}

rules = [
    (["Missile(T1)"], "Weapon(T1)"),

    (["Missile(T1)", "Owns(A,T1)"],
     "Sells(Robert,T1,A)"),

    (["Enemy(A,America)"], "Hostile(A)"),

    (["American(Robert)", "Weapon(T1)",
      "Sells(Robert,T1,A)", "Hostile(A)"],
     "Criminal(Robert)")
]

goal = "Criminal(Robert)"

print("Initial Facts:")
for fact in sorted(facts):
    print(fact)

print("\nForward Chaining Process:")

while True:
    new_fact = False

    for conditions, conclusion in rules:
        if all(c in facts for c in conditions):
            if conclusion not in facts:
                facts.add(conclusion)
                print("Derived:", conclusion)
                new_fact = True

    if goal in facts:
        print("\nGoal proved:", goal)
        break

    if not new_fact:
        print("\nGoal cannot be proved")
        break
