import openpyxl
import json

with open('data_3.json') as file:
    data = json.load(file)
    print(data['Items'])


# book = openpyxl.Workbook()
#
# sheet = book.active
#
# sheet[''] =
# sheet[''] =
# sheet[''] =
#
# book.save('parser_book.xlsx')
# book.close()