import requests
import random
import time

url = 'http://127.0.0.1:8000/api/get_readings/'

def send_packets():
    data = {'humidity': random.randint(30, 60)}
    response = requests.post(url, json=data)  
    print('Wysłano')
    time.sleep(random.randint(1,5))
    return response

for _ in range(50):
    send_packets()

