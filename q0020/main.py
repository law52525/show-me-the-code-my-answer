import os
import re
import xlrd

tel_path = 'TelephoneDetails'


def parse(p):
    a = re.split(r'[分|秒]', p)[:-1]
    return (0, int(a[0])) if len(a) == 1 else (int(a[0]), int(a[1]))


if __name__ == '__main__':
    for file in os.listdir(tel_path):
        path = tel_path + os.sep + file
        book = xlrd.open_workbook(path)
        sheet1 = book.sheet_by_index(0)
        time = sheet1.col_values(4)[1:]
        call_type = sheet1.col_values(2)[1:]
        called_minutes = called_seconds = call_seconds = call_minutes = 0
        for t in range(len(time)):
            m, s = parse(time[t])
            if call_type[t] == "主叫":
                call_minutes += m
                call_seconds += s
            else:
                called_minutes += m
                called_seconds += s
        messages = (file[:-5], call_minutes + call_seconds // 60,
                    call_seconds % 60, called_minutes + called_seconds // 60,
                    called_seconds % 60)
        print("{}:\t主叫:{}分{}秒\t\t被叫:{}分{}秒".format(*messages))
