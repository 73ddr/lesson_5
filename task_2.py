def count_info():
    try:
        with open("new_file.txt", encoding = "utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                result = (f"Количество строк {len(my_list)}. в {i + 1} строке {len(new_l)} слов")
                print(result)
    except FileNotFoundError:
        return "Файл не найден"


count_info()

