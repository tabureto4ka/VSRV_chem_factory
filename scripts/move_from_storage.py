from transport_functions import *
from routes import *
while True:
    find_and_move(start_storage, drying_capacity, 'air', 1)
    find_and_move(start_storage, sulfur_boiler, 'sulfur', 2)
    find_and_move(start_storage, ammonia_air_mixer, 'air', 1)
    find_and_move(start_storage, mixing_capacity, 'water', 3)
    find_and_move(start_storage, ammonia_evaporator, 'liquid_ammonia', 2)
    find_and_move(start_storage, steam_turbine, 'water', 2)
    find_and_move(start_storage, absorption_tank, 'water', 2)
