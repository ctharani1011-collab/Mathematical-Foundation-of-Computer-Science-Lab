# Experiment 13: BFS shortest route in a hospital
# Rooms are nodes, corridors are connections

from collections import deque

# The hospital layout as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['B', 'C', 'F'],
    'F': ['D', 'E'],
}

start = 'A'   # emergency entrance
goal = 'F'    # ICU

queue = deque([start])        # rooms waiting to be checked
visited = {start}             # rooms already seen
came_from = {start: None}     # remembers which room led to each room
order = []                    # the order rooms are checked

while queue:
    room = queue.popleft()    # take the room that has waited longest
    order.append(room)

    if room == goal:
        break

    for next_room in graph[room]:
        if next_room not in visited:
            visited.add(next_room)
            came_from[next_room] = room
            queue.append(next_room)

# Build the route by walking backwards from the goal
route = []
current = goal
while current is not None:
    route.append(current)
    current = came_from[current]
route.reverse()

print("Traversal order:", order)
print("Shortest route:", route)
print("Corridors used:", len(route) - 1)