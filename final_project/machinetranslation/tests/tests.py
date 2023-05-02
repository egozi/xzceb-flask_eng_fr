import unittest

from translator import english_to_french, french_to_english

class TestTranslate(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("hello"), "Bonjour") # test when 2 is given as input the output is 4.
        self.assertEqual(french_to_english("Bonjour"), "Hello")  # test when 3.0 is given as input the output is 9.0.
        
unittest.main()
