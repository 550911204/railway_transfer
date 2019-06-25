import pymysql

#conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db',cursorclass=pymysql.cursors.DictCursor)
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db')
cur = conn.cursor()

#通过id查城市中文名
def selectNameChineseById(id):
    cur.execute('select name_chinese from city where id = (%s)',(id))
    row = cur.fetchone()
    return row[0]

#通过id查城市编码
def selectNameCodeById(id):
    cur.execute('select name_code from city where id = (%s)',(id))
    row = cur.fetchone()
    return row[0]

#通过编码查城市中文名
def selectNameChineseByCode(code):
    cur.execute('select name_chinese from city where name_code = (%s)',(code))
    row = cur.fetchone()
    return row[0]

#通过中文名查城市编码
def selectNameCodeByChinese(chinese):
    cur.execute('select name_code from city where name_chinese = (%s)',(chinese))
    row = cur.fetchone()
    return row[0]

#通过城市编码查id
def selectIdByCode(code):
    cur.execute('select id from city where name_code = (%s)',(code))
    row = cur.fetchone()
    return row[0]


