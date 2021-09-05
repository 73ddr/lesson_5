with open("sal.txt", "r") as file:
    salary = []
    poor = []
    my_list = file.read().split('\n')
    for i in range(len(my_list)):
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        salary.append(i[1])
print(f"Оклад меньше 20000: {poor}, cредний оклад {sum(map(int, salary)) / len(salary)}")

