import os
import xlrd
from xml.etree.ElementTree import Element, tostring
import html


x1 = xlrd.open_workbook(next(f for f in os.listdir('.') if f.endswith('xls')))
sheet1 = x1.sheet_by_index(0)

head = '<?xml version="1.0" encoding="UTF-8"?>'
root = Element('root')

if __name__ == '__main__':
    cities = Element('cities')
    for i in range(sheet1.nrows):
        _id, name = sheet1.row_values(i)
        child = Element('city')
        child.text = name
        child.set('id', _id)
        cities.append(child)
    root.append(cities)
    with open('city.xml', 'w', encoding='utf-8') as f:
        f.write(head + html.unescape(tostring(root).decode('utf-8')))
