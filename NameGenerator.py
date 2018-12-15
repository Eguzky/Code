import NameLists
import random


male_group = []
for x in range(6):
    from NameLists import male, last
    male_name = random.choice(male)+"  "+random.choice(last)
    male_group.append(male_name)
print(", ".join(male_group))

female_group = []
for x in range(6):
    from NameLists import female, last
    female_name = random.choice(female)+"  "+random.choice(last)
    female_group.append(female_name)
print(", ".join(female_group))