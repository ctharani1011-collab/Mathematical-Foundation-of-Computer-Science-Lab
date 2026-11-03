# Experiment 18: Euler circuit for postal delivery route
# Roads are edges. Every road must be used exactly once,
# and the van must return to where it started.

roads = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['C', 'E'],
    'E': ['C', 'D'],
}

# Step 1: degree of each place = number of roads touching it
print("Degree of each place:")
for place in roads:
    print(place, ":", len(roads[place]))

# Step 2: an Euler circuit exists only if every degree is even
all_even = all(len(roads[place]) % 2 == 0 for place in roads)

if not all_even:
    print("\nNo Euler circuit exists (some place has an odd degree).")
else:
    print("\nAll degrees are even, so an Euler circuit exists.")

    # Step 3: Hierholzer's method (use a copy, so we can remove roads as we use them)
    unused = {place: list(nbrs) for place, nbrs in roads.items()}
    start = 'A'
    stack = [start]
    circuit = []

    while stack:
        place = stack[-1]
        if unused[place]:
            nxt = unused[place].pop()        # use one road from here
            unused[nxt].remove(place)        # remove that same road from the other end
            stack.append(nxt)
        else:
            circuit.append(stack.pop())      # dead end: record this place

    circuit.reverse()
    print("Euler circuit:", " -> ".join(circuit))