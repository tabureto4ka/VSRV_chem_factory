from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(first_absorption_capacity, ['SO2', 'SO3'], 'oleum', 9, 2)
    find_and_move(first_absorption_capacity, second_contact_device, 'SO2', 9)
    find_and_move(first_absorption_capacity, mixing_capacity, 'oleum', 2)
