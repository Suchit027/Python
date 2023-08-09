def student_details(number_students):
    student_name = {}
    number_students = int(number_students)
    for i in range(0, number_students):
        name = input('enter name')
        reg_no = input('reg no')
        marks = input('marks')
        student_name[name] = [reg_no, marks]
    search = input('enter needed student')
    if search not in student_name.keys():
        print('not there')
    else:
        print(f'reg no - {student_name[search][0]} ')
        print(f'marks - {student_name[search][1]}')


def main():
    no_students = input('enter number of students ')
    student_details(no_students)


if __name__ == '__main__':
    main()
