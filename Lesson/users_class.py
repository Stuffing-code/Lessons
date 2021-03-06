"""Класс информации о пользователе."""


class User:
    """Информация о пользователе"""

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describle_user(self):
        """Представление пользователя"""
        full_name = self.first_name + " " + self.last_name
        print(f"Name {full_name.title()}\nAge: {self.age} \
        \nGender: {self.gender.title()}")

    def greet_user(self):
        """Вывод персонального приветсвия пользователя"""
        print(f"Hellow {self.first_name.title()} {self.last_name}")

    def increment_login_attempts(self):
        """Увеличивает попытки входа на 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Обнуляет счетчик попыток входа"""
        self.login_attempts = 0
