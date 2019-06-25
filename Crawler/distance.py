import json
import requests
import pymysql
import SqlDir.city_table

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db')
cur = conn.cursor()

#访问链接
def getIndex(url):
    respose = requests.get(url)
    if respose.status_code == 200:
        return respose.text

def distance(i,j):
    sql = 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=nav&sn=2$$$$$$'+SqlDir.city_table.selectNameChineseById(i)+'$$0$$$$&en=2$$$$$$'+SqlDir.city_table.selectNameChineseById(j)+'$$0$$$$'
    list = getIndex(sql)
    str_json = json.loads(list)
    fromCity = SqlDir.city_table.selectNameChineseById(i)
    toCity = SqlDir.city_table.selectNameChineseById(j)
    dis = str_json['content']['dis']
    insertSql = 'insert into distance value(0,%s,%s,%s)'
    cur.execute(insertSql,(fromCity,toCity,dis))
    conn.commit()
    return dis

for i in range(1,34):
    for j in range(i,34):
        if i != j:
            print(distance(i,j))