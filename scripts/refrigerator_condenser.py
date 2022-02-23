from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(refrigerator_condenser, ['hot_nitron_gases'], 'liquid_nitron_gases', 4, 2)
    find_and_move(refrigerator_condenser, absorption_tank, 'liquid_nitron_gases', 2)
