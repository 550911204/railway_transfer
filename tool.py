import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()


# 查询所有城市
def selectAllCity():
    cur.execute('select * from city')
    row = cur.fetchall()
    return row


# 转换时间到分钟
def timeToMin(time):
    list = time.split(':')
    return int(list[0]) * 60 + int(list[1])

# 转换中文到分钟
def timeChineseToMin(time):
    list = time.split('小时')
    return int(list[0]) * 60 + int((list[1].split('分钟'))[0])

# 转换时间到分钟
def timeToHoure(time):
    h = int(time / 60)
    m = time % 60
    return (str(h) + '小时' + str(m) + '分钟')


# 时间间隔
def timeWait(time):
    h = int(time / 60)
    m = time % 60
    return (str(h) + '小时' + str(m) + '分钟')


# 价格提取
def priceToFloat(price):
    return float(price[1:])

# 保留前10
def getTopTen(list,lenth):
    if len(list) < lenth:
        return list
    resuList = []
    for i in range(0, lenth):
        resuList.append(list[i])
    return resuList

#sql条件正则
def trainType(type):
    sql = ' and number regexp \'^'
    if type == '全部':
        return ''
    elif type == '':
        sql = ''
    elif type == 'GC-高铁/城际':
        sql += 'G\''
    elif type == 'D-动车':
        sql += 'D\''
    elif type == 'Z-直达':
        sql += 'Z\''
    elif type == 'T-特快':
        sql += 'T\''
    elif type == 'K-快速':
        sql += 'K\''
    return sql
