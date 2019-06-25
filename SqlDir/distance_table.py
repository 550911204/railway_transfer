import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db')
cur = conn.cursor()

#查询目标城市距离
def selectDistance(start,end):
    #A到B和B到A距离相同，固表中只存储A到B
    sql = 'select distance from distance where from_city = ' + '\'' + start + '\'' + ' and ' + 'to_city = ' + '\'' + end + '\''
    cur.execute(sql)
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        sql = 'select distance from distance where from_city = ' + '\'' + end + '\'' + ' and ' + 'to_city = ' + '\'' + start + '\''
        cur.execute(sql)
        row = cur.fetchone()
        if row:
            return row[0]
        else:
            return 'null'