import csv
from pprint import pprint

import requests




def load_csv(file):
    with open(file, newline='') as f:
        # with open('tst.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        datacsv = list(reader)
        print(f'{len(datacsv)=}')
    return datacsv


def esi_jump_in_reg():
    # прыжки за час в регионе
    # regionID,constellationID,solarSystemID,solarSystemName ....    SS
    #     0           1               2               3             21
    datacsv = load_csv('D:\code\eve\_data\mapSolarSystems.csv')
    print(len(datacsv))


    # esi = 'https://esi.evetech.net/latest/universe/system_kills/'
    esi = 'https://esi.evetech.net/latest/universe/system_jumps/'

    params = {}
    r = requests.get(esi, params=params)
    system_kills = r.json()
    # pprint(system_kills)
    print(type(system_kills))

    # for sys_kill_line in system_kills:
    #     print(sys_kill_line)
    #     print(type(sys_kill_line['system_id'])

    # "10000033": "The Citadel",
    # "10000002": "The Forge",

    # 10000032  Sinq Laison
    # "10000037": "Everyshore",
    # "10000064": "Essence",
    # "10000068": "Verge Vendor",
    # "10000044": "Solitude",
    # "10000048": "Placid",

    _reg = '10000064'
    _res_arr = []

    for system_csv_line in datacsv:
        # print(system)
        if system_csv_line[0] == _reg:
            system_csv_id = system_csv_line[2]

            system_csv_ss = round(float(system_csv_line[21]), 1)

            # скип если маньше
            if system_csv_ss > 0.4:
                continue

            # print(system_csv_id, system_csv_line[3], system_csv_line[21], system_csv_ss)

            for sys_kill_line in system_kills:
                if str(sys_kill_line['system_id']) == system_csv_id:
                    # print(system_csv_id, system_csv_line[3], system_csv_ss, sys_kill_line['npc_kills'])

                    # _res_arr.append([system_csv_id, system_csv_line[3], sys_kill_line['npc_kills']])
                    _res_arr.append([system_csv_id, system_csv_line[3], sys_kill_line['ship_jumps']])

    sorted_tuple: list = sorted(_res_arr, key=lambda x: x[2], reverse=True)

    pprint(sorted_tuple)

esi_jump_in_reg()

def esi_npc_kills_in_reg():
    # убито нпц за час в регионе

    # regionID,constellationID,solarSystemID,solarSystemName ....    SS
    #     0           1               2               3             21
    datacsv = load_csv('D:\code\eve\_data\mapSolarSystems.csv')
    print(len(datacsv))


    esi = 'https://esi.evetech.net/latest/universe/system_kills/'
    # esi = 'https://esi.evetech.net/latest/universe/system_jumps/'

    params = {}
    r = requests.get(esi, params=params)
    system_kills = r.json()
    # pprint(system_kills)
    print(type(system_kills))

    # for sys_kill_line in system_kills:
    #     print(sys_kill_line)
    #     print(type(sys_kill_line['system_id'])

    _reg = '10000032'
    _res_arr = []

    for system_csv_line in datacsv:
        # print(system)
        if system_csv_line[0] == _reg:
            system_csv_id = system_csv_line[2]

            system_csv_ss = round(float(system_csv_line[21]), 1)

            if system_csv_ss <= 0.5:
                continue

            # print(system_csv_id, system_csv_line[3], system_csv_line[21], system_csv_ss)

            for sys_kill_line in system_kills:
                if str(sys_kill_line['system_id']) == system_csv_id:
                    # print(system_csv_id, system_csv_line[3], system_csv_ss, sys_kill_line['npc_kills'])

                    _res_arr.append([system_csv_id, system_csv_line[3], sys_kill_line['npc_kills']])
                    # _res_arr.append([system_csv_id, system_csv_line[3], sys_kill_line['ship_jumps']])

    sorted_tuple: list = sorted(_res_arr, key=lambda x: x[2], reverse=True)

    pprint(sorted_tuple)

# esi_npc_kills_in_reg()