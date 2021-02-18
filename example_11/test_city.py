import unittest
from city_function import get_city_country_name

class CityFunctionTestCase(unittest.TestCase):
    """Тесты для 'city_function.py."""
    def test_city_country(self):
        """Название типа 'Santiago, Chile' работают правильно?"""
        fiormatted_name = get_city_country_name('santiago', 'chile')
        self.assertEqual(fiormatted_name, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
