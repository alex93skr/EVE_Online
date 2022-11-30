import csv

with open('D:\code\eve\orderset.csv', newline='') as f:
    # with open('tst.csv', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

print(f'{len(data)=}')


# Sinq Laison

#
# 6055051617	47257	2021-08-08T18:16:33Z	False	36	43	1	902200.0	1031084757448	region	90	10000030	90733
# 6060589414	16467	2021-08-16T16:05:21Z	False	61	61	1	138400.0	1031084757448	region	90	10000030	90733
#
# order[2][-1] != 'Z'   все z
# order[2][-1] != 'Z'   все z

# 2021-09-30T07:42:32Z

# for order in data:
#     if '2021-10-19' in order[2]:
#         print(order)


# for order in data:
#     if order[3] == 'False' and order[5] != '1':
#         print(order)

# False - продаваны
# True - покупатели

# продаваны мин объем всегда 1
# покупатели  мин объем всегда не оьязательно 1

# for order in data:
#     if order[3] == 'False' and order[5] != '1':
#         print(order)



# не компы  / топ товары  / ордеры / количество
def sell_ppl():
    # 10 		{'365': 452460, '90': 815040, '7': 13810, '30': 38098, '14': 12359, '1': 2131, '3': 6613, '0': 34}

    with open('typeids.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        _types = list(reader)
        _types = {k: v for k, v, _ in _types}
        # pprint(_types)

    order_count = {}
    value_count = {}

    for order in data:
        if order[10] != '365':
            if order[3] == 'False':
                if order[1] not in order_count:
                    order_count.update({order[1]: 1})
                    value_count.update({order[1]: int(order[5])})
                else:
                    order_count[order[1]] += 1
                    value_count[order[1]] += int(order[5])

    sorted_tuple = dict(sorted(value_count.items(), reverse=True, key=lambda x: x[1]))

    for n in sorted_tuple:
        print(n, sorted_tuple[n], _types[n])


sell_ppl()




# сколько продают компы, по сроку ордера
# сколько люди
def sell_pc_ppl():
    # 10 		{'365': 452460, '90': 815040, '7': 13810, '30': 38098, '14': 12359, '1': 2131, '3': 6613, '0': 34}

    with open('typeids.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        _types = list(reader)
        _types = {k: v for k, v, _ in _types}
        # pprint(_types)

    order_count = {}
    value_count = {}

    for order in data:
        if order[10] == '365':
            if order[3] == 'False':
                if order[1] not in order_count:
                    order_count.update({order[1]: 1})
                    value_count.update({order[1]: int(order[5])})
                else:
                    order_count[order[1]] += 1
                    value_count[order[1]] += int(order[5])

    sorted_tuple = dict(sorted(value_count.items(), reverse=True, key=lambda x: x[1]))

    for n in sorted_tuple:
        print(n, sorted_tuple[n], _types[n])


# sell_pc_ppl()


def sell_top():
    with open('typeids.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        _types = list(reader)
        _types = {k: v for k, v, _ in _types}
        # pprint(_types)

    order_count = {}
    value_count = {}

    for order in data:
        if order[3] == 'False':
            if order[1] not in order_count:
                order_count.update({order[1]: 1})
                value_count.update({order[1]: int(order[5])})
            else:

                # if order[1] == '17338':
                #     print(value_count[order[1]], '+', order[4])

                order_count[order[1]] += 1
                value_count[order[1]] += int(order[5])

    sorted_tuple = dict(sorted(value_count.items(), reverse=True, key=lambda x: x[1]))

    # pprint(sorted_tuple)

    for n in sorted_tuple:
        print(n, sorted_tuple[n], _types[n])

# sell_top()
