# Experiment 6: Relation Analysis for a Course Prerequisite System
# Courses: 1 = Programming, 2 = Data Structures, 3 = Algorithms

A = {1, 2, 3}

# The relation R as ordered pairs (a, b)
R = {
    (1, 1), (2, 2), (3, 3),
    (1, 2), (2, 3), (1, 3),
}

# Reflexive: every course is related to itself
reflexive = all((a, a) in R for a in A)

# Symmetric: if (a, b) is in R, then (b, a) must also be in R
symmetric = all((b, a) in R for (a, b) in R)

# Antisymmetric: if (a, b) and (b, a) are both in R, then a must equal b
antisymmetric = all(
    a == b or (b, a) not in R
    for (a, b) in R
)

# Transitive: if (a, b) and (b, c) are in R, then (a, c) must be in R
transitive = all(
    (a, c) in R
    for (a, b) in R
    for (x, c) in R
    if b == x
)

print("Relation R:", sorted(R))
print()
print("Reflexive?    ", reflexive)
print("Symmetric?    ", symmetric)
print("Antisymmetric?", antisymmetric)
print("Transitive?   ", transitive)

# A partial order must be reflexive, antisymmetric and transitive
partial_order = reflexive and antisymmetric and transitive
print()
print("Partial order?", partial_order)