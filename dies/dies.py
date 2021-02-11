from random import randint


class Die:
    """Класс предстовляющий бросок кубика."""

    def __init__(self, sides=6):
        """[Конструктор создания кубика]

        Args:
            sides (int, optional): [количество граней]. Defaults to 6.
        """
        self.sides = sides

    def roll_side(self):
        """Бросок кубика"""
        return randint(1, self.sides)
