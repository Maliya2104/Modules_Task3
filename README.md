                                  3 Задание. Практикума по программированию.
Тема задания: «Реализация собственного пакета модулей по манипулированию табличными данными».
ФИО: Иванова Мария Юрьевна
Группа: ТРПО24-3

Задание:
На базе модулей: csv, pickle и прямой работы с файлами реализовать следующий базовый функционал:

1.	функций load_table, save_table по загрузке/сохранению табличных данных во внутреннее представление модуля/из внутреннего представления модуля:
o	файла формата csv (отдельный модуль с load_table, save_table в рамках общего пакета)
o	файла формата pickle (отдельный модуль с load_table, save_table в рамках общего пакета), модуль использует структуру данных для представления таблицу, удобную автору работы.
o	текстового файла (только функция save_table сохраняющая в текстовом файле представление таблицы, аналогичное выводу на печать с помощью функции print_table()).
Примечание: внутреннее представление может базироваться на словаре, где по разным ключам хранятся ключевые «атрибуты» таблицы, а значения таблицы хранятся в виде вложенных списков. Студент может выбрать другое внутреннее представление таблицы (согласовав его с преподавателем), в том числе, студенты знакомые с ООП на Python, могут реализовать собственный класс для таблицы.
При определении api модулей максимально полно использовать возможности сигнатур функций на Python (значения по умолчанию, запаковка/распаковка, в т.ч. именованных параметров, возвращение множественных значений), интенсивно выполнять проверки и возбуждать исключительные ситуации.

2.	модуля с базовыми операциями над таблицами:
o	get_rows_by_number(start, [stop], copy_table=False) – получение таблицы из одной строки или из строк из интервала по номеру строки. Функция либо копирует исходные данные, либо создает новое представление таблицы, работающее с исходным набором данных (copy_table=False), таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.
o	get_rows_by_index(val1, … , copy_table=False) – получение новой таблицы из одной строки или из строк со значениями в первом столбце, совпадающими с переданными аргументами val1, … , valN. Функция либо копирует исходные данные, либо создает новое представление таблицы, работающее с исходным набором данных (copy_table=False), таким образом изменения, внесенные через это представления будут наблюдаться и в исходной таблице.
o	get_column_types(by_number=True) – получение словаря вида столбец:тип_значений. Тип значения: int, float, bool, str (по умолчанию для всех столбцов). Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.
o	set_column_types(types_dict, by_number=True) – задание словаря вида столбец:тип_значений. Тип значения: int, float, bool, str (по умолчанию для всех столбцов). Параметр by_number определяет вид значения столбец – целочисленный индекс столбца или его строковое представление.
o	get_values(column=0) – получение списка значений (типизированных согласно типу столбца) таблицы из столбца либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца)
o	get_value(column=0) – аналог get_values(column=0) для представления таблицы с одной строкой, возвращает не список, а одно значение (типизированное согласно типу столбца).
o	set_values(values, column=0) – задание списка значений values для столбца таблицы (типизированных согласно типу столбца) либо по номеру столбца (целое число, значение по умолчанию 0, либо по имени столбца).
o	set_value(column=0) – аналог set_values(value, column=0) для представления таблицы с одной строкой, устанавливает не список значений, а одно значение (типизированное согласно типу столбца).
o	print_table() – вывод таблицы на печать.
3.	Для каждой функции должно быть реализована генерация не менее одного вида исключительных ситуаций.

Результат выволнения кода:
![image](https://github.com/user-attachments/assets/cd78810e-46c6-4d54-bd0b-2db652c074d4)
![image](https://github.com/user-attachments/assets/1b0ac49c-d273-443a-af1c-149712678ed4)
![image](https://github.com/user-attachments/assets/18edeaea-818e-4a4e-a6f3-0f21896313f8)
![image](https://github.com/user-attachments/assets/0da0440a-c1e7-4f03-a3d3-63c1c7b81939)
![image](https://github.com/user-attachments/assets/55938b68-f8b0-4b1f-9cad-803cc88cc668)

