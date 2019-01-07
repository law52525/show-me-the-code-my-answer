from q0018.main import sheet1, root, CustomElement

if __name__ == '__main__':
    students = CustomElement('students')
    for i in range(sheet1.nrows):
        m = map(str, sheet1.row_values(i))
        name = ['name', 'math', 'chinese', 'english']
        child = CustomElement('student', id=next(m))
        for t in zip(name, m):
            child.append(CustomElement(*t))
        students.append(child)
    root.append(students)
    root.write('student.xml')
