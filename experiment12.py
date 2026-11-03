# Experiment 12: Tower of Hanoi using recursion
# Recurrence: T(n) = 2T(n-1) + 1, with T(1) = 1
# Towers: A = source, B = helper, C = destination

moves = 0  # counts every disk move

def hanoi(n, source, helper, destination):
    global moves

    # Base case: only one disk, move it directly
    if n == 1:
        moves += 1
        print("Move disk 1 from", source, "to", destination)
        return

    # Step 1: move the top n-1 disks out of the way
    hanoi(n - 1, source, destination, helper)

    # Step 2: move the biggest disk to the destination
    moves += 1
    print("Move disk", n, "from", source, "to", destination)

    # Step 3: move the n-1 disks on top of the biggest disk
    hanoi(n - 1, helper, source, destination)


n = int(input("Enter number of disks: "))

hanoi(n, 'A', 'B', 'C')

print()
print("Total moves:", moves)
print("Minimum moves (2^n - 1):", 2 ** n - 1)