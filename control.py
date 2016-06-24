#!/usr/bin/python
import sys
import requests
import random
import time

left = True
access_token = '0aad1aeb6da44fcebc94c28e393924e8ae1db36c'
device_id = '27003b000247353138383138'

def sendRequest(servo, speed):
    address = 'https://api.particle.io/v1/devices/'+format(device_id)+'/'+servo
    data = {'access_token': access_token, 'arg': speed}
    # print(address)
    r = requests.post(address, data=data)
    # print(r.text)

def rando():
    if (random.choice([True, False])):
        turn(1)
        time.sleep(2)
    else:
        turn(-1)
        time.sleep(2.2)
    rando()

def turn(num):
    if (num > 0):
        sendRequest('setPos', '0, 30')
        time.sleep(1)
        sendRequest('setposR', 0)
    else:
        sendRequest('setPos', '30, 0')
        time.sleep(1.2)
        sendRequest('setposL', 0)
    sendRequest('setpos', '30, 30')

if (len(sys.argv) == 1):
    rando()
    # sendRequest('setposL', 30)
    # time.sleep(1)
    # sendRequest('setposL', 0)
else:
    sendRequest('setpos', sys.argv[1]+', '+ sys.argv[2])
