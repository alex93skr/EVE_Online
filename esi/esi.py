from pprint import pprint

import requests

# esi = 'https://esi.evetech.net/latest/alliances/'
# esi = 'https://esi.evetech.net/latest/alliances/99000083/'
# esi = 'https://esi.evetech.net/latest/characters/97026914/'
# esi = 'https://esi.evetech.net/latest/contracts/public/10000002'

# esi = 'https://esi.evetech.net/latest/dogma/attributes/'
# esi = 'https://esi.evetech.net/latest/dogma/attributes/2156/'
# esi = 'https://esi.evetech.net/latest/dogma/effects/'
# esi = 'https://esi.evetech.net/latest/dogma/effects/6513'

# esi = 'https://esi.evetech.net/latest/fw/leaderboards/'
# esi = 'https://esi.evetech.net/latest/fw/leaderboards/corporations/'
# esi = 'https://esi.evetech.net/latest/fw/leaderboards/characters/'
# esi = 'https://esi.evetech.net/latest/fw/stats/'
# esi = 'https://esi.evetech.net/latest/fw/wars/'

# esi = 'https://esi.evetech.net/latest/incursions/'
# esi = 'https://esi.evetech.net/latest/insurance/prices/'

# esi = 'https://esi.evetech.net/latest/loyalty/stores/1000179/offers/'


# esi = 'https://esi.evetech.net/latest/opportunities/tasks/'
# esi = 'https://esi.evetech.net/latest/route/10000002/10000032/'
# https://esi.evetech.net/latest/search/?categories=agent,alliance,character,constellation,corporation,faction,inventory_type,region,solar_system,station&datasource=tranquility&language=en&search=skr&strict=false
# esi = 'https://esi.evetech.net/latest/status/'

# esi = 'https://esi.evetech.net/latest/universe/types/2476'
# esi = 'https://esi.evetech.net/latest/universe/regions/10000032'
# esi = 'https://esi.evetech.net/latest/universe/constellations/20000393'
esi = 'https://esi.evetech.net/latest/universe/systems/30002686'
# esi = 'https://esi.evetech.net/latest/universe/asteroid_belts/40170855'
# esi = 'https://esi.evetech.net/latest/universe/system_kills/'
# esi = 'https://esi.evetech.net/latest/universe/system_jumps/'

# esi = 'https://esi.evetech.net/latest/universe/graphics/4252'


# D:\code\eve\_data\mapSolarSystems.csv
# esi = 'https://esi.evetech.net/latest/route/30000142/30000190/'


# esi = 'https://esi.evetech.net/latest/wars'
# esi = 'https://esi.evetech.net/latest/wars/711535'
# esi = 'https://esi.evetech.net/latest/wars/711535/killmails/'


# Market
# esi = 'https://esi.evetech.net/latest/markets/10000032/history/?type_id=2476'
# esi = 'https://esi.evetech.net/latest/markets/10000032/orders/'
# esi = 'https://esi.evetech.net/latest/markets/10000032/types/'
# esi = 'https://esi.evetech.net/latest/markets/groups/'
# esi = 'https://esi.evetech.net/latest/markets/prices/'


params = {}

r = requests.get(esi, params=params)
# print(r.status_code)

pprint(r.json())
