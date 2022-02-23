import time
import routes
import os
import re

storage = routes.end_storage
start_time = {
    'HNO3': time.time(),
    'H2SO4': time.time(),
}

average_times_for_HNO3 = []
average_times_for_H2SO4 = []


def calc(name, times, product):
    items = os.listdir(storage)
    for item in items:
        if re.match(name, item):
            try:
                old_item = f'{storage}\\{item}'
                os.remove(old_item)
                temp_time = time.time() - start_time[product]
                times.append(temp_time)
                print(item, 'moved from storage')
                print('time for cooking:', '%.2f' % temp_time)
                print('average time:', '%.2f' % (sum(times) / len(times)), '\n')
                start_time[product] = time.time()
                break
            except:
                print(item, 'not found')


while True:
    calc('HNO3', average_times_for_HNO3, 'HNO3')
    calc('H2SO4', average_times_for_H2SO4, 'H2SO4')