
def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def NOT(p):
    return not p

def IMPLIES(p, q):
    return (not p) or q

def BICONDITIONAL(p, q):
    return p == q


print("\nPROPOSITIONAL LOGIC SIMULATOR")
print("1. AND")
print("2. OR")
print("3. NOT")
print("4. IMPLIES")
print("5. BICONDITIONAL")

choice = int(input("Enter your choice: "))

if choice < 1 or choice > 5:
    print("Invalid choice!")

else:
    p = input("Enter value of P (True/False): ").lower()

    if p not in ["true", "false"]:
        print("Invalid input for P!")

    else:
        p = (p == "true")

        if choice == 3:
            result = NOT(p)

        else:
            q = input("Enter value of Q (True/False): ").lower()

            if q not in ["true", "false"]:
                print("Invalid input for Q!")
                exit()

            q = (q == "true")

            if choice == 1:
                result = AND(p, q)
            elif choice == 2:
                result = OR(p, q)
            elif choice == 4:
                result = IMPLIES(p, q)
            elif choice == 5:
                result = BICONDITIONAL(p, q)

        print("Result:", result)
