import random
from NameLists import male, female, last
from Species import animals

def male_namegen():
    male_group = []
    for x in range(1):
        male_name = random.choice(male).capitalize()+" "+random.choice(last).capitalize()
        male_group.append(male_name)
    print('Male Names: ')
    print("\n".join(male_group))

def female_namegen():
    female_group = []
    for x in range(1):
        female_name = random.choice(female).capitalize()+" "+random.choice(last).capitalize()
        female_group.append(female_name)
    print('Female Names:')
    print("\n".join(female_group))

def species_gen():
    species_group = []
    for x in range(1):
        species_name = random.choice(animals).capitalize()
        species_group.append(species_name)
    print('Species:')
    print("\n".join(species_group))

def namegen():
    while True:
        gender = input('[M]ale or [F]emale? ')
        if gender.upper() == 'M':
            male_namegen()
            species_gen()
        elif gender.upper() == 'F':
            female_namegen()
            species_gen()
        else:
            print('Please use M or F')
            continue
        break

namegen()
