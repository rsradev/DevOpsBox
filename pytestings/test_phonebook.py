import unittest
 
from phonebook import Phonebook

class Phonebook:
    pass


class PhonebookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = Phonebook()