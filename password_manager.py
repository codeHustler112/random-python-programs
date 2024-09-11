#program stores password along with username , we will encrypt password


import getpass
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", 'rb') as file:
        key = file.read()
        return key

def view():
    with open("password.txt", 'r') as file:
        for line in file:
            data = line.strip()
            user, password = data.split(',')
            print(f"User: {user}, Password: {f.decrypt(password.encode()).decode()}")

def add():
    name = input("Name the account for which you want to create the password: ")
    passwd = getpass.getpass("Password: ").encode()
    token = f.encrypt(passwd)
    with open("password.txt", 'a') as file:
        file.write(f"{name},{token.decode()}\n")

# generate and save key
write_key()

# Load the key
key = load_key()
f = Fernet(key)

while True:
    mode = input("Would you like to view password or add password? Write 'add' for adding password or 'view' to view password, press 'q' to quit.\n")
    
    if mode == 'q':
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
       print("Invalid mode")
       continue
