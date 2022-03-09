from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(steam_boiler_utilizer, ['nitron_gases', 'steam'], 'hot_nitron_gases', 3, 3)
    move(steam_boiler_utilizer, refrigerator_condenser, 'hot_nitron_gases', 1)
