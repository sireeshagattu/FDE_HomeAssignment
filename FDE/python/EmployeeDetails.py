employees = [
    [101, "Sireesha", 200000],
    [102, "Rahul", 180000],
    [103, "Praveen", 260000],
    [104, "Sujatha", 220000],
    [105, "Anjali", 150000]
]

for employee in employees:
    emp_id = employee[0]
    name = employee[1]
    salary = employee[2]

    if len(name) > 6 and salary < 250000:
        print(name)