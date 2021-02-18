class Employee():
    """Класс представления сотрудников."""

    def __init__(self, first_name, last_name, salary):
        """
        Создание сотрудника с именем, фамилией и годовым окладом.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, increase=5000):
        """
        Увеличивает годовую зарплату стандартно на 5000$
        или на колличествое заданое вручную.
        """
        self.salary += increase
