brojevi = list(range(1, 51))
# print(numbers)
def parni(x):
    return  x % 2 == 0

# parini_brojevi = list(filter(parni, brojevi))
# print(parini_brojevi)
# parini_brojevi = list(filter(lambda x: parni(x), brojevi))
# print(parini_brojevi)


parini_brojevi = list(filter(lambda x: x % 2 == 0, brojevi))
print(parini_brojevi)


kvadrati_brojeva = list(map(lambda x: x ** 2, brojevi))
print(kvadrati_brojeva)