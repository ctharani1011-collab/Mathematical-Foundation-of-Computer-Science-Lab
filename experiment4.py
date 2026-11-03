# Experiment 4: Set Operations for University Course Registration
# AI, DS, CS are sets of student register numbers

AI = {101, 102, 103, 104}
DS = {103, 104, 105, 106}
CS = {104, 106, 107, 108}

print("Course Enrollment Analysis")
print()
print("AI :", AI)
print("DS :", DS)
print("CS :", CS)
print()

# 1. Students in all three courses (intersection &)
all_three = AI & DS & CS
print("Enrolled in all three courses:", all_three)

# 2. Students in at least one course (union |)
at_least_one = AI | DS | CS
print("Enrolled in at least one course:", at_least_one)

# 3. Students only in AI (difference -)
only_ai = AI - (DS | CS)
print("Enrolled only in AI:", only_ai)

# 4. Students in exactly one course
exactly_one = set()
for student in at_least_one:
    count = 0
    if student in AI:
        count += 1
    if student in DS:
        count += 1
    if student in CS:
        count += 1

    if count == 1:
        exactly_one.add(student)

print("Enrolled in exactly one course:", exactly_one)