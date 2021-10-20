import requests as rq
import json
from bs4 import BeautifulSoup
from markdownify import markdownify as md

interview_data = []


def main():
    getDataFEHandbook()
    getData30Seconds()
    saveToFile(interview_data)


def saveToFile(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_url(url):
    res = rq.get(url)
    return res.content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def getData30Seconds():
    BASE_URL = "https://raw.githubusercontent.com/30-seconds/30-seconds-of-interviews/master/data/questions.json"
    data = get_json_from_url(BASE_URL)
    interview_data.extend(data)


def getDataFEHandbook():
    tags = ['html', 'css', 'javascript']
    data = []
    for tag in tags:
        url = 'https://frontendinterviewhandbook.com/' + tag + '-questions'
        page = rq.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        titles = []
        contents = []

        for title in soup.find_all('h3'):
            if title.text != 'Other Answers#':
                titles.append(title.text)
                contents.append(url + title.find('a', href=True)['href'])

        for num, i in enumerate(titles):
            curData = {"question": titles[num],
                       "answer": contents[num],
                       "tags": [tag]}
            data.append(curData)
    interview_data.extend(data)


main()
