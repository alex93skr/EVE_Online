from pprint import pprint

from bs4 import BeautifulSoup
from bs4 import element

with open('lp.html', encoding='utf-8') as f:
    read_data = f.read()

# print(read_data)

soup = BeautifulSoup(read_data, 'html.parser')

# <table border=1 id="lp" class="tablesorter">

table = soup.find('table', {'id': 'lp', 'class': 'tablesorter'})

# table.tbody.table.decompose()


# for line in arr:

# <th>id</th>
# <th>LP</th>
# <th>Isk</th>
# <th>Item</th>
# <th>Other Requirements</th>
# <th>Other Cost</th>
# <th>Quantity</th>
# <th>Buy Price</th>
# <th>5% Volume</th>
# <th>isk/lp</th>

# data = {id:data}

data = []

corp_id = '7777777'

for i in table.tbody:

    if isinstance(i, element.Tag):
        _td = i.findAll('td')

        # _arr = {'corp': id,
        #         'id': _td[0].text,
        #        'LP': _td[1].text,
        #        'Isk': _td[2].text,
        #        'Item': _td[3].text,
        #        'Other Cost': _td[-5].text,
        #        'Quantity': _td[-4].text,
        #        'Buy Price': _td[-3].text,
        #        '5% Volume': _td[-2].text,
        #        'isk-to-lp': _td[-1].text}

        _arr = [
            int(corp_id),
            int(_td[0].text),
            int(_td[1].text.replace(',', '')),
            int(_td[2].text.replace(',', '')),
            _td[3].text,  # имя
            float(_td[5].text.replace(',', '')),
            float(_td[-5].text.replace(',', '')),
            int(_td[-4].text),
            float(_td[-3].text.replace(',', '')),
            int(_td[-2].text),
            float(_td[-1].text.replace(',', '')),
        ]

        # pprint(_arr)
        data += [_arr]

pprint(data)
