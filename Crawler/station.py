import json
import pymysql
import SqlDir.code_list_table
import SqlDir.station_table
import SqlDir.city_table

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db')
cur = conn.cursor()

#检查英文代码是否存在
def match(cityCode):
    row = SqlDir.station_table.getCityCodeList()
    for i in row:
        if i[0] == cityCode:
            return 1
    return 0

#检查写入车站信息
def outPut(id_1,id_2,str):
    str_json = json.loads(str)
    for code in str_json['data']['map']:
        if str_json['data']['map'][code] != SqlDir.city_table.selectNameChineseById(id_1) and str_json['data']['map'][code] != SqlDir.city_table.selectNameChineseById(id_2):
            if match(code) == 0:
                SqlDir.station_table.insertStation(code,str_json['data']['map'][code],id_1)

#检查写入主车站信息
def outPut2(id_1,id_2,str):
    str_json = json.loads(str)
    for code in str_json['data']['map']:
        if str_json['data']['map'][code] == SqlDir.city_table.selectNameChineseById(id_1):
            if match(code) == 0:
                SqlDir.station_table.insertStation(code,str_json['data']['map'][code],id_1)
        else:
            if str_json['data']['map'][code] == SqlDir.city_table.selectNameChineseById(id_2):
                if match(code) == 0:
                    SqlDir.station_table.insertStation(code,str_json['data']['map'][code],id_2)

#主方法
def function():
    id = 0
    for city_1 in range(1,34):
        for city_2 in range(1,34):
            if city_1 != city_2:
                id+=1
                outPut(city_1,city_2,SqlDir.code_list_table.getCode(id))
                print(id)

function()

