import random as r
import time
import os

color = ''
title = ''

os.system('title ' + title)
os.system('color ' + color)

ip = str(r.randrange(100, 999)) + '.' + str(r.randrange(100, 999)) + '.' + str(r.randrange(1, 9)) + '.' + str(r.randrange(1, 9))

print('Cracking IP address...')
time.sleep(1)
print("Your IP is " + ip)
time.sleep(1000)