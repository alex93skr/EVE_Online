import json
import pickle
import re

import win32clipboard
from prettytable import PrettyTable

# 10000048    placid
# 10000069    Black Rise
# 10000016    lonetrek
# 10000002   The Forge
# 10000032   додикса
# "10000064": "Essence",

REGION = 10000064
TYPES = 'D:\code\eve\_types.json'
STATIONS = 'D:\code\eve\_stations.json'
ORDERSET = 'D:\code\eve\orderset.pickle'


# ORDERSET = 'D:\code\eve\orderset-90807.csv'
# ORDERSET = 'D:\code\eve\orderset_cut10000002.csv'

# SHOPLISTTEST = {'Vexor': 1, 'AE-K Compact Drone Damage Amplifier': 3, 'Medium ACM Compact Armor Repairer': 1,
#                 'IFFA Compact Damage Control': 1, '50MN Y-T8 Compact Microwarpdrive': 1,
#                 'Drone Navigation Computer I': 1, 'Sensor Booster I': 1, 'F-12 Enduring Tracking Computer': 1,
#                 '250mm Carbide Railgun I': 2, 'Drone Link Augmentor I': 2, 'Medium Processor Overclocking Unit I': 1,
#                 'Medium Kinetic Armor Reinforcer I': 1, 'Medium Thermal Armor Reinforcer I': 1,
#                 'Federation Navy Hobgoblin': 3, 'Federation Navy Hammerhead': 3, 'Federation Navy Ogre': 2,
#                 'Optimal Range Script': 2, 'Tracking Speed Script': 1, 'Targeting Range Script': 1,
#                 'Scan Resolution Script': 1, 'Nanite Repair Paste': 10, 'Iron Charge M': 80}


class EveShopping:
    def __init__(self, sector, buyship=True):
        self.sector = str(sector)
        self.buyship = buyship

        # подгрузка
        self.shoplist = self.get_clipboard_data()
        if not self.shoplist: return
        # self.shoplist = SHOPLISTTEST
        self.stations = self.json_load(STATIONS)
        self.typeids = self.json_load(TYPES)
        self.typeids_revers = {self.typeids[i]: i for i in self.typeids}
        self.evemarket = self.load_evemarket()

        # рабочие
        self.raw_offer = {}
        self.big_basket = {}
        # self.summary_table = []
        # self.sum_line = {}

        self.summary_table = PrettyTable()
        self.preparation_raw_offer()
        self.preparation_summary_table()

        # итог
        print(self.summary_table)
        print()
        for station in self.station_sort_list[:8]:
            print(station, self.stations[station])

    def preparation_summary_table(self):
        """
        итоговые данные
        подготовка, вывод
        :return:
        """
        _len_shoplist = len(self.shoplist)
        # print(f'{_len_shoplist}')

        # список станции, от большего найденого к меньш
        _station_sort_list = []
        for count_found_items in range(_len_shoplist, -1, -1):
            # for count_found_items in range(_len_shoplist + 1):
            for station in self.raw_offer:
                if len(self.raw_offer[station]) == count_found_items:
                    _station_sort_list.append(station)

        self.station_sort_list = _station_sort_list

        # print(_station_sort_list)
        # print(len(_station_sort_list))
        # self.summary_table.add_row(_station_sort_list)

        # таблица настройки
        self.summary_table.field_names = [''] + _station_sort_list
        self.summary_table.align = "r"
        self.summary_table.align[''] = "l"

        from prettytable import MARKDOWN
        self.summary_table.set_style(MARKDOWN)

        # формирование строк для таблицы
        # каждая строка - по списку покупок
        for item in self.shoplist:
            _item_line = [item]
            _itemid = self.typeids_revers[item]

            for station in _station_sort_list:
                if _itemid in self.raw_offer[station]:

                    # закидывание мелких данных для корзины
                    self.sort_item_on_station(station, _itemid)

                    # линия с сумой закупки из корзины
                    # прификс [найдены все]
                    _line = f'{self.big_basket[station][_itemid][0]} {self.big_basket[station][_itemid][1]}'
                    _item_line.append(_line)

                else:
                    _item_line.append('')

            # затаблировать
            self.summary_table.add_row(_item_line)

        # подвал, сыммы итого по столбам
        _sum_line = ['']

        for station in _station_sort_list:
            _sum = sum(self.big_basket[station][item][1] for item in self.big_basket[station])
            _sum_line.append(_sum)

        # затаблировать
        self.summary_table.add_row(_sum_line)

    def sort_item_on_station(self, station, item):
        """
        формирование корзины

        :param station:
        :param item:
        :return:
        """

        item_need_name = self.typeids[item]
        need = self.shoplist[self.typeids[item]]
        basket_position = []
        basket_collected = False

        # сортировка по цене от дешевых
        sorted_tuple: list = sorted(self.raw_offer[station][item].items(), key=lambda x: x[0])

        for order in sorted_tuple:

            # хватает
            if need <= order[1]:
                # basket_sum = float(order[0]) * need
                basket_position.append([float(order[0]), need])
                basket_collected = True
                break
            # не хватает
            else:
                # basket_sum = float(order[0]) * need
                basket_position.append([float(order[0]), order[1]])
                need -= order[1]

        # print()

        # корзина с вариантами и суммами
        basket_sum = sum([i[0] * i[1] for i in basket_position])

        if station not in self.big_basket:
            self.big_basket[station] = {}

        self.big_basket[station][item] = [('!', '')[basket_collected], basket_sum, basket_position]

    # Vexor
    # 626
    # {'22000000.0': 2, '11830000.0': 10, '11300000.0': 5, '10270000.0': 28, '10330000.0': 46, '10230000.0': 1,
    #  '10240000.0': 6, '10080000.0': 13, '11850000.0': 10, '10730000.0': 4, '11000000.0': 1, '10410000.0': 3,
    #  '10980000.0': 3, '10440000.0': 2, '10470000.0': 9, '12000000.0': 6, '12420000.0': 14, '10670000.0': 3,
    #  '10660000.0': 2, '18000000.0': 17, '12290000.0': 5, '12280000.0': 14, '12460000.0': 1, '12450000.0': 1,
    #  '10990000.0': 9, '12200000.0': 1, '10300000.0': 2, '10390000.0': 2, '10370000.0': 2, '12100000.0': 12,
    #  '16000000.0': 6, '10490000.0': 5, '12310000.0': 83, '10290000.0': 1, '10450000.0': 10, '10280000.0': 2,
    #  '12070000.0': 3, '10100000.0': 6, '11380000.0': 2}

    def sorting_offer(self):
        '''

       !!! skip !!!

        :return:
        '''
        # pprint(self.raw_offer)

        _len_shoplist = len(self.shoplist)
        print(f'{_len_shoplist}')

        # найдено итемов на станции
        # for cound_found_items in range(_len_shoplist,-1,-1):
        for cound_found_items in range(_len_shoplist + 1):
            # print(cound_found_items)
            for station in self.raw_offer:
                len(self.raw_offer[station])
                if len(self.raw_offer[station]) == cound_found_items:
                    print('==============================================')
                    print(cound_found_items, 'items on station', station)

                    for item in self.raw_offer[station]:
                        self.sort_item_on_station(station, item)

    def preparation_raw_offer(self):
        """
        перебор всех ордеров из БД на входные условия
        :return:
        """

        for item in self.shoplist:
            # print(item, self.shoplist[item])
            # print(self.typeids_revers[item])

            for order in self.evemarket:
                if all([
                    order[1] == self.typeids_revers[item],
                    order[3] == 'False',
                    order[11] == self.sector
                ]):
                    self.add_raw_offer(order)

                    # print(order)

        # pprint(self.raw_offer)

        # False - продаваны
        # True - покупатели

        # 	   0 			1			2					3		4     5     6		  7			   8				9		  10	11			12
        # ['6085387005', '47257', '2021-10-18T10:36:47Z', 'True', '3', '8',   '1', 	'355700.0',  '60004588',      'station', '90', '10000030', '90733']
        # ['6055479918', '47257', '2021-10-18T08:59:50Z', 'True', '10', '20', '1', '355600.0', '1031084757448', '1',       '90', '10000030', '90733']
        # ['6022083809', '47257', '2021-08-28T13:30:22Z', 'True', '16', '20', '1', '10010.0',  '60014779',      'region',  '90', '10000030', '90733']
        #
        #     ордер,       тип,        дата??,            покупате, остаток, кол-во, минобъем, цена, stationID,      дистания  срок(дней)  регион
        #

    def add_raw_offer(self, order):
        """
        сырые данные из ордера

        :param order:
        :return:
        """

        # 1 итем
        # 4 остаток
        # 6 минимум колво покупки
        # 7 цена
        # 8 станция

        item = order[1]
        amount = order[4]
        minamount = order[6]
        price = float(order[7])
        station = order[8]

        # станция
        if station not in self.raw_offer:
            self.raw_offer[station] = {}

        # итем
        if item not in self.raw_offer[station]:
            self.raw_offer[station][item] = {}

        # цена : колво
        if price not in self.raw_offer[station][item]:
            self.raw_offer[station][item][price] = int(amount)
        else:
            self.raw_offer[station][item][price] += int(amount)

    # def load_evemarket(self):
    #     with open(ORDERSET, newline='', encoding='utf-8') as f:
    #         reader = csv.reader(f, delimiter='\t')
    #         evemarket = list(reader)
    #     print(f'load {len(evemarket)=}')
    #     return evemarket

    def load_evemarket(self):
        with open(ORDERSET, "rb") as read_file:
            return pickle.load(read_file)

    def json_load(self, file):
        with open(file, "r") as read_file:
            return json.load(read_file)

    def get_clipboard_data(self):
        """
        взять их буфера
        :return:
        """
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        # print(repr(data))
        # print(data)
        # data = data.replace('\r\n\r\n', '\r\n')
        # print(type(data))

        if data[0] != '[':
            return print('incorrect information in Clipboard')

        # list1 = data.split('\r\n')

        # print(list1)

        def count_cut(line):
            """
            вырезать кол-во
            :param line:
            :return:
            """
            res = re.search(r' x\d+$', line)

            if res:
                return line[:res.span()[0]], int(res.group(0)[2:])
            else:
                return line, 1

        shoplist = {}

        if self.buyship:
            shoplist[data[1: data.find(',')]] = 1

        for line in data.split('\r\n'):
            if line == '' or line[0] == '[':
                continue

            _count_cut = count_cut(line)
            # print(_count_cut)

            if _count_cut[0] not in shoplist:
                shoplist.update({_count_cut[0]: _count_cut[1]})
            else:
                shoplist[_count_cut[0]] += 1

        # pprint(shoplist)

        return shoplist


EveShopping(REGION, buyship=True)
# print(EveShopping(10000002).get_clipboard_data())
