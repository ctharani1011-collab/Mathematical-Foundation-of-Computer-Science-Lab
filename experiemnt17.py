# Experiment 17: Exam timetable using graph colouring
# Subjects are nodes. An edge means two exams share students,
# so they cannot be in the same slot.

conflicts = {
    'Maths':       ['Programming', 'Networks'],
    'Programming': ['Maths', 'Database'],
    'Networks':    ['Maths', 'Database'],
    'Database':    ['Programming', 'Networks'],
}

slot = {}   # subject -> slot number (starting at 0)

# Go through the subjects one by one (greedy)
for subject in conflicts:

    # Find the slots already taken by conflicting subjects
    taken = set()
    for other in conflicts[subject]:
        if other in slot:
            taken.add(slot[other])

    # Pick the smallest slot number that is not taken
    s = 0
    while s in taken:
        s += 1

    slot[subject] = s

print("Examination Timetable:")
for subject in slot:
    print(subject, "-> Slot", slot[subject] + 1)

print()
print("Total slots used:", len(set(slot.values())))