import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db')
cur = conn.cursor()

#写入数据库
def insertCodeList(str):
    cur.execute('insert into code_list value(0,%s)',(str))
    conn.commit()

#拿到待解析编码
def getCode(id):
    cur.execute('select code from code_list where id = (%s)', (id))
    row = cur.fetchone()
    return row[0]