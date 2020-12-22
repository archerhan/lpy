import pymysql
from pymysql.cursors import DictCursor


class Student(object):

    def __init__(self, id, name, sex, birthday, address):
        self.id = id
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.address = address

    def __str__(self):
        return f'\n学号：{self.id}\n姓名：{self.name}\n性别：{self.sex}\n生日：{self.birthday}\n地址：{self.address}\n'


def main():
    page = int(input('页码：'))
    size = int(input('大小：'))
    con = pymysql.connect(host='123.57.130.195', port=3306,database='school', charset='utf8',user='root',password='123456')
    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute(
                'select stuid as id, stuname as name, stusex as sex, stubirth as birthday, stuaddr as address from tb_student limit %s,%s',
                ((page-1) * size, size)
            )
            results = cursor.fetchall()
            print(results)
            for stu in results:
                student = Student(*stu)
                print(student)
                # print(stu['id'],end='\t')
                # print(stu['name'], end='\t')
                # print(stu['sex'], end='\t')
                # print(stu['birthday'], end='\t')
                # print(stu['address'], end='\t')

    finally:
        con.close()


if __name__ == '__main__':
    main()