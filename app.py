import requests as rq
import json
import random

from noti import send
from data import getData


def template(data):
    '''
    Question:
    Answer:
    '''
    title = '*' + data['question'] + '*'
    body = data['answer']
    tags = ', '.join(data['tags'])

    return title + '\n\n' + body + '\n\n' + tags


BASE_URL = "https://raw.githubusercontent.com/30-seconds/30-seconds-of-interviews/master/data/questions.json"

res = rq.get(BASE_URL).content
data1 = json.loads(res)

pages = ['html', 'css', 'javascript']
data2 = getData(pages)

data = data1 + data2

rand_num = random.randint(0, len(data))
selected_data = template(data[rand_num])
print(selected_data)

send(selected_data)
