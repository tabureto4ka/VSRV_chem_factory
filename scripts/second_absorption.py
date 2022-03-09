from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(second_absorption_capacity, ['SO3'], 'oleum', 4, 2)
    move(second_absorption_capacity, mixing_capacity, 'oleum', 1)
