from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md


def getData(tags):
    data = []
    for tag in tags:
        url = 'https://yangshun.github.io/front-end-interview-handbook/en/' + tag + '-questions'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        titles = []
        contents = []

        for title in soup.find_all('h3'):
            if title.text != 'Other Answers#':
                titles.append(title.text)
                contents.append(url + title.find('a', href=True)['href'])
            # for a in text.find_all('a', href=True):
            #     print(a['href'])

        # for content in soup.find('h3').next_siblings:
        #     if content.name == "h3":
        #         contents.append(curContent)
        #         curContent = []
        #         continue
        #     else:
        #         curContent.append(md(str(content) + '\n'))

        for num, i in enumerate(titles):
            curData = {"question": titles[num],
                       "answer": contents[num],
                       "tags": [tag]}
            data.append(curData)
    return data
