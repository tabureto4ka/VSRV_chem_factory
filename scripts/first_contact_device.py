from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(first_contact_device, ['SO2'], 'SO3', 6, 1)
    find_and_move(first_contact_device, first_absorption_capacity, 'SO3', 6)
    find_and_move(first_contact_device, first_absorption_capacity, 'SO2', 6)