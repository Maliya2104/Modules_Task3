import os
import csv_operations as csv

file_open = False
def main():
    print("""\nДля работы со мной у тебя есть следующие команды:
    ОТКРЫТЬ - будет совершена попытка открытия файл, путь к которому был указан,
    СОЗДАТЬ - написанная информация будет зафиксирована и сохранена в файле,
    СТОП - конец работы программы.
    
    Если файл был успешно открыт, то можно задействовать следующие команды:
    ВЫВОД - информация из файла будет выведена на экран,
    ДОБАВИТЬ - добавляет введённые данные вниз строки,
    ИЗМЕНИТЬ - указанная информация будет изменена,
    СОХРАНИТЬ - сохранение изменений в отдельный файл,
    УДАЛИТЬ - указанная информация будет удалена.\n""")
    check_input()

def check_input():
    us_input = ""
    while us_input != "СТОП":
        us_input = input("Введите команду: ").upper()
        if us_input == "ОТКРЫТЬ":
            open_file()
        elif us_input == "СОЗДАТЬ":
            new_file()
        elif file_open:
            if us_input == "ВЫВОД":
                csv.print_file()
            elif us_input == "ИЗМЕНИТЬ":
                edit_file()
            elif us_input == "СОХРАНИТЬ":
                save_file()
            elif us_input == "ДОБАВИТЬ":
                csv.add_record()
            elif us_input == "УДАЛИТЬ":
                str_num = input("Введите номер строки: ")
                try:
                    str_num = int(str_num)
                except:
                    print("Неверный формат")
                    return
                else:
                    csv.delete_rec(str_num)

def open_file():
    us_path = input("Введите путь к файлу *.cvs: ")
    if os.path.exists(us_path):
        try:
            csv.load_table(us_path)
        except:
            print("Не удалось открыть файл")
        else:
            global file_open
            file_open = True
    else:
        print("Путь не найден")
        return

def edit_file():
    str_num = input("Введите номер строки: ")
    try:
        str_num = int(str_num)
    except:
        print("Неверный формат")
        return
    parametr = input("Введите изменяемый параметр: ")
    result = input("Введите замену текущему значению: ")
    csv.change_file(str_num, parametr, result)

def save_file():
    new_path = input("Введите новый путь к файлу *.csv: ")
    try:
        csv.save_change(new_path)
    except:
        print("Неверный путь")
    else:
        print("Путь корректен")

def new_file():
    headers = input("Через пробел заголовки таблицы: ")
    try:
        head_l = [head.capitalize() for head in headers.split()]
        if len(head_l) > 1:
            csv.save_table(head_l)
        else:
            print("Введено недостаточное количество заголовков для создания таблицы.")
            return
    except:
        print("Выполнить запрос не удалось.")


if __name__ == "__main__":
    main()
