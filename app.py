from bottle import run,route,template,request,error,response,static_file
import Interface.distance
import SqlDir.city_table
import MainMethod.timeLeast
import MainMethod.multJudge
import MainMethod.costLeast
import MainMethod.firstArrive
import tool
import json

response.headers['Access-Control-Allow-Origin'] = '*'
response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
allow_headers = 'Referer, Accept, Origin, User-Agent, Content-Type'
response.headers['Access-Control-Allow-Headers'] = allow_headers

#系统首页
@route('/index')
def index():
    return template('index')

#城市列表请求
@route('/rail')
def rail():
    list = tool.selectAllCity()
    return json.dumps(list)

#中转城市请求
@route('/transCityList')
def midList():
    fromCity = request.query.from_city
    toCity = request.query.to_city
    list = Interface.distance.connectedDistanceList(SqlDir.city_table.selectNameCodeByChinese(fromCity),SqlDir.city_table.selectNameCodeByChinese(toCity))
    return json.dumps(list)

#方案请求
@route('/resuList')
def resuList():
    fromCity = request.query.from_city
    toCity = request.query.to_city
    midCity = request.query.mid_city
    type = request.query.type
    typeFirstSql = tool.trainType(request.query.typeFirst)
    typeSecondSql = tool.trainType(request.query.typeSecond)
    if type == "综合排序":
        resu = MainMethod.multJudge.multJudge(SqlDir.city_table.selectNameCodeByChinese(fromCity),
                                              SqlDir.city_table.selectNameCodeByChinese(midCity),
                                              SqlDir.city_table.selectNameCodeByChinese(toCity),typeFirstSql,typeSecondSql)
    elif type == "耗时优先":
        resu = MainMethod.timeLeast.timeLeast(SqlDir.city_table.selectNameCodeByChinese(fromCity),
                                              SqlDir.city_table.selectNameCodeByChinese(midCity),
                                              SqlDir.city_table.selectNameCodeByChinese(toCity),typeFirstSql,typeSecondSql)
    elif type == "价格优先":
        resu = MainMethod.costLeast.costLeast(SqlDir.city_table.selectNameCodeByChinese(fromCity),
                                              SqlDir.city_table.selectNameCodeByChinese(midCity),
                                              SqlDir.city_table.selectNameCodeByChinese(toCity),typeFirstSql,typeSecondSql)
    elif type == "率先到达":
        resu = MainMethod.firstArrive.firstArrive(SqlDir.city_table.selectNameCodeByChinese(fromCity),
                                                  SqlDir.city_table.selectNameCodeByChinese(midCity),
                                                  SqlDir.city_table.selectNameCodeByChinese(toCity),typeFirstSql,typeSecondSql)
    return json.dumps(resu)

#搜索按钮跳转展示页
@route('/search')
def searchResult():
    fromCity = request.query.from_city
    toCity = request.query.to_city
    if fromCity == toCity:
        return template('error_no', fromCity=fromCity, toCity=toCity)
    list = Interface.distance.connectedDistanceList(SqlDir.city_table.selectNameCodeByChinese(fromCity),SqlDir.city_table.selectNameCodeByChinese(toCity))
    if list:
        return template('result', fromCity=fromCity,toCity=toCity,midCity=list[0])
    else:
        return template('error_no', fromCity=fromCity, toCity=toCity)

#指定中转城市展示页
@route('/appoint')
def appointResult():
    fromCity = request.query.from_city
    toCity = request.query.to_city
    midCity = request.query.mid_city
    return template('appointMidcity', fromCity=fromCity, toCity=toCity, midCity=midCity)

    #if fromCity == toCity:
        #return template('error_no', fromCity=fromCity, toCity=toCity)
    #return template('result', fromCity=fromCity,toCity=toCity,midCity=midCity)

#定义图片路径
@route('/img/<filename:re:.*\.png>')
def server_static(filename):
    return static_file(filename, root='./images')

@route('/favicon.ico')
def server_static():
    return static_file('favicon.ico', root='./images')

@error(404)
def error404(error):
    return '请求的网页不存在'

@error(500)
def error500(error):
    return '内部服务器错误'

run(host='localhost',port=8080)