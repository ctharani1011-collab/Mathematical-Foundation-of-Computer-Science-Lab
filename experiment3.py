# Experiment 3: Predicate Logic for Employee Eligibility
# T(x): employee x has completed basic training
# E(x): employee x has at least 2 years of experience
# A(x): employee x is eligible = T(x) AND E(x)

employees = {
    "E1": {"training": True,  "experience": 3},
    "E2": {"training": False, "experience": 4},
    "E3": {"training": True,  "experience": 1},
    "E4": {"training": True,  "experience": 5},
}

def has_training(emp):        # T(x)
    return emp["training"]

def has_experience(emp):      # E(x)
    return emp["experience"] >= 2

def is_eligible(emp):         # A(x) = T(x) AND E(x)
    return has_training(emp) and has_experience(emp)

print("Employee Eligibility Check")
print("Rule: Training AND Experience >= 2")
print()
print("Employee | Training | Experience | Result")
print("-" * 41)

eligible = []
not_eligible = []

for name, emp in employees.items():
    training_text = "Yes" if has_training(emp) else "No"
    result = is_eligible(emp)
    result_text = "Eligible" if result else "Not Eligible"

    print(f"{name:<8} | {training_text:<8} | {emp['experience']:<10} | {result_text}")

    if result:
        eligible.append(name)
    else:
        not_eligible.append(name)

print()
print("Eligible employees:", ", ".join(eligible))
print("Not eligible employees:", ", ".join(not_eligible))