


def generate_full_name(first_name:str, last_name:str = '') -> str:
    # full_name = f('{first_name} {last_name}')
    # return full_name
    if last_name == '':
        return f'{first_name}'
    else:
        return f'{first_name} {last_name}' 
    

def podijeli(x=int, y=int) -> float:
    '''
    Funkcija koja vraca rezulrar dijeljenja, ako je y nula onda ce vratiit -1

    Keyword arguments:
    argument -- description
    Return: return_description
    '''
    if y != 0:
        return x / y
    else:
        return -1

    


firts_name = 'Pero'
last_name = 'Peric'
full_name = generate_full_name(firts_name, last_name)
print(full_name)

firts_name = 'Ana'
# last_name = 'Peric'
full_name = generate_full_name(firts_name)
print(full_name)


x = 5
y = 4
rezultat = podijeli(x, y)

if rezultat == -1:
    print(f'Nije moguce dijeliti s nula (y ima vrijednost {y})')
else:
    print(f'Rezultat dijeljenja je {rezultat:.3f}')