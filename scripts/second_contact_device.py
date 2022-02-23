from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(second_contact_device, ['SO2'], 'SO3', 3, 1)
    find_and_move(second_contact_device, second_absorption_capacity, 'SO3', 1)
