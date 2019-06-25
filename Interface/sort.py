import tool

#按花费时间递增排序
def timeCost(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-i-1):
            time = tool.timeToMin(list[j]['cost'])
            time1 = tool.timeToMin(list[j+1]['cost'])
            if time > time1:
                list[j],list[j+1] = list[j+1],list[j]
    return list

#按价格递增排序
def priceCost(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-i-1):
            price = tool.priceToFloat(list[j]['price'])
            price1 = tool.priceToFloat(list[j+1]['price'])
            if price > price1:
                list[j],list[j+1] = list[j+1],list[j]
    return list

#按到达时间递增排序
def toTime(list):
    newList = tool.getTopTen(timeCost(list),10)
    for i in range(0,len(newList)-1):
        for j in range(0,len(newList)-i-1):
            toTime = tool.timeToMin(newList[j]['to_time'])
            toTime1 = tool.timeToMin(newList[j+1]['to_time'])
            if toTime > toTime1:
                newList[j],newList[j+1] = newList[j+1],newList[j]
    return newList

#综合排序
def multJu(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-i-1):
            costTime = tool.timeToMin(list[j]['cost'])
            costTime1 = tool.timeToMin(list[j+1]['cost'])
            price = int(tool.priceToFloat(list[j]['price']))
            price1 = int(tool.priceToFloat(list[j+1]['price']))
            multIn = costTime * 0.4 + price
            multIn1 = costTime1 * 0.4 + price1
            if multIn > multIn1:
                list[j],list[j+1] = list[j+1],list[j]
    return list