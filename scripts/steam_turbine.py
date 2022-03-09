from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(steam_turbine, ['water'], 'steam', 4, 4)
    move(steam_turbine, steam_boiler_utilizer, 'steam', 1)
