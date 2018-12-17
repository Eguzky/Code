import random
from NameLists import male, female, last

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

def namegen():
    input('[M]ale or [F]emale?')