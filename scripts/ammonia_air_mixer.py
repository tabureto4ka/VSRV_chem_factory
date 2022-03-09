from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(ammonia_air_mixer, ['ammonia', 'air'], 'ammonia_mixture', 1, 2)
    move(ammonia_air_mixer, contact_device, 'ammonia_mixture', 1)
