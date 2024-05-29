# Complete Example
# Here's a complete example demonstrating all the concepts discussed:


students = {
    'student1': {
        'name': 'John Doe',
        'age': 20,
        'courses': ['Math', 'Science']
    },
    'student2': {
        'name': 'Jane Smith',
        'age': 22,
        'courses': ['English', 'History']
    }
}

# Accessing values
print(students['student1']['name'])  # Output: John Doe

# Modifying values
students['student1']['age'] = 21
students['student2']['courses'].append('Art')

# Adding and removing elements
students['student3'] = {
    'name': 'Emily Davis',
    'age': 19,
    'courses': ['Biology', 'Chemistry']
}
del students['student1']

# Dictionary functions
print(students.keys())  # Output: dict_keys(['student2', 'student3'])
print(students.values())  # Output: dict_values([{'name': 'Jane Smith', 'age': 22, 'courses': ['English', 'History', 'Art']}, {'name': 'Emily Davis', 'age': 19, 'courses': ['Biology', 'Chemistry']}])
print(students.items())  # Output: dict_items([('student2', {'name': 'Jane Smith', 'age': 22, 'courses': ['English', 'History', 'Art']}), ('student3', {'name': 'Emily Davis', 'age': 19, 'courses': ['Biology', 'Chemistry']})])
print(students.get('student2'))  # Output: {'name': 'Jane Smith', 'age': 22, 'courses': ['English', 'History', 'Art']}

# Updating dictionary
students['student3'].update({'age': 20, 'courses': ['Biology', 'Physics']})

# Looping through nested dictionary
for student, info in students.items():
    print(f"\n{student}:")
    for key, value in info.items():
        print(f"  {key}: {value}")