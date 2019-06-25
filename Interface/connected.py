import SqlDir.city_table
import SqlDir.train_table
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db',cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

#筛选出理论能中转的城市
def connectedTheoryList(start,end):
    list = []
    for i in range(1,34):
        mid = SqlDir.city_table.selectNameCodeById(i)
        if SqlDir.train_table.isConnected(start,mid) == 1 and SqlDir.train_table.isConnected(mid,end) == 1:
            list.append(mid)
    return list
