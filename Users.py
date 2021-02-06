class User():
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


class Admin(User):
    """Информация об администраторе"""

    def __init__(self, first_name, last_name, age, gender, *privileges):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = privileges

    def show_privileges(self):
        """Список привелегий"""
        return self.privileges


Admin_1 = Admin(
    "Andrey",
    "Yarovenko",
    27,
    "male",
    "diashdaskn",
    "kasnfas;lknd"
    )
print(Admin_1.show_privileges())
# Admin_1.show_privileges()

# user_1 = User("Andrey", "Yarovenko", 25, "male")
# user_1.describle_user()
# user_1.greet_user()

# user_2 = User("Alina", "Kopysova", 18, "female")
# user_2.increment_login_attempts()
# user_2.increment_login_attempts()
# user_2.increment_login_attempts()
# user_2.increment_login_attempts()
# user_2.increment_login_attempts()
# print(user_2.login_attempts)
# user_2.reset_login_attempts()
# print(user_2.login_attempts)
# user_2.increment_login_attempts()
# print(user_2.login_attempts)
