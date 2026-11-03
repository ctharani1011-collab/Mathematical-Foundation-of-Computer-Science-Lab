# Experiment 16: Shortest route using Dijkstra's algorithm
# Locations are nodes, roads are weighted edges (distance)

import heapq

# The road network as an adjacency list: (neighbour, distance)
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('D', 2)],
}

start = 'A'
goal = 'E'

best_distance = {start: 0}   # shortest distance found so far to each location
came_from = {start: None}    # which location we came from on the best route
to_visit = [(0, start)]      # (distance so far, location), smallest first

while to_visit:
    dist, place = heapq.heappop(to_visit)   # take the closest unvisited place

    # Skip old entries that are no longer the best distance
    if dist > best_distance[place]:
        continue

    # Look at each road leaving this place
    for neighbour, road_length in graph[place]:
        new_dist = dist + road_length

        # If this road gives a shorter trip, remember it
        if new_dist < best_distance.get(neighbour, float('inf')):
            best_distance[neighbour] = new_dist
            came_from[neighbour] = place
            heapq.heappush(to_visit, (new_dist, neighbour))

# Rebuild the route by walking backwards from the goal
route = []
current = goal
while current is not None:
    route.append(current)
    current = came_from[current]
route.reverse()

print("Shortest route:", route)
print("Total distance:", best_distance[goal])