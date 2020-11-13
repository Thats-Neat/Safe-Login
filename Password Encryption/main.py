import hashlib


def get_password(file):
    global hash
    with open(file, 'r') as f:
        hash = f.readline()
    return hash



def encrypt(text):
    hash = hashlib.md5(text.encode())
    textHash = hash.hexdigest()
    return textHash


def login():
    username = input('Username: ')
    password = input('Password: ')

    get_password('password.txt')

    if hash == encrypt(password):
        print('\npassword correct!')


def signup():
    ...


print('[1] Login')
print('[2] Signup')
menu = input('> ')

if menu == '1':
    login()
elif menu == '2':
    signup()
