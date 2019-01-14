import NameGenK
from Species import animals, height_feet, height_inches
import random


    

class furry(NameGenK.personname):

    def __init__(self, gender, first='', last='', height_ft= None, height_in= None):
        self.height_ft = height_ft
        self.height_in = height_in
        self.gender = gender
        super().__init__(first=first, last=last)
        


    def height(self):
        pass
