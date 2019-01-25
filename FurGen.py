import NameGenK
from Species import animals, height_feet, height_inches, bust_size
import random

class personname():
    def __init__(self, first = "", last = ""):
        self.first = first
        self.last = last
    
    def set_first(self, first: str):
        self.first = first.capitalize()
    
    def set_last(self, last: str):
        self.last = last.capitalize()
    

class furry(personname):

    def __init__(self, gender):
        
        self.animal = random.choice(animals)
        self.height_ft = random.randint(1,8)
        self.height_in = random.randint(0, 11)

        name = NameGenK.namegen(sex = gender[0].lower(), lastname = True)
        self.first = name.first
        self.last = name.last
            
        if gender[0].lower() == 'f':
            bust_size = random.choice(['A', 'B', 'C', 'D'])
        else:
            bust_size = None
        self.bust_size = bust_size
        self.gender = gender[0].lower()
    
    def getBust(self) -> str:
        if self.bust_size is None:
            return "No bust"
        else:
            return "{} cup".format(self.bust_size)
    
    def getHeight(self) -> str:
        heightprint = str(self.height_ft)
        if self.height_ft != 1:
            heightprint += " feet"
        else:
            heightprint += " foot"
        
        heightprint += " {}".format(str(self.height_in))
        if self.height_in != 1:
            heightprint += " inches"
        else:
            heightprint += " inch"
        
        return heightprint
    
    def getName(self) -> str:
        return self.first + " " + self.last

    def getSpecies(self) -> str:
        return self.animal

    def getSex(self):
        return self.gender


# gen = input("What gender do you want?")
# furry1 = furry(gen)
# print(furry1.getName())
# print(furry1.getSpecies())
# print(furry1.getHeight())
# print(furry1.getBust())

furries = []

for x in range(100):
    #populate the list with 100 furries, randomly decide the gender between m and f
    furries.append(furry(random.choice(['M', 'F'])))

furries.sort(key = lambda fur: fur.getName())

for fur in furries:
    #make a printout of the furries, giving full name, sex, species, and height
    print("{} - {} - {} - {} - {}".format(fur.getName().ljust(35), fur.getSex().upper().ljust(10), fur.getSpecies().ljust(15), fur.getHeight().ljust(25), fur.getBust()))
    