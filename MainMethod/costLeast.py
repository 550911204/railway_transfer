import Interface.connected
import Interface.sort
import SqlDir.train_table
import SqlDir.city_table
import SqlDir.station_table
import tool

#花费时间最少方案
def costLeast(start,mid,end,typeFirstSql,typeSecondSql):
    flag = 1
    resultList = []
    list = Interface.sort.priceCost(SqlDir.train_table.selectByCity(start,mid,typeFirstSql))
    listNext = Interface.sort.priceCost(SqlDir.train_table.selectByCity(mid,end,typeSecondSql))
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
    #处理结果  因为前半程最少加符合最少合起来不一定最少
    listPrint = computeResult(resultList)
    return listPrint


#处理结果
def computeResult(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-i-1):
            price = tool.priceToFloat(list[j][0]['price']) + tool.priceToFloat(list[j][1]['price'])
            price1 = tool.priceToFloat(list[j+1][0]['price']) + tool.priceToFloat(list[j+1][1]['price'])
            if price > price1:
                list[j],list[j+1] = list[j+1],list[j]
    return tool.getTopTen(list,10)