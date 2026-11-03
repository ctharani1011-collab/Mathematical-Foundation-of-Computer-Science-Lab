# Experiment 5: Function Mapping for Student Department Allocation
# Students (domain) and departments (codomain)

A = {1, 2, 3, 4}               # students
B = {"IT", "CSE", "ECE"}       # departments

# The mapping: each student -> one department
f = {
    1: "IT",
    2: "CSE",
    3: "ECE",
    4: "CSE",
}

print("Function Mapping (student -> department)")
for student in sorted(A):
    print(student, "->", f[student])

# Departments that are actually used (the range)
range_set = set(f.values())
print()
print("Range (departments used):", sorted(range_set))

# Injective: no two students share a department
injective = len(range_set) == len(f)

# Surjective: every department has at least one student
surjective = range_set == B

print()
print("Injective (one-to-one)?", injective)
print("Surjective (onto)?", surjective)