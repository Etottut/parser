import requests
from bs4 import BeautifulSoup
import json


for i in range(0, 3000, 1000):
    page_number = int(i/1000)+1
    print(f"Начинаем парсить страницу {page_number}, offset = {i}")
    url = f"https://xn--b1aedfedwqbdfbnzkf0oe.xn--p1ai/api/v1/cms/publicorganizationpages/?fields=*&order=is_body_empty,title&limit=1000&offset={i}&search_id=1"
    r = requests.get(url=url)

    soup = BeautifulSoup(r.text, 'lxml')
    string = soup.find("body").text

    json_string = json.dumps(string, indent=4)
    # print(json_string)

    with open(f"data_{page_number}.json", "w", encoding="utf-8") as file:
        file.write(str(json_string))

    data = json.loads(json_string)
    with open(f"formatted_data_{page_number}.json", "w", encoding="utf-8") as file:
        file.write(str(data))
