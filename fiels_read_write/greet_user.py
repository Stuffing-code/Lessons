import json

filename = 'C:\\Users\\Stuffing\\Desktop\\lessons\\VSCODE'
filename += "\\Python__2020\\username.json"

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
