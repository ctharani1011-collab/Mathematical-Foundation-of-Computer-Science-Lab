# Experiment 14: Minimum cost network using Kruskal's algorithm
# Substations are nodes, possible connections are weighted edges

# Each edge is (cost, substation1, substation2)
edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (2, 'B', 'C'),
    (4, 'B', 'D'),
    (5, 'C', 'D'),
    (6, 'C', 'E'),
    (7, 'D', 'E'),
]

# group[x] tells us which group substation x belongs to
group = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}

def find_group(x):
    return group[x]

def join_groups(old_group, new_group):
    # change every substation in old_group to belong to new_group
    for s in group:
        if group[s] == old_group:
            group[s] = new_group

edges.sort()          # cheapest connection first

chosen = []           # the connections we keep
total_cost = 0

for cost, s1, s2 in edges:
    g1 = find_group(s1)
    g2 = find_group(s2)

    # Only keep the cable if it joins two different groups (no loop)
    if g1 != g2:
        join_groups(g2, g1)
        chosen.append((s1, s2, cost))
        total_cost += cost

print("Minimum Spanning Tree:")
for s1, s2, cost in chosen:
    print(s1, "-", s2, ":", cost)

print()
print("Total Installation Cost:", total_cost)