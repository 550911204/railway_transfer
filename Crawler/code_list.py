import requests
import pymysql
import SqlDir.city_table
import SqlDir.code_list_table

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='rail_db')
cur = conn.cursor()

#访问链接
def getIndex(url):
    respose = requests.get(url)
    if respose.status_code == 200:
        return respose.text

#组装url链接
def getUrl(id_1,id_2):
    url_head = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-04-27&leftTicketDTO.from_station='
    url_mid = '&leftTicketDTO.to_station='
    url_bottom = '&purpose_codes=ADULT'
    from_city = SqlDir.city_table.selectNameCodeById(id_1)
    to_city = SqlDir.city_table.selectNameCodeById(id_2)
    url = url_head + from_city +url_mid + to_city + url_bottom
    return url

#主方法
def function():
    total = 1
    for city_1 in range(1,34):
        for city_2 in range(1,34):
            if city_1 != city_2:
                url = getUrl(city_1,city_2)
                result = getIndex(url)
                print('第'+str(total)+'条：')
                total = total + 1
                print('出发城市:'+SqlDir.city_table.selectNameCodeById(city_1))
                print('目的城市:' + SqlDir.city_table.selectNameCodeById(city_2))
                print('信息:' + result)
                SqlDir.code_list_table.insertCodeList(result)

function()