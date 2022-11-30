import csv
from pprint import pprint

with open('D:\code\eve\orderset.csv', newline='') as f:
    # with open('tst.csv', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

print(f'{len(data)=}')

# 	0 			1			2					3		4     5     6		  7			   8				9		  10	11			12
# ['6085387005', '47257', '2021-10-18T10:36:47Z', 'True', '3', '8',   '1', 	'355700.0',  '60004588',      'station', '90', '10000030', '90733']
# ['6055479918', '47257', '2021-10-18T08:59:50Z', 'True', '10', '20', '1', '355600.0', '1031084757448', '1',       '90', '10000030', '90733']
# ['6022083809', '47257', '2021-08-28T13:30:22Z', 'True', '16', '20', '1', '10010.0',  '60014779',      'region',  '90', '10000030', '90733']
#
#     ордер,       тип,        дата??,            продажа, остаток, кол-во, минобъем, цена,     stationID,      дистания  срок(дней)  регион
#
# False - продаваны
# True - покупатели


# False - продаваны
# True - покупатели



# for order in data:
#     if order[3] == 'False' and order[5] != '1':
#         print(order)




def time_stat():
    #
    # order[2][-1] != 'Z'   все z
    # order[2][-1] != 'Z'   все z

    # 2021-09-30T07:42:32Z

    # for order in data:
    #     if '2021-10-19' in order[2]:
    #         print(order)


    statist = {}

    for order in data:
        if order[2][11:13] not in statist:
            statist.update({order[2][11:13]: 1})
        else:
            statist[order[2][11:13]] += 1

    sorted_tuple = sorted(statist.items(), reverse=True, key=lambda x: x[1])

    pprint(sorted_tuple)


# time_stat()


def date_stat():
    statist = {}

    for order in data:
        if order[2][:10] not in statist:
            statist.update({order[2][:10]: 1})
        else:
            statist[order[2][:10]] += 1

    sorted_tuple = sorted(statist.items(), reverse=True, key=lambda x: x[1])

    pprint(sorted_tuple)


def regions():
    with open('regions.csv', newline='') as f:
        # with open('tst.csv', newline='') as f:
        reader = csv.reader(f)
        _regions = list(reader)
        _regions = {k: v for k, v in _regions}
        pprint(regions)

    statist = {}

    for order in data:
        if order[3] != 'False':
            if order[11] not in statist:
                statist.update({order[11]: 1})
            else:
                statist[order[11]] += 1

    print(f'{len(statist)=}')

    sorted_tuple = dict(sorted(statist.items(), reverse=True, key=lambda x: x[1]))

    for n in sorted_tuple:
        print(n, sorted_tuple[n], _regions[n])
