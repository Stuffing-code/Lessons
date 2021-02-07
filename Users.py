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


class Privileges:
    """Класс привелегий"""
    def __init__(self):
        self.privileges = ("create", "delete", "save")

    def show_privileges(self):
        """Список привелегий"""
        return self.privileges


class Admin(User):
    """Информация об администраторе"""

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


Admin_1 = Admin(
    "Andrey",
    "Yarovenko",
    27,
    "male",
    )

print(Admin_1.privileges.show_privileges())
