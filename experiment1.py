# Experiment 1: Truth Table for Automated Railway Signalling System
# P = Track is clear
# Q = Signal is green
# R = Emergency override is activated
# Entry rule: (P AND Q) OR R

print("Truth Table for Train Entry Permission")
print("Expression: (P AND Q) OR R")
print()
print("P  Q  R  | Entry")
print("-" * 15)

permitted = []

for P in [False, True]:
    for Q in [False, True]:
        for R in [False, True]:
            entry = (P and Q) or R
            print(int(P), " ", int(Q), " ", int(R), " | ", int(entry))

            if entry:
                permitted.append((P, Q, R))

print()
print("Conditions where the train IS permitted to enter:")
for P, Q, R in permitted:
    print("  Track clear:", int(P), "| Signal green:", int(Q), "| Override:", int(R))

print()
print("Total permitted cases:", len(permitted), "out of 8")