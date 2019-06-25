import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db')
cur = conn.cursor()

#id查询车站编码
def selectStationCodeById(id):
    cur.execute('select station_code from station where id = (%s)',(id))
    row = cur.fetchone()
    return row[0]

#id查询车站名字
def selectStationNameById(id):
    cur.execute('select station_name from station where id = (%s)',(id))
    row = cur.fetchone()
    return row[0]

#编码查询车站名字
def selectStationNameByStationCode(code):
    cur.execute('select station_name from station where station_code = (%s)',(code))
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        return code

#名字查询车站编码
def selectStationCodeByStationName(name):
    cur.execute('select station_code from station where station_name = (%s)',(name))
    row = cur.fetchone()
    return row[0]

#编码查询车站id
def selectCityIdByStstionCode(code):
    cur.execute('select city_id from station where station_code = (%s)',(code))
    row = cur.fetchone()
    return row[0]

#名字查询车站id
def selectCityIdByStstionName(name):
    cur.execute('select city_id from station where station_name = (%s)',(name))
    row = cur.fetchone()
    return row[0]

#城市id查询车站id
def selectStationCodeByCityId(id):
    cur.execute('select station_code from station where city_id = (%s)',(id))
    row = cur.fetchall()
    return row

#城市id查询车站name
def selectStationNameByCityId(id):
    cur.execute('select station_name from station where city_id = (%s)',(id))
    row = cur.fetchall()
    return row

#写入车站信息
def insertStation(code,name,cityId):
    cur.execute('insert into station value(0,%s,%s,%s)',(code,name,cityId))
    conn.commit()

#拿到车站列表  英文代码
def getCityCodeList():
    cur.execute('select station_code from station')
    return cur.fetchall()