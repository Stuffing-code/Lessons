import json


def get_store_favorite_number():
    """Проверяет есть ли уже записаны числа."""
    filename = "C:\\Users\\Stuffing\\Desktop\\lessons\\VSCODE\\Python__2020\\lesson_10\\favorite_number.json"
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def get_number():
    """Запрос любимого числа."""
    favorite_number = get_store_favorite_number()
    if favorite_number:
        print(f'I know your favorite number! This is {favorite_number}!')
    else:
        number = int(input("What's your favorite number? "))
        filename = "favorite_number.json"
        with open(filename, 'w') as f:
            json.dump(number, f)


get_number()
