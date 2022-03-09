from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(drying_capacity, ['air'], 'dry_air', 2, 1)
    move(drying_capacity, sulfur_boiler, 'dry_air', 1)
