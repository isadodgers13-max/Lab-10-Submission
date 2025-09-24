from functools import reduce

# Step 1: Create a list of employees
employees = [
    {"name": "PersonA", "salary": 1000, "department": "Engineering"},
    {"name": "PersonB", "salary": 7500, "department": "Marketing"},
    {"name": "PersonC", "salary": 5000, "department": "Sales"}
]

# Step 2a: Increase salary by 10% using map + lambda
incremented_salaries = list(map(lambda emp: {
    "name": emp["name"],
    "salary": emp["salary"] * 1.10,
    "department": emp["department"]
}, employees))

# Step 2b: Filter employees earning above $7,000 using filter + lambda
high_earners = list(filter(lambda emp: emp["salary"] > 7000, incremented_salaries))

# Step 2c: Calculate total payroll using reduce + lambda
total_payroll = reduce(lambda acc, emp: acc + emp["salary"], incremented_salaries, 0)

# Print results
print("Salaries After 10% Increment:")
print(incremented_salaries)

print("\nEmployees Earning Above $7,000:")
print(high_earners)

print(f"\nTotal Payroll Amount: ${total_payroll:.2f}")
