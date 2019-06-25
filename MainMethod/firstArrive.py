import Interface.connected
import Interface.sort
import SqlDir.train_table
import SqlDir.station_table
import tool

#最先到达方案
def firstArrive(start,mid,end,typeFirstSql,typeSecondSql):
    flag = 1
    resultList = []
    list = Interface.sort.toTime(SqlDir.train_table.selectByCity(start,mid,typeFirstSql))
    listNext = Interface.sort.toTime(SqlDir.train_table.selectByCity(mid,end,typeSecondSql))
    if len(list)==0 or len(listNext)==0:
        return
    elif len(list)<=3 or len(listNext)<=3:
        flag = 0
    for i in list:
        midTimeStart = tool.timeToMin(i['to_time'])
        for j in listNext:
            midTimeEnd = tool.timeToMin(j['start_time'])
            if(midTimeEnd > midTimeStart + 60 ):
                collection = []
                stayTime = tool.timeToHoure(midTimeEnd - midTimeStart)
                wholeCost = tool.timeToHoure(
                    tool.timeToMin(i['cost']) + tool.timeToMin(j['cost']) + midTimeEnd - midTimeStart)
                wholePrice = '￥' + str(tool.priceToFloat(i['price']) + tool.priceToFloat(j['price']))
                list3 = {'stay_time': stayTime, 'whole_cost': wholeCost, 'whole_price': wholePrice}
                collection.append(i)
                collection.append(j)
                collection.append(list3)
                resultList.append(collection)
                if flag == 1:
                    break
            else:
                if listNext.index(j) == len(listNext) - 1:
                    break
    return tool.getTopTen(resultList,10)