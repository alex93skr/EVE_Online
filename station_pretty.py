import csv
import json
from pprint import pprint


def load_csv(file):
    with open(file, newline='') as f:
        # with open('tst.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        datacsv = list(reader)
        # print(f'{len(datacsv)=}')
    return datacsv



def print_smart_json(data):

    print('{')

    # "10000001": {	    "20000001": {	"30000001": {	"faction": "500007","name": "Tanoo","security": "0.8583240688"},

    prev_reg = None
    prev_cel = None

    for reg in data:


        for cel in data[reg]:

            for sys in data[reg][cel]:

                # print(reg, prev_reg)
                # print(cel, prev_cel)



                if prev_reg != reg:
                    print('"', reg, '": {\t', sep='', end='')
                else:
                    print('\t\t\t\t', sep='', end='')

                if prev_cel != cel:
                    print('"',cel, '": {\t', sep='', end='')
                else:
                    print('\t\t\t\t', sep='', end='')

                # print('"', reg, '": {\t"', cel, '": {\t"', sys, '\t"name": "', data[reg][cel][sys]["name"], '", \t"security": "', data[reg][cel][sys]["security"], '", \t"faction": "', data[reg][cel][sys]["faction"], '"},', sep='', end='')

                # print(sys, '\t"name": "', data[reg][cel][sys]["name"], '", \t"security": "', data[reg][cel][sys]["security"], '", \t"faction": "', data[reg][cel][sys]["faction"], '"},', sep='', end='')
                print('"', sys, '": {\t"name": "', data[reg][cel][sys]["name"], '", \t"security": "', data[reg][cel][sys]["security"], '", \t"faction": "', data[reg][cel][sys]["faction"], '"},', sep='')

                prev_cel = cel
                prev_reg = reg


    print('}')



def go():
    _res_data = {}

    # regionID,constellationID,solarSystemID,solarSystemName ....    security, faction
    #     0           1               2               3             21            22
    datacsv = load_csv('D:\code\eve\map111111.csv')
    # print(len(datacsv))

    # region, const, solar, name, ss, faction

    # print(datacsv[0])

    for line in datacsv[1:]:
        # print(line)
        region, constellation, system, name, security, faction = line[0], line[1], line[2], line[3], line[21], line[22]

        # _res_data.update({region: {constellation: {system: {
        #     'name': name, 'security': security, 'faction': faction
        # }}}})

        if region not in _res_data:
            _res_data[region] = {}

        if constellation not in _res_data[region]:
            _res_data[region][constellation] = {}

        _res_data[region][constellation][system] = {
            'name': name, 'security': security, 'faction': faction
        }

    # pprint(_res_data)

    # with open("_systems.json", "w") as write_file:
    #     json.dump(_res_data, write_file, sort_keys=True, indent=1)

    print_smart_json(_res_data)

go()
