# brojevi_1 = list(range(1, 10))
# brojevi_2 = list(range(1, 10))

# nova_lista = list(zip(brojevi_1, brojevi_2))
# print(nova_lista)


# brojevi_1 = list(range(1, 10))
# brojevi_2 = list(range(1, 10))
# brojevi_3 = list(range(1, 20))

# nova_lista = list(zip(brojevi_3, brojevi_2, brojevi_1))
# print(nova_lista)


students = [
    'Pero Peric',
    'Ana Anic',
    'Iva Ivic',
    'Marko Markic'
]
subjects = [
    'Programming 1',
    'Math',
    'Databases 1',
    'Economy'
]
grades = [
    5, 3, 2, 4
]

print(list(zip(students, subjects, grades)))