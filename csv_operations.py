import csv

data_dict = {}
max_len = []
headers = []
count = 0

def load_table(full_path):
    with open(full_path, encoding='utf-8-sig') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        global count
        count = 0
        count_c = 0
        index = 1
        for row in file_reader:
            if count == 0:
                global headers
                global max_len
                headers = row
                max_len = [len(head) for head in headers]
                count_c = len(headers)
            else:
                data_dict[index] = {}
                for i in range(count_c):
                    data_dict[index][headers[i]] = row[i]
                    max_len[i] = len(row[i]) if len(row[i]) > max_len[i] else max_len[i]
                index += 1
            count += 1
    print(f"Данные в количестве {count} строк успешно сохранены в словарь:")

def change_file(us_count, key, value):
    if us_count > count:
        print("Строчки с таким номером не найдено.")
        return
    try:
        data_dict[us_count][key] = value
    except:
        print("Изменение зафиксировать не удалось.")
    else:
        print("Изменение успешно зафиксировано во внутреннем представлении модуля.")

def print_file():
    string = "{:{fill}{align}{width}}"
    for ind, head in enumerate(headers):
        print(string.format(head, fill=' ', align='^', width=max_len[ind] + 2), end="| ")
    print()
    for ind, info in data_dict.items():
        for i, rec in enumerate(info.values()):
            print(string.format(str(rec), fill=' ', align='<', width=max_len[i] + 2), end="| ")
        print()

def add_record():
    new_rec = []
    global count
    count += 1
    for ind, column in enumerate(headers):
        new_rec.append(input(f"Введите значение столбца <{column}>: "))
    print(new_rec)
    data_dict[count] = {}
    for ind, column in enumerate(new_rec):
        try:
            data_dict[count][headers[ind]] = column
        except:
            print("Добавить данные не удалось.")
            return
        else:
            max_len[ind] = len(column) if len(column) > max_len[ind] else max_len[ind]
    print(f"Данные успешно добавлены в открытый файл. Не забудьте сохранить файл.")

def delete_rec(us_count):
    if us_count > count:
        print("Строчки с таким номером не найдено.")
        return
    try:
        del data_dict[us_count]
    except:
        print("Изменение зафиксировать не удалось.")
    else:
        print("Изменение успешно зафиксировано во внутреннем представлении модуля.")

def save_change(new_path):
    with open(new_path, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(headers)
        for ind, info in data_dict.items():
            file_writer.writerow([value for key, value in info.items()])
    print(f"Данные успешно сохранены в новый файл по адресу {new_path}.")

def save_table(headers_l):
    global headers, count, max_len, data_dict
    headers = headers_l
    count = 0
    max_len = [len(h) for h in headers]
    data_dict.clear()
    print("Заголовки для файла успешно созданы!")
