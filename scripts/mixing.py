from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(mixing_capacity, ['oleum', 'water'], 'H2SO4', 6, 3)
    find_and_move(mixing_capacity, intermediate_capacity, 'H2SO4', 1)
