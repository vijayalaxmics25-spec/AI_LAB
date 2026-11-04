
# First Order Logic Simulator

domain = input("Enter objects in domain (comma separated): ").split(",")
domain = [x.strip() for x in domain]

facts = input("Enter objects satisfying predicate P(x): ").split(",")
facts = [x.strip() for x in facts]

print("\nFIRST ORDER LOGIC SIMULATOR")
print("1. Universal Quantifier (FOR ALL)")
print("2. Existential Quantifier (THERE EXISTS)")

choice = int(input("Enter your choice: "))

if not all(x in domain for x in facts):
    print("Error: Predicate contains objects outside the domain!")

elif choice == 1:
    result = all(x in facts for x in domain)
    print("\nExpression: For all x, P(x)")

    if result:
        print("Result: TRUE")
    else:
        print("Result: FALSE")

elif choice == 2:
    result = any(x in facts for x in domain)
    print("\nExpression: There exists x, P(x)")

    if result:
        print("Result: TRUE")
    else:
        print("Result: FALSE")

else:
    print("Invalid choice!")
