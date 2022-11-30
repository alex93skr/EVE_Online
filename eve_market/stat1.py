import csv
from pprint import pprint

with open('orderset-90744.csv', newline='') as f:
    # with open('tst.csv', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

print(f'{len(data)=}')

# 10000032/types/4573/buy

for order in data:
    if order[1] == '17322':
        print(order)


# for order in data:
#     if order[1] == '4573' and order[11] == '10000032':
#         print(order)

# for order in data:
#     if int(order[4]) < int(order[5]):
#         print(order)