# coding=utf-8
import re
import pymysql
import requests
import json
import SqlDir.city_table
import SqlDir.station_table
import SqlDir.code_list_table
import SqlDir.train_table

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db')
cur = conn.cursor()
total = 0

#访问链接
def getIndex(url):
    respose = requests.get(url)
    if respose.status_code == 200:
        return respose.text

#获得沿途车次url
def getStationListUrl(number):
    url_head = 'https://kyfw.12306.cn/otn/queryTrainInfo/query?leftTicketDTO.train_no='
    url_bottom = '&leftTicketDTO.train_date=2019-04-26&rand_code='
    url = url_head + number + url_bottom
    return url

#获得价格url
def getPriceUrl(number,fromNo,toNo,type):
    url_head = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no='
    url = url_head + number + '&from_station_no=' + fromNo + '&to_station_no=' + toNo + '&seat_types=' + type + '&train_date=2019-04-28'
    return url

#主方法
def function():
    id = 0
    for city_1 in range(1, 34):
        for city_2 in range(1, 34):
            if city_1 != city_2:
                id += 1
                print('')
                print('')
                print('正在处理第:'+str(id)+'条信息')
                analysis(SqlDir.city_table.selectNameCodeById(city_1),SqlDir.city_table.selectNameCodeById(city_2),SqlDir.code_list_table.getCode(id))

#抽取信息
def analysis(fromCity,toCity,strin):
    str_json = json.loads(strin)
    for code in str_json['data']['result']:
        stuffs = re.split('\|', code)
        global total
        total+=1
        if '预订'== stuffs[1]:
            print(fromCity+ '编号：' + stuffs[2] + ' 车次:'+stuffs[3] +'   出发站：'+ stuffs[6] + '   目的站：' +stuffs[7] + ' 出发时间：' +stuffs[8] + '  到达时间：'+ stuffs[9] + ' 耗时：'+ stuffs[10]+ '    第'+str(total)+'条车次信息'+'  目的地：'+toCity)
            price = priceOfTicket(fromCity, toCity, stuffs[2],stuffs[35])
            print('价格：' + price)
            list = [stuffs[3],stuffs[6],stuffs[7],stuffs[8],stuffs[9],stuffs[10],toCity,price]
            SqlDir.train_table.insertNumber(fromCity,list)

#查找价格
def priceOfTicket(fromCity,toCity,number,type):
    stationUrl = getStationListUrl(number)
    print(getIndex(stationUrl))
    fromCityNumber = numberOfCity(getIndex(stationUrl),SqlDir.city_table.selectIdByCode(fromCity))
    toCityNumber = numberOfCity(getIndex(stationUrl),SqlDir.city_table.selectIdByCode(toCity))
    if fromCityNumber != 'null' and toCityNumber != 'null':
        priceUrl = getPriceUrl(number, fromCityNumber, toCityNumber,type)
        print(priceUrl)
        str_json = json.loads(getIndex(priceUrl))
        print(str_json)
        try:
            return str_json['data']['WZ']
        except:
            return priceUrl
    else:
        return number

#检测是否中文
def isChinese(strin):
    for ch in strin:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False



#查找城市站次
def numberOfCity(code,city):
    str_json = json.loads(code)
    station_list = SqlDir.station_table.selectStationNameByCityId(city)
    index = 0
    if not str_json['data']['data']:
        return 'null'
    for i in str_json['data']['data']:
        index = index + 1
        for j in station_list:
            if i['station_name'] == j[0]:
                if index < 10:
                    return '0'+str(index)
                else:
                    return str(index)
    return 'null'


#function()
#analysis('shh','sjp',getCode(55))
#numberOfCity(getIndex(getStationListUrl('240000G1490W')),Tool.city.selectIdByCode('shh'))




