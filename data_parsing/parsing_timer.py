import datetime
import time
import random
import requests
from urllib.request import ProxyHandler, build_opener, HTTPHandler

# PROXIES = ['104.236.141.243:8080', '104.131.178.157:8085']


def get_requests():
    time.sleep(random.randint(1, 10))
    # proxy = random.choice(PROXIES)
    # opener = build_opener(ProxyHandler({'https': proxy}))
    print('work')
    response=requests.get('https://www.cbr.ru')
    # response  = opener.open('https://www.cbr.ru')
    print(response.status_code)
    return response


for i in range(20):
    print(i)
    response = get_requests()
    print(response.status_code)
    print(datetime.datetime.now())
