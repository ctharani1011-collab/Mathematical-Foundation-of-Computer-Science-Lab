# Experiment 10: Fibonacci Sequence for Population Growth
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2)

n = int(input("Enter number of generations: "))

# Start with the two known values
f = [0, 1]

# Each new generation is the sum of the previous two
for i in range(2, n + 1):
    next_value = f[i - 1] + f[i - 2]
    f.append(next_value)

print()
print("Population Sequence:")
for i in range(n + 1):
    print("Generation", i, ":", f[i])

print()
print("Final population at generation", n, "=", f[n])