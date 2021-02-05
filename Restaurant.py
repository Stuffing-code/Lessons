class Restaurant():
    """
    Простая модель ресторана
    """
    
    def __init__(self, restaurant_name, cuisine_type):
        """Иницализирует название и тип кухни ресторана"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Описание ресторана"""
        print(f"Restaurant: {self.restaurant_name}! {self.cuisine_type} cuisine")
    
    def open_restaurant(self):
        """Информация о том что ресторан открыт"""
        print(f"Restaurant {self.restaurant_name} is open")

    def set_number_served(self, value):
        """Задает количество обслуженных гостей"""
        self.number_served = value

    def increment_number_served(self, value):
        """Увеличивает количествообслуженных посетителей"""
        self.number_served += value


restaurant = Restaurant("Bobo", "Azia")
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(70)
print(restaurant.number_served)
