import os
import xlrd
from xml.etree.ElementTree import Element, ElementTree


class CustomElement(Element):
    def __init__(self, tag, text='\n', tail='\n', **extra):
        super().__init__(tag, **extra)
        self.text = text
        self.tail = tail

    def write(self, file_or_filename):
        ElementTree(self).write(file_or_filename, encoding='utf-8', xml_declaration=True)


x1 = xlrd.open_workbook(next(f for f in os.listdir('.') if f.endswith('xls')))
sheet1 = x1.sheet_by_index(0)
root = CustomElement('root')

if __name__ == '__main__':
    cities = CustomElement('cities')
    for i in range(sheet1.nrows):
        _id, name = sheet1.row_values(i)
        cities.append(CustomElement('city', name, id=_id))
    root.append(cities)
    root.write('city.xml')
