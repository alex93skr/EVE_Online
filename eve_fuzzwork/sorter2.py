import csv

with open('full.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(f'{len(data)=}')

_work_data = []

# for i in data:
#     if i[9] != 'inf':
#         _work_data += [i]

# print(data[0])

# ['1000002', '14866', '2400', '2400000', 'NAME____', '447000.0', '5000', '870.9', '25538', '628.125']

# <th>id</th>
# <th>LP</th>
# <th>Isk</th>
# <th>Item</th>
# <th>Other Requirements</th>
# <th>Other Cost</th>
# <th>Quantity</th>
# <th>Buy Price</th>
# <th>5% Volume</th>
# <th>isk/lp</th>

ZeroDivisionError = 0
ZeroDivisionError_corp = []

for i, _ in enumerate(data):

    if int(data[i][2]) == 0:
        ZeroDivisionError += 1

        if int(data[i][0]) not in ZeroDivisionError_corp:
            ZeroDivisionError_corp.append(int(data[i][0]))

        # print(_)

        continue

    _work_data.append([
        int(data[i][0]),  # corp
        int(data[i][1]),  # item
        int(data[i][2]),  # lp
        int(data[i][3]),  # Isk
        data[i][4],  # name
        float(data[i][5]),  # Other Cost
        int(data[i][6]),  # Quantity
        float(data[i][7]),  # Buy Price
        int(data[i][8]),  # 5% Volume
        # int(data[i][9]),    # isk/lp

        # переращет формулы
        ((float(data[i][7]) * int(data[i][6])) - float(data[i][5]) - int(data[i][3])) / int(data[i][2])

    ])

print(f'{len(_work_data)=}')

print(f'{ZeroDivisionError=}')
print(f'{ZeroDivisionError_corp=}')

# for n, _ in enumerate(_work_data):
# _work_data[n].append(float(_work_data[n][9]))
# print(n)

_work_data.sort(reverse=True, key=lambda i: i[9])

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
