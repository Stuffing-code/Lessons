import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Тесты для 'employee.py."""

    def setUp(self):
        """Создание сотрудника и значения увеличения зарплаты."""
        self.my_employee = Employee('Andrey', 'Sokolov', 6000)
        self.increase_custom = 7000

    def test_default_raise(self):
        """Тест со стандартными значениями increased."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 11000)

    def test_give_custom_raise(self):
        """Тест с кастомным значением increased."""
        self.my_employee.give_raise(self.increase_custom)
        self.assertEqual(self.my_employee.salary, 13000)

if __name__ == '__main__':
    unittest.main()
