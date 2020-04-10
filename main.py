from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    header = contacts_list.pop(0)
# print(type(contacts_list[0][5]))

# TODO 1: выполните пункты 1-3 ДЗ
contacts_list_new = [header]
patt_FIO = re.compile('[А-Я][а-я]*')
patt_tel = re.compile('(8|\+7)(\s*|)(\(|)(\d{3})(\)|)(\s*|-|)(\d{3})(-|)(\d{2})(-|)(\d{2})(\s*(\(|)(доб\.)\s*(\d*)|)')
for item in contacts_list:
    res_F = patt_FIO.findall(item[0])
    res_I = patt_FIO.findall(item[1])
    res_O = patt_FIO.findall(item[2])
    if len(res_F) == 2:
        item[1] = res_F[1]
        item[0] = res_F[0]
    if len(res_F) == 3:
        item[1] = res_F[1]
        item[2] = res_F[2]
        item[0] = res_F[0]
    if len(res_I) == 2:
      item[1] = res_I[0]
      item[2] = res_I[1]
    # print(type(item[5]))
    res_tel = patt_tel.sub(r'+7(\4)\7-\9-\11 \14\15', item[5])
    item[5] = res_tel
    item[6] = item[6].lower()

    print(item)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    # datawriter.writerows(contacts_list)
