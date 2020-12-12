import requests as rq
import json
import random

from noti import send


def template(data):
    '''
    Question:
    Answer:
    '''
    title = data['question']
    body = data['answer']

    return title + '\n' + body


BASE_URL = "https://raw.githubusercontent.com/30-seconds/30-seconds-of-interviews/master/data/questions.json"

res = rq.get(BASE_URL).content
data = json.loads(res)

rand_num = random.randint(0, len(data))
selected_data = template(data[rand_num])
print(selected_data)

send(selected_data)
