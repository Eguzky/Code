import unittest
import NumberToWord

class TestNum(unittest.TestCase):

    def test_zero_word(self):
        result = NumberToWord.number_to_word(0)
        self.assertEquals(result, 'zero')

    def test_fifteen_word(self):
        result = NumberToWord.number_to_word(15)
        self.assertEquals(result, 'fifteen')

    def test_twenty_word(self):
        result = NumberToWord.number_to_word(20)
        self.assertEquals(result, 'twenty')

    def test_twenty_one_word(self):
        result = NumberToWord.number_to_word(21)
        self.assertEquals(result, 'twenty one')

    def test_tens_words(self):
        self.assertEquals(NumberToWord.number_to_word(34), 'thirty four')
        self.assertEquals(NumberToWord.number_to_word(56), 'fifty six')
        self.assertEquals(NumberToWord.number_to_word(85), 'eighty five')
        self.assertEquals(NumberToWord.number_to_word(42), 'fourty two')
        self.assertEquals(NumberToWord.number_to_word(22), 'twenty two')
        self.assertEquals(NumberToWord.number_to_word(55), 'fifty five')

    def test_hundreds_words(self):
        self.assertEquals(NumberToWord.number_to_word(100), 'one hundred')
        self.assertEquals(NumberToWord.number_to_word(134), 'one hundred thirty four')
        self.assertEquals(NumberToWord.number_to_word(256), 'two hundred fifty six')
        self.assertEquals(NumberToWord.number_to_word(385), 'three hundred eighty five')
        self.assertEquals(NumberToWord.number_to_word(442), 'four hundred fourty two')
        self.assertEquals(NumberToWord.number_to_word(522), 'five hundred twenty two')
        self.assertEquals(NumberToWord.number_to_word(655), 'six hundred fifty five')

    def test_big_number_words(self):
        self.assertEquals(NumberToWord.number_to_word(1000), 'one thousand')
        self.assertEquals(NumberToWord.number_to_word(1000000), 'one million')
        self.assertEquals(NumberToWord.number_to_word(1000000000), 'one billion')
        self.assertEquals(NumberToWord.number_to_word(1001001000), 'one billion one million one thousand')

    def test_tricky_number_words(self):
        self.assertEquals(NumberToWord.number_to_word(1500), 'one thousand five hundred')
        self.assertEquals(NumberToWord.number_to_word(1500000), 'one million five hundred thousand')
        self.assertEquals(NumberToWord.number_to_word(1500000000), 'one billion five hundred million')

    def test_the_big_one_word(self):
        self.assertEquals(NumberToWord.number_to_word(1583167458111), 'one trillion five hundred eighty three billion one hundred sixty seven million four hundred fifty eight thousand one hundred eleven')

    def test_one_hundred_fifteen_word(self):
        result = NumberToWord.number_to_word(115)
        self.assertEquals(result, 'one hundred fifteen')