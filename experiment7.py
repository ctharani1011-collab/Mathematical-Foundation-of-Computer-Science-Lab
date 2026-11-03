# Experiment 7: Cartesian Product for an Online Shopping System
# A = products, B = payment methods

A = {"Laptop", "Mobile", "Tablet"}
B = {"UPI", "Card"}

# Build every (product, payment) pair
cartesian = set()
for product in A:
    for payment in B:
        cartesian.add((product, payment))

print("Cartesian Product (A x B):")
for pair in sorted(cartesian):
    print(pair)

print()
print("Cardinality of A x B:", len(cartesian))

# Check the rule |A x B| = |A| * |B|
print("|A| * |B| =", len(A) * len(B))
print("Rule holds?", len(cartesian) == len(A) * len(B))