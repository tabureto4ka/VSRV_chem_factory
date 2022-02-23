import random
import time
import os
import re


# путь, название, время производства, объем.
# создаёт вещество в папке назанчения
def create_substances(path, name, time_for_manufacturing, volume):
    time.sleep(time_for_manufacturing)
    for i in range(volume):
        open(f'{path}{name}{random.randint(1, 1000)}_{i}', 'a').close()
    print(volume, name, 'created')


# объеденить несколько веществ в 1
def join_substances(path, substances, name, time_for_manufacturing, volume):
    items = os.listdir(path)
    temp_substances = []
    for substance in substances:
        for item in items:
            if re.match(substance, item):
                # print('find', item)
                temp_substances.append(item)
                break

    if len(temp_substances) == len(substances):
        for temp_substance in temp_substances:
            os.remove(f'{path}\\{temp_substance}')
        create_substances(path, name, time_for_manufacturing, volume)
        print(volume, name, 'created')
    else:
        print('not enough substances', substances, 'for', name)
        time.sleep(time_for_manufacturing)

