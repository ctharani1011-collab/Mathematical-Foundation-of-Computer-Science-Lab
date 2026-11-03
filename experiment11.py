# Experiment 11: Binary Search Comparison Count
# Recurrence: T(n) = T(n/2) + 1, with T(1) = 1
# Each comparison cuts the list in half

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2   # check the middle item
        count += 1                # one comparison done

        if arr[mid] == key:
            return mid, count     # found it
        elif arr[mid] < key:
            low = mid + 1         # key is in the right half
        else:
            high = mid - 1        # key is in the left half

    return -1, count              # not found


n = int(input("Enter number of elements: "))
arr = list(range(1, n + 1))       # sorted list: 1, 2, 3, ..., n

key = int(input("Enter element to search: "))

position, comparisons = binary_search(arr, key)

print()
print("Position:", position)
print("Comparisons:", comparisons)