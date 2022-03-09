from production_functions import *
from transport_functions import *
from routes import *
while True:
    join_substances(package_H2SO4, ['H2SO4'], 'packed_H2SO4', 20, 5)
    join_substances(package_HNO3, ['HNO3'], 'packed_HNO3', 20, 5)
    move(package_H2SO4, end_storage, 'packed_H2SO4', 10)
    move(package_HNO3, end_storage, 'packed_HNO3', 10)

