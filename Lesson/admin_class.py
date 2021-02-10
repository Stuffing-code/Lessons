from users_class import User

"""Набор классов для работы с админами."""


class Privileges:
    """Класс привелегий"""
    def __init__(self):
        self.privileges = ("create", "delete", "save")

    def show_privileges(self):
        """Список привелегий"""
        print(self.privileges)


class Admin(User):
    """Информация об администраторе"""

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()
