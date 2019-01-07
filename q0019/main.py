from q0018.main import sheet1, root, CustomElement

if __name__ == '__main__':
    students = CustomElement('numbers')
    for i in range(sheet1.nrows):
        a = sheet1.row_values(i)
        child = CustomElement('number')
        for j in a:
            child.append(CustomElement('i', str(int(j))))
        students.append(child)
    root.append(students)
    root.write('numbers.xml')
