# Experiment 8: Equivalence Relation for Student Grouping
# Students 1, 2 are in Year 1
# Students 3, 4 are in Year 2
# Students 5, 6 are in Year 3

students = {1, 2, 3, 4, 5, 6}

year = {
    1: 1, 2: 1,
    3: 2, 4: 2,
    5: 3, 6: 3,
}

# R: two students are related if they are in the same year
R = set()
for a in students:
    for b in students:
        if year[a] == year[b]:
            R.add((a, b))

# Reflexive: every student is related to themselves
reflexive = all((a, a) in R for a in students)

# Symmetric: if (a, b) is in R, then (b, a) is in R
symmetric = all((b, a) in R for (a, b) in R)

# Transitive: if (a, b) and (b, c) are in R, then (a, c) is in R
transitive = True
for (a, b) in R:
    for (x, c) in R:
        if b == x and (a, c) not in R:
            transitive = False

is_equivalence = reflexive and symmetric and transitive

print("Reflexive?  ", reflexive)
print("Symmetric?  ", symmetric)
print("Transitive? ", transitive)
print()
print("Equivalence relation?", is_equivalence)

# Equivalence classes: group students by their year
classes = {}
for student in sorted(students):
    y = year[student]
    if y not in classes:
        classes[y] = set()
    classes[y].add(student)

print()
print("Equivalence classes:")
for y in sorted(classes):
    print("Year", y, "->", sorted(classes[y]))