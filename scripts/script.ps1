start wt ' python delivery_in_storage.py ; sp -H -s 0.75 python move_from_storage.py ; sp -H -s 0.66 python dehumidification_of_air.py '
start wt ' python sulfur_boiler.py ; sp -H -s 0.75 python first_contact_device.py ; sp -H -s 0.66 python fist_absorption.py ; sp -H python second_contact_device.py '
start wt ' python second_absorption.py ; sp -H -s 0.75 python mixing.py ; sp -H -s 0.66 python intermediate_capacity.py '
start wt ' python evaporation.py ; sp -H -s 0.8 python ammonia_air_mixer.py ; sp -H -s 0.75 python steam_turbine.py ; sp -H -s 0.66 python contact.py ; sp -H python steam_boiler_utilizer.py '
start wt ' python refrigerator_condenser.py ; sp -H -s 0.75 python absorption.py ; sp -H -s 0.66 python package.py '
start wt ' python calc_time.py '