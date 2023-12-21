def get_average():
    with open("data.txt",'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    print(values)


a = get_average()