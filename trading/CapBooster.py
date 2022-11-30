import pickle

standard_weight = {
    25: 1,
    50: 2,
    75: 3,
    100: 4,
    150: 6,
    200: 8,
    400: 16,
    800: 32,
    3200: 128}

navy_weight = {
    25: 0.75,
    50: 1.5,
    75: 2.25,
    100: 3,
    150: 4.5,
    200: 6,
    400: 12,
    800: 24,
    3200: 96
}

id_standard_navy = {
    '263': '33330',
    '264': '33332',
    '3552': '33334',
    '3554': '31982',
    '11283': '31990',
    '11285': '31998',
    '11287': '32006',
    '11289': '32014',
    '41489': '41490'
}

id_navy_standard = {
    '33330': '263',
    '33332': '264',
    '33334': '3552',
    '31982': '3554',
    '31990': '11283',
    '31998': '11285',
    '32006': '11287',
    '32014': '11289',
    '41490': '41489'
}

# 10000048    placid
# 10000069    Black Rise
# 10000016    lonetrek
# 10000002   The Forge

REGION = 10000002
# TYPES = 'D:\code\eve\_types.json'
# STATIONS = 'D:\code\eve\_stations.json'
ORDERSET = 'D:\code\eve\orderset.pickle'


class CapBooster:
    def __init__(self, region):
        self.region = region

        # подгрузка
        self.evemarket = self.load_evemarket()

        self.raw_data = {}


        # 	   0 			1			2					3		4     5     6		  7			   8				9		  10	11			12
        # ['6085387005', '47257', '2021-10-18T10:36:47Z', 'True', '3', '8',   '1', 	'355700.0',  '60004588',      'station', '90', '10000030', '90733']
        #     ордер,       тип,        дата??,            покупате, остаток, кол-во, минобъем, цена, stationID,      дистания  срок(дней)  регион
        # False - продаваны
        # True - покупатели


    def data_selection(self):

        for id_navy in id_navy_standard:
            for order in self.evemarket:
                if order[1] == id_navy and order[1] == self.region:
                    /////

    def load_evemarket(self):
        with open(ORDERSET, "rb") as read_file:
            return pickle.load(read_file)


CapBooster(REGION)
