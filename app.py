import requests as rq
import json
import random

from noti import send


def main():
    final_data = readData()
    rand_num = random.randint(0, len(final_data))
    selected_data = template(final_data[rand_num])
    send(selected_data)


def readData():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data


def template(data):
    title = '*' + data['question'] + '*'
    body = data['answer']
    tags = ', '.join(data['tags'])

    return title + '\n\n' + body + '\n\n' + tags


main()
