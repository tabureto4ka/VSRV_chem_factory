from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(contact_device, ['ammonia_mixture'], 'nitron_gases', 6, 6)
    move(contact_device, steam_boiler_utilizer, 'nitron_gases', 1)
