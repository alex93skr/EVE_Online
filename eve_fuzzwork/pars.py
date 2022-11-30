import asyncio
import csv

import aiohttp
from bs4 import BeautifulSoup
from bs4 import element

corp = {'1000002': 'CBD Corporation', '1000003': 'Prompt Delivery', '1000004': 'Ytiri',
        '1000005': 'Hyasyoda Corporation', '1000006': 'Deep Core Mining Inc.', '1000007': 'Poksu Mineral Group',
        '1000008': 'Minedrill', '1000009': 'Caldari Provisions', '1000010': 'Kaalakiota Corporation',
        '1000011': 'Wiyrkomi Corporation', '1000012': 'Top Down', '1000013': 'Rapid Assembly', '1000014': 'Perkone',
        '1000015': 'Caldari Steel', '1000016': 'Zainou', '1000017': 'Nugoeihuvi Corporation',
        '1000018': 'Echelon Entertainment', '1000019': 'Ishukone Corporation', '1000020': 'Lai Dai Corporation',
        '1000021': 'Zero-G Research Firm', '1000022': 'Propel Dynamics', '1000023': 'Expert Distribution',
        '1000024': 'CBD Sell Division', '1000025': 'Sukuuvestaa Corporation', '1000026': 'Caldari Constructions',
        '1000027': 'Expert Housing', '1000028': 'Caldari Funds Unlimited', '1000029': 'State and Region Bank',
        '1000030': 'Modern Finances', '1000031': 'Chief Executive Panel', '1000032': 'Mercantile Club',
        '1000033': 'Caldari Business Tribunal', '1000034': 'House of Records', '1000035': 'Caldari Navy',
        '1000036': 'Internal Security', '1000037': 'Lai Dai Protection Service', '1000038': 'Ishukone Watch',
        '1000039': 'Home Guard', '1000040': 'Peace and Order Unit', '1000041': 'Spacelane Patrol',
        '1000042': 'Wiyrkomi Peace Corps', '1000043': 'Corporate Police Force',
        '1000044': 'School of Applied Knowledge', '1000045': 'Science and Trade Institute',
        '1000046': 'Sebiestor Tribe', '1000047': 'Krusual Tribe', '1000048': 'Vherokior Tribe',
        '1000049': 'Brutor Tribe', '1000050': 'Republic Parliament', '1000051': 'Republic Fleet',
        '1000052': 'Republic Justice Department', '1000053': 'Urban Management',
        '1000054': 'Republic Security Services', '1000055': 'Minmatar Mining Corporation',
        '1000056': 'Core Complexion Inc.', '1000057': 'Boundless Creation', '1000058': 'Eifyr and Co.',
        '1000059': 'Six Kin Development', '1000060': 'Native Freshfood', '1000061': 'Freedom Extension',
        '1000062': 'The Leisure Group', '1000063': 'Amarr Constructions', '1000064': 'Carthum Conglomerate',
        '1000065': 'Imperial Armaments', '1000066': 'Viziam', '1000067': 'Zoar and Sons',
        '1000068': 'Noble Appliances',
        '1000069': 'Ducia Foundry', '1000070': 'HZO Refinery', '1000071': 'Inherent Implants',
        '1000072': 'Imperial Shipment', '1000073': 'Amarr Certified News', '1000074': 'Joint Harvesting',
        '1000075': 'Nurtura', '1000076': 'Further Foodstuffs', '1000077': 'Royal Amarr Institute',
        '1000078': 'Imperial Chancellor', '1000079': 'Amarr Civil Service', '1000080': 'Ministry of War',
        '1000081': 'Ministry of Assessment', '1000082': 'Ministry of Internal Order',
        '1000083': 'Amarr Trade Registry',
        '1000084': 'Amarr Navy', '1000085': 'Court Chamberlain', '1000086': 'Emperor Family',
        '1000087': 'Kador Family',
        '1000088': 'Sarum Family', '1000089': 'Kor-Azor Family', '1000090': 'Ardishapur Family',
        '1000091': 'Tash-Murkon Family', '1000092': 'Civic Court', '1000093': 'Theology Council',
        '1000094': 'TransStellar Shipping', '1000095': 'Federal Freight', '1000096': 'Inner Zone Shipping',
        '1000097': 'Material Acquisition', '1000098': 'Astral Mining Inc.', '1000099': 'Combined Harvest',
        '1000100': 'Quafe Company', '1000101': 'CreoDron', '1000102': 'Roden Shipyards',
        '1000103': 'Allotek Industries', '1000104': 'Poteque Pharmaceuticals', '1000105': 'Impetus',
        '1000106': 'Egonics Inc.', '1000107': 'The Scope', '1000108': 'Chemal Tech', '1000109': 'Duvolle Laboratories',
        '1000110': 'FedMart', '1000111': 'Aliastra', '1000112': 'Bank of Luminaire', '1000113': 'Pend Insurance',
        '1000114': 'Garoun Investment Bank', '1000115': 'University of Caille', '1000116': 'President',
        '1000117': 'Senate', '1000118': 'Supreme Court', '1000119': 'Federal Administration',
        '1000120': 'Federation Navy', '1000121': 'Federal Intelligence Office', '1000122': 'Federation Customs',
        '1000123': 'Ammatar Fleet', '1000124': 'Archangels', '1000125': 'CONCORD', '1000126': 'Ammatar Consulate',
        '1000127': 'Guristas', '1000128': "Mordu's Legion", '1000129': 'Outer Ring Excavations',
        '1000130': 'Sisters of EVE', '1000133': 'Salvation Angels', '1000134': 'Blood Raiders',
        '1000135': 'Serpentis Corporation', '1000136': 'Guardian Angels', '1000137': 'DED', '1000138': 'Dominations',
        '1000139': 'Food Relief', '1000141': 'Guristas Production', '1000144': 'Intaki Bank',
        '1000145': 'Intaki Commerce', '1000146': 'Intaki Space Police', '1000147': 'Intaki Syndicate',
        '1000151': 'Khanid Innovation', '1000152': 'Khanid Transport', '1000153': 'Khanid Works',
        '1000154': 'Nefantar Miner Association', '1000156': 'Royal Khanid Navy', '1000157': 'Serpentis Inquest',
        '1000159': 'The Sanctuary', '1000160': 'Thukker Mix', '1000161': 'True Creations', '1000162': 'True Power',
        '1000163': 'Trust Partners', '1000165': 'Hedion University', '1000166': 'Imperial Academy',
        '1000167': 'State War Academy', '1000168': 'Federal Navy Academy', '1000169': 'Center for Advanced Studies',
        '1000170': 'Republic Military School', '1000171': 'Republic University', '1000172': 'Pator Tech School',
        '1000179': '24th Imperial Crusade', '1000180': 'State Protectorate', '1000181': 'Federal Defense Union',
        '1000182': 'Tribal Liberation Force', '1000270': 'Outer Ring Development', '1000271': 'Outer Ring Prospecting',
        '1000276': 'ORE Technologies', '1000277': 'Frostline Laboratories', '1000283': 'Imperial War Reserves',
        '1000284': 'State Military Stockpile', '1000285': 'Federal Strategic Materiel',
        '1000286': 'Republic Fleet Ordnance', '1000292': 'Veles Clade', '1000293': 'Perun Clade',
        '1000294': 'Svarog Clade', '1000298': 'The Convocation of Triglav'}


# corp = {'1000002': 'CBD Corporation', '1000003': 'Prompt Delivery'}


class Parser():
    def __init__(self):

        self.MAX_REQUESTS = 10
        self.data = []

    async def loader(self):
        # запустить таски

        _idlist = list(corp.keys())

        for i in range(0, len(_idlist), self.MAX_REQUESTS):
            tasks = _idlist[i:i + self.MAX_REQUESTS]
            await asyncio.gather(*[self.async_get(id) for id in tasks])

            # print('done')

        # print(_idlist[i:i + self.MAX_REQUESTS])

        # pprint(self.data)
        # pprint(len(self.data))

        # ts = time.time()
        # myFile = open(f'{round(ts)}.csv', 'w', newline='')

        myFile = open('pl_list.csv', 'w', newline='')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(self.data)

    # sell - продавцы
    # buy - покупатели

    async def async_get(self, id):
        url = f'https://www.fuzzwork.co.uk/lpstore/buy/10000002/{id}'
        # url = f'https://www.fuzzwork.co.uk/lpstore/buy/10000002/{id}'

        print(id, url)

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:

                if resp.status == 200:
                    # УДАЧНО
                    print(resp.status)
                    _html = await resp.text()
                    await self.pars_html(_html, id)
                    # print(await resp.text())
                    # await self.successful_request()
                else:
                    print('err get')

    async def pars_html(self, html, corpid):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', {'id': 'lp', 'class': 'tablesorter'})

        for i in table.tbody:
            if isinstance(i, element.Tag):
                _td = i.findAll('td')

                # _arr = [
                #     corpid,
                #     _td[0].text,
                #     _td[1].text,
                #     _td[2].text,
                #     _td[3].text,
                #     _td[-5].text,
                #     _td[-4].text,
                #     _td[-3].text,
                #     _td[-2].text,
                #     _td[-1].text,
                # ]

                _arr = [
                    int(corpid),
                    int(_td[0].text),
                    int(_td[1].text.replace(',', '')),
                    int(_td[2].text.replace(',', '')),
                    _td[3].text,  # имя
                    float(_td[-5].text.replace(',', '')),
                    int(_td[-4].text),
                    float(_td[-3].text.replace(',', '')),
                    int(_td[-2].text),
                    float(_td[-1].text.replace(',', '')),
                ]

                self.data += [_arr]


async def main():
    await Parser().loader()

    # await parser()

    # with open("lp.json", "w") as write_file:
    #     json.dump(data, write_file)


if __name__ == '__main__':
    # asyncio.run(main())

    # loop = asyncio.get_event_loop()
    # # future = asyncio.ensure_future(main)
    # loop.run_until_complete(main)
    # # loop.close()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        loop.run_until_complete(asyncio.sleep(1))
    finally:
        loop.close()