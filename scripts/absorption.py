from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(absorption_tank, ['liquid_nitron_gases', 'water'], 'HNO3', 9, 9)
    find_and_move(absorption_tank, end_storage, 'HNO3', 1)