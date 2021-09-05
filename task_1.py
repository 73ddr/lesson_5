with open("new_file.txt", "w") as file:
    while True:
        user_answ = input("Напишите что-нибудь: ")
        file.write(user_answ + "\n")
        if not user_answ:
            break
