import json
import pickle
from pprint import pprint
import datetime

# "10000033": "The Citadel",
# "10000002": "The Forge",

# 10000032  Sinq Laison
# "10000037": "Everyshore",
# "10000064": "Essence",
# "10000068": "Verge Vendor",
# "10000044": "Solitude",
# "10000048": "Placid",

REGION = '10000064'
# TYPES = 'D:\code\eve\_types.json'
# STATIONS = 'D:\code\eve\_stations.json'
ORDERSET = 'D:\code\eve\orderset.pickle'


def load_evemarket():
    with open(ORDERSET, "rb") as read_file:
        return pickle.load(read_file)

with open("D:\code\eve\_stations.json", "r") as read_file:
    stations_names = json.load(read_file)


def trade_hub_find():
    market = load_evemarket()

    _stations = {}

    for order in market:
        if order[11] == REGION:
            if order[8] not in _stations:
                _stations[order[8]] = 1
            else:
                _stations[order[8]] += 1

    sorted_tuple = dict(sorted(_stations.items(), reverse=False, key=lambda x: x[1]))

    for n in sorted_tuple:
        try:
            print(n, sorted_tuple[n], stations_names[n])
        except:
            print(n, sorted_tuple[n], '-----')

    # Caslemon

    # pprint(_stations)


trade_hub_find()