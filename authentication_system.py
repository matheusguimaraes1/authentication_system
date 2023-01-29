import hashlib

registered_users = {}
current_user = None

def register_user():
    username = input("Insira um nome de usuário: ")
    password = input("Insira sua senha: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    registered_users[username] = hashed_password
    print(username + ", você foi registrado com sucesso!")

def login():
    global current_user
    username = input("Insira seu nome de usuário: ")
    password = input("Insira sua senha: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in registered_users and registered_users[username] == hashed_password:
        print("Bem vindo(a), " + username + "!")
        current_user = username
    else:
        print("Ops... parece que o nome de usuário ou a senha estão incorretos. Por favor, tente novamente.")

def logout():
    global current_user
    if current_user:
        print("Até logo, " + current_user + "!")
        current_user = None
    else:
        print("Não há usuário atualmente logado.")

def display_current_user():
    if current_user:
        print("Usuário atual: " + current_user)
    else:
        print("Não há usuário atualmente logado.")

while True:
    print("1. Registrar usuário")
    print("2. Login")
    print("3. Encerrar sessão")
    print("4. Exibir usuário atual")
    print("5. Sair do programa")
    choice = int(input("Insira sua escolha: "))

    if choice == 1:
        register_user()
    elif choice == 2:
        login()
    elif choice == 3:
        logout()
    elif choice == 4:
        display_current_user()
    elif choice == 5:
        break
    else:
        print("Ops... escolha inválida.\nPor favor, tente novamente.")
