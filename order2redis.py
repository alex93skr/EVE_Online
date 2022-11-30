import pickle

import redis

r = redis.Redis(decode_responses=True, host='localhost', port=6379, db=0)

# _arr = {111112: 222222, 3333332: 4444444, 55555552: 6666666}
# print(r.hset('001', mapping=_arr))

# print(r.hmset('pypa', _arr))
# print(r.hgetall("pypa"))
# print(r.hget("pypa", '11111'))
# print(r.hlen("pypa"))

# 	0 			1			2					3		4     5     6		  7			   8				9		  10	11			12
# ['6085387005', '47257', '2021-10-18T10:36:47Z', 'True', '3', '8',   '1', 	'355700.0',  '60004588',      'station', '90', '10000030', '90733']
# ['6055479918', '47257', '2021-10-18T08:59:50Z', 'True', '10', '20', '1', '355600.0',     '1031084757448', '1',       '90', '10000030', '90733']
# ['6022083809', '47257', '2021-08-28T13:30:22Z', 'True', '16', '20', '1', '10010.0',      '60014779',      'region',  '90', '10000030', '90733']
#
#     ордер,       тип,        дата??,            продажа, остаток, кол-во, минобъем, цена,     stationID,   дистания  срок(дней)  регион
#

with open('D:\code\eve\orderset.pickle', "rb") as read_file:
    orderset = pickle.load(read_file)

# for order in orderset:
#     # print(order)
#     _order = {
#         'type': order[1],
#         'date': order[2],
#         'buyer': order[3],
#         'rem': order[4],
#         'max': order[5],
#         'min': order[6],
#         'price': order[7],
#         'station': order[8],
#         'distance': order[9],
#         'term': order[10],
#         'region': order[11],
#         'set': order[12],
#     }
#
#     r.hset(order[0], mapping=_order)


with r.pipeline() as pipe:
    for order in orderset:
        _order = {
            'type': order[1],
            'date': order[2],
            'buyer': order[3],
            'rem': order[4],
            'max': order[5],
            'min': order[6],
            'price': order[7],
            'station': order[8],
            'distance': order[9],
            'term': order[10],
            'region': order[11],
            'set': order[12],
        }
        pipe.hset(order[0], mapping=_order)
    # for h_id, hat in hats.items():
    #     pipe.hmset(h_id, hat)
    pipe.execute()
    r.bgsave()





