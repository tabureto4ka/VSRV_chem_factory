from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(absorption_tank, ['liquid_nitron_gases', 'water'], 'HNO3', 9, 9)
    move(absorption_tank, package_HNO3, 'HNO3', 1)