import requests
import xlsxwriter
import json

workbook = xlsxwriter.Workbook('Output.xlsx')

for i in range(0, 3000, 1000):
    page_number = int(i/1000)+1
    print(f"Начинаем парсить страницу {page_number}, offset = {i}")
    url = f"https://xn--b1aedfedwqbdfbnzkf0oe.xn--p1ai/api/v1/cms/publicorganizationpages/?fields=*&order=is_body_empty,title&limit=1000&offset={i}&search_id=1"
    r = requests.get(url=url)
    data = json.loads(r.text)

    worksheet = workbook.add_worksheet("{page_number}")
    
    row = 0
    col = 0

    for company in data["items"]:
        worksheet.write(row, col, company["title"])
        worksheet.write(row, col + 1, company["region"]["title"])
        # add some columns
        row += 1

workbook.close()