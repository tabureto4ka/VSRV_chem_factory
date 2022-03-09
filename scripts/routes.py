import os

work_directory = os.getcwd()

if os.path.basename(work_directory) == 'scripts':
    work_directory = os.path.normpath(os.getcwd() + os.sep + os.pardir)


# пути для узлов
start_storage = f'{work_directory}\\factory\\start_storage\\'
end_storage = f'{work_directory}\\factory\\end_storage\\'
drying_capacity = f'{work_directory}\\factory\\drying_capacity\\'
sulfur_boiler = f'{work_directory}\\factory\\sulfur_boiler\\'
first_contact_device = f'{work_directory}\\factory\\first_contact_device\\'
first_absorption_capacity = f'{work_directory}\\factory\\first_absorption_capacity\\'
second_contact_device = f'{work_directory}\\factory\\second_contact_device\\'
second_absorption_capacity = f'{work_directory}\\factory\\second_absorption_capacity\\'
mixing_capacity = f'{work_directory}\\factory\\mixing_capacity\\'
intermediate_capacity = f'{work_directory}\\factory\\intermediate_capacity\\'
ammonia_evaporator = f'{work_directory}\\factory\\ammonia_evaporator\\'
ammonia_air_mixer = f'{work_directory}\\factory\\ammonia_air_mixer\\'
steam_turbine = f'{work_directory}\\factory\\steam_turbine\\'
contact_device = f'{work_directory}\\factory\\contact_device\\'
steam_boiler_utilizer = f'{work_directory}\\factory\\steam_boiler_utilizer\\'
refrigerator_condenser = f'{work_directory}\\factory\\refrigerator_condenser\\'
absorption_tank = f'{work_directory}\\factory\\absorption_tank\\'
package = f'{work_directory}\\factory\\package'
package_H2SO4 = f'{work_directory}\\factory\\package\\package_H2SO4'
package_HNO3 = f'{work_directory}\\factory\\package\\package_HNO3'


