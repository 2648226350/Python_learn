import unittest
#11-1&&11-2
from city_func import city_country
class NameTest(unittest.TestCase):
    def test_city_country(self):
        formatted_name = city_country('peiking','china')
        self.assertEqual(formatted_name,'Peiking China')
    def test_city_country_population(self):
        formatted_name = city_country('peiking','china','532w')
        self.assertEqual(formatted_name,'Peiking China-population 532w')
unittest.main()

