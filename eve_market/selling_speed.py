import pickle
from pprint import pprint
import datetime

REGION = 10000002
# TYPES = 'D:\code\eve\_types.json'
# STATIONS = 'D:\code\eve\_stations.json'
ORDERSET = 'D:\code\eve\orderset.pickle'


class SellingSpeed:
    def __init__(self, region):
        self.region = region

        # подгрузка
        self.evemarket = self.load_evemarket()
        print(len(self.evemarket))

        self.raw_data = {}

        self.go()

        # 	   0 			1			2					3		   4          5      6		  7			   8				9		    10	       11			12
        # ['6085387005', '47257', '2021-10-18T10:36:47Z', 'True',     '3',      '8',   '1', 	'355700.0',  '60004588',      'station', '    90',   '10000030', '90733']
        #     ордер,       тип,        дата??,            покупате, остаток, кол-во, минобъем,     цена,       stationID,      дистания  срок(дней)   регион    №
        # False - продаваны
        # True - покупатели



    def go(self):

        # _work_data = []

        # for order in self.evemarket:
        #     if int(order[0]) > 5975997688 and order[10] == '365':
        #         print(order)

        for order in self.evemarket:
            if not self.actual(order[2], order[10]):
            # if int(order[0]) > 5975997688 and order[10] == '365':
                print(order)


    def go2(self):
        # сортировка по id ордера

        _work_data = []

        for order in self.evemarket:

            # print([int(order[0])] + order[1:])
            _work_data.append([int(order[0])] + order[1:])


        _work_data.sort(key=lambda x: x[0])

        with open(f'_selling_speed_all.txt', "w", encoding='utf-8') as file:
            # file.write(_work_data)

            for i in _work_data:
                # print(i)
                # print(str(i[0]) + '\t' + '\t'.join(i[1:]))
                file.write(str(i[0]) + '\t' + '\t'.join(i[1:]) + "\n")

        print(len(_work_data))


    def go1(self):
        # сортировка по id ордера с условиями

        _work_data = []

        for order in self.evemarket:
            if order[3] == 'False' and order[10] != '365':
                # print(order[0])

                # _arr_tmp = [int(order[0]), order[1:]]

                _work_data.append(order)
                # orders_is = [order[0] for order in self.evemarket]
                # key = lambda x: x[1]

        _work_data.sort(key=lambda x: x[0])

        with open(f'_selling_speed.txt', "w", encoding='utf-8') as file:
            # file.write(_work_data)

            for i in _work_data:
                # print(i)

                file.write('\t'.join(i) + "\n")

        print(len(_work_data))

    # def data_selection(self):
    #
    #     for id_navy in id_navy_standard:
    #         for order in self.evemarket:
    #             if order[1] == id_navy and order[1] == self.region:
    #                 /////

    def load_evemarket(self):
        with open(ORDERSET, "rb") as read_file:
            return pickle.load(read_file)

    def actual(self, date, days):
        # print(date)

        y = int(date[:4])
        mo = int(date[5:7])
        d = int(date[8:10])
        h = int(date[11:13])
        mi = int(date[14:16])
        s = int(date[17:19])

        # print(y, mo, d, h, mi, s, sep='|')

        serv_h_delta = 3

        order_date = datetime.datetime(y, mo, d, h, mi, s)
        expired_date = order_date + datetime.timedelta(days=int(days)) + datetime.timedelta(hours=serv_h_delta)

        # print(order_date)
        # print(expired_date)
        # print(datetime.datetime.today() < expired_date)

        return datetime.datetime.today() < expired_date


SellingSpeed(REGION)
