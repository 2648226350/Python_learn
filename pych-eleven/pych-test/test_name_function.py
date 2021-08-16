import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):#'test_' auto run
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgan','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgan Amadeus Mozart')
unittest.main()
