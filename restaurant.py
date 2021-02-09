"""Набор классов предстовления общепита."""


class Restaurant():
    """Простая модель ресторана."""

    def __init__(self, restaurant_name, cuisine_type):
        """Иницализирует название и тип кухни ресторана."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Описание ресторана."""
        print(f"Restaurant {self.restaurant_name}", end=" ")
        print(f"{self.cuisine_type.lower()} cuisine.")

    def open_restaurant(self):
        """Информация о том что ресторан открыт."""
        print(f"Restaurant {self.restaurant_name} is open.")

    def set_number_served(self, value):
        """Задает количество обслуженных гостей."""
        self.number_served = value

    def increment_number_served(self, value):
        """Увеличивает количествообслуженных посетителей."""
        self.number_served += value


class IceCreamStand(Restaurant):
    """Класс мороженого."""

    def __init__(self, *flavors):
        """Вкусы мороженого."""
        self.flavors = flavors

    def get_flavors(self):
        """Get flavors."""
        print("We can offer for desert: ")
        for flavor in self.flavors:
            print(flavor)
