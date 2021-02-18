import unittest
from city_function import get_city_country_name

class CityFunctionTestCase(unittest.TestCase):
    """Тесты для 'city_function.py."""
    def test_city_country(self):
        """Название типа 'Santiago, Chile' работают правильно?"""
        formatted_name = get_city_country_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Проверка работает ли функция правильно для 'Santiago, Chile - population 5000000'."""
        formatted_name = get_city_country_name('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
