import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db',cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

#判断是否连通
def isConnected(start,end):
    sql = 'select number from ' + start + ' where to_city = \'' + end + '\'' + ' limit 1'
    cur.execute(sql)
    return 1 if cur.fetchone() else 0

#查询指定终点车次信息
def selectByCity(start,end,typeSql):
    sql = 'select id,number,start_time,to_time,cost,to_city,price,(select station_name from station ' \
          'where station_code = '+start+'.from_station) as from_station,(select station_name from station where ' \
          'station_code = '+start+'.to_station) as to_station from '+start+' where to_city = \'' + end + '\' '+ typeSql
    cur.execute(sql)
    row = cur.fetchall()
    return row

#查询指定车站车次信息
def selectByStation(start,end):
    sql = 'select * from ' + start + ' where to_station = \'' + end + '\''
    cur.execute(sql)
    row = cur.fetchall()
    return row

#写入数据
def insertNumber(name,list):
    sql = 'insert into ' + name +  ' value(0,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, (list))
    conn.commit()