from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(sulfur_boiler, ['dry_air', 'sulfur'], 'SO2', 3, 1)
    find_and_move(sulfur_boiler, first_contact_device, 'SO2', 1)
