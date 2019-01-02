from q0018.main import sheet1, root, Element, ElementTree

if __name__ == '__main__':
    students = Element('students')
    for i in range(sheet1.nrows):
        _id, name, math, chinese, english = sheet1.row_values(i)
        child = Element('student')
        child.tail = '\n'
        child.set('id', _id)
        a = Element('math')
        a.text = str(math)
        b = Element('chinese')
        b.text = str(chinese)
        c = Element('english')
        c.text = str(english)
        d = Element('name')
        d.text = name
        child.extend([d, a, b, c])
        students.append(child)
    root.append(students)
    ElementTree(root).write('student.xml', encoding='utf-8', xml_declaration=True)
