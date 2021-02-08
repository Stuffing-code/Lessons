current_users = ['Andrey', 'Sergey', 'Alina', 'Oleg', 'Gosha']
new_users = ['ANDREY', 'Jena', 'OleG', 'Anna', 'Tolik']
current_users_lower = [i.lower() for i in current_users]
for user in new_users:
    if user.lower() in current_users_lower:
        print(f'Sorry, name {user} is taken.')
    else:
        print(f'Name {user} avaible.')
