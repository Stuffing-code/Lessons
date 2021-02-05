class User():
    """Информация о пользователе"""
    
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describle_user(self):
        """Представление пользователя"""
        full_name = self.first_name + " " + self.last_name
        print(f"Name {full_name.title()}\nAge: {self.age} \
        \nGender: {self.gender.title()}")

    def greet_user(self):
        """Вывод персонального приветсвия пользователя"""
        print(f"Hellow {self.first_name.title()} {self.last_name}")


user_1 = User("Andrey", "Yarovenko", 25, "male")
user_1.describle_user()
user_1.greet_user()
