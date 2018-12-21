import json
import xlwt

if __name__ == '__main__':
    with open('student.txt', encoding='utf-8') as f:
        s = f.read()
    students = json.loads(s)
    book = xlwt.Workbook()
    sheet = book.add_sheet('student')
    i = 0
    for k, v in students.items():
        sheet.write(i, 0, k)
        j = 1
        for l in v:
            sheet.write(i, j, l)
            j += 1
        i += 1
    book.save('student.xls')
