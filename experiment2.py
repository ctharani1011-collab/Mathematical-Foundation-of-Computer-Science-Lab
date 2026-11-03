# Experiment 2: Logical Equivalence Verification (De Morgan's Law)
# Expression 1: NOT (P AND Q)
# Expression 2: (NOT P) OR (NOT Q)

print("Checking if NOT(P AND Q) is the same as (NOT P) OR (NOT Q)")
print()
print("P  Q  | NOT(P AND Q) | (NOT P) OR (NOT Q)")
print("-" * 45)

all_same = True

for P in [False, True]:
    for Q in [False, True]:
        E1 = not (P and Q)
        E2 = (not P) or (not Q)

        print(int(P), " ", int(Q), " |      ", int(E1), "      |        ", int(E2))

        if E1 != E2:
            all_same = False

print()
print("Are they logically equivalent?", all_same)