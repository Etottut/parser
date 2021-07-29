import xlwt
from datetime import datetime

# Стиль: жирный шрифт + красный цвет + итд
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                     num_format_str='#,##0.00')
# Стиль: форматировать как дату
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
# Добавляем Лист в таблицу и даём ему название
ws = wb.add_sheet('A Test Sheet')
# Добавляем ещё один лист - сохраняем информацию об этом в переменной ws2
ws2 = wb.add_sheet('New sheet')

# В ячейку A1 (координаты - 0;0) вписываем 1234.56 и задаём стиль style0, указанный на строке 5
ws.write(0, 0, 1234.56, style0)
# В A2 (координаты - 1;0) пишем дату в формате, определенном в style1 (строка 8)
ws.write(1, 0, datetime.now(), style1)
# В A3 (координаты - 2;0) пишем 1
ws.write(2, 0, 1)
# В B3 (координаты - 2;1) пишем 1
ws.write(2, 1, 1)
# В C3 (координаты - 2;2) складываем значения ячеек A3 и B3
ws.write(2, 2, xlwt.Formula("A3+B3"))

# На втором листе (ws2) пишем Hello, world!
ws2.write(0, 0, "Hello, world!")

# Сохраняем файл
wb.save('example.xls')
