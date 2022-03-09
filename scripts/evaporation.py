from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(ammonia_evaporator, ['liquid_ammonia'], 'ammonia', 1, 1)
    move(ammonia_evaporator, ammonia_air_mixer, 'ammonia', 1)
