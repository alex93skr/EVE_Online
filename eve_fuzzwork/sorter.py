import csv

with open('1634323955.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)




print(len(data))

_work_data = []

for i in data:
    if i[9] != 'inf':
        _work_data += [i]

print(len(_work_data))

for n, _ in enumerate(_work_data):
    _work_data[n].append(float(_work_data[n][9]))
    # print(n)

_work_data.sort(reverse=True, key=lambda i: i[10])

# for i in _work_data[:50]:
#     print(i)


from prettytable import PrettyTable
mytable = PrettyTable()
# имена полей таблицы
# mytable.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# добавление списка строк
mytable.add_rows(
    _work_data[:500]
)

mytable.align = "l"

print(mytable)