guest_name = input("What's your name? ")

filename = 'C:\\Users\\Stuffing\\Desktop\\lessons\\VSCODE'
filename += "\\Python__2020\\fiels_read_write\\guest.md"

with open(filename, 'a') as name:
    name.write(guest_name)

with open(filename, 'r') as obj:
    file = obj.read()
    print(file)
