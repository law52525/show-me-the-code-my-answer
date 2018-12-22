import xlwt

if __name__ == '__main__':
    with open('numbers.txt', encoding='utf-8') as f:
        s = f.read()
    numbers = eval(s)
    book = xlwt.Workbook()
    sheet = book.add_sheet('numbers')
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            sheet.write(i, j, numbers[i][j])
    book.save('numbers.xls')
