#11-3
import unittest
class Employee():
    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
    def give_raise(self,money_plus = 5000):
        self.annual_salary += money_plus
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('lucien', 'evevce', 5000000)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 5005000)
    def test_give_custom_raise(self):
        self.employee.give_raise(1000000)
        self.assertEqual(self.employee.annual_salary,6000000)
unittest.main()