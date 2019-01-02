from q0018.main import sheet1, root, Element, ElementTree

if __name__ == '__main__':
    students = Element('numbers')
    for i in range(sheet1.nrows):
        a = sheet1.row_values(i)
        child = Element('number')
        child.tail = '\n'
        for j in a:
            t = Element('i')
            t.text = str(j)
            child.append(t)
        students.append(child)
    root.append(students)
    ElementTree(root).write('numbers.xml', encoding='utf-8', xml_declaration=True)
