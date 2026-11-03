# Experiment 9: Function Composition for Employee Salary Processing
# f(x): add a bonus of 5000
# g(x): take 10% tax (keep 90%)

def f(x):
    return x + 5000

def g(x):
    return 0.9 * x

salary = 30000

print("Basic Salary:", salary)
print()

# Step 1: apply f first
after_bonus = f(salary)
print("After bonus f(x):", after_bonus)

# Step 2: apply g to the result of f
gf = g(f(salary))
print("g(f(x)) - bonus first, then tax:", gf)

# Step 3: apply g first, then f
fg = f(g(salary))
print("f(g(x)) - tax first, then bonus:", fg)

print()
print("Are they equal?", gf == fg)