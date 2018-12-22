import json
import xlwt

if __name__ == '__main__':
    with open('city.txt', encoding='utf-8') as f:
        s = f.read()
    city = json.loads(s)
    book = xlwt.Workbook()
    sheet = book.add_sheet('city')
    for i, k in enumerate(city.keys()):
        sheet.write(i, 0, k)
        sheet.write(i, 1, city[k])
    book.save('city.xls')
