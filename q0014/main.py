import json
import xlwt

if __name__ == '__main__':
    with open('student.txt', encoding='utf-8') as f:
        s = f.read()
    students = json.loads(s)
    book = xlwt.Workbook()
    sheet = book.add_sheet('student')
    for i, k in enumerate(students.keys()):
        sheet.write(i, 0, k)
        for j, l in enumerate(students[k]):
            sheet.write(i, j+1, l)
    book.save('student.xls')
