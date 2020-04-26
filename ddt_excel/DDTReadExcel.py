# coding=utf-8
"""
利用excel结合ddt实现数据驱动
2020-04-26
"""
import xlrd
class ddtreadexcel(object):
    def getdata(self):

        path = 'locman.xlsx'
        book_data = xlrd.open_workbook(path)  # 读取excel
        book_sheet = book_data.sheet_by_index(0)  # 获取sheet1的数据
        rows_num = book_sheet.nrows  # 获取行数
        rows0 = book_sheet.row_values(0)  # 获取第一行的数据，作为字典的键，list
        rows0_num = len(rows0)  # 数据个数作为列数
        print "列数：", rows0_num

        list = []
        for x in range(1, rows_num):
            rows_data = book_sheet.row_values(x)  # 读取每一行的数据
            print "每行数据：", rows_data  # 每行的数据，[u'chqwh@163.com', u'111111']
            rows_dic = {}
            for y in range(0, rows0_num):
                rows_dic[rows0[y]] = rows_data[y]  # 每一行的每列数据加到字典里
                print "每列：rows_dic[rows0[", y, "]]", rows_dic[rows0[y]]
            list.append(rows_dic)  # 把字典数据加到列表里
            print "list:", list
        return list


if __name__ == '__main__':
    test = ddtreadexcel()
    test.getdata()
