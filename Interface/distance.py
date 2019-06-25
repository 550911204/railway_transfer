import Interface.connected
import SqlDir.city_table
import SqlDir.distance_table
import tool

#根据地理位置进一步排除不合逻辑中转城市
def connectedDistanceList(start,end):
    listDitail = []
    list = Interface.connected.connectedTheoryList(start,end)
    for i in list:
        dis = SqlDir.distance_table.selectDistance(SqlDir.city_table.selectNameChineseByCode(start),SqlDir.city_table.selectNameChineseByCode(i))
        dis2 = SqlDir.distance_table.selectDistance(SqlDir.city_table.selectNameChineseByCode(i),SqlDir.city_table.selectNameChineseByCode(end))
        directDis = SqlDir.distance_table.selectDistance(SqlDir.city_table.selectNameChineseByCode(start),SqlDir.city_table.selectNameChineseByCode(end))
        if( (dis + dis2) < directDis * 1.1):
            listDitail.append(SqlDir.city_table.selectNameChineseByCode(i))
            print('   中转城市：'+ SqlDir.city_table.selectNameChineseByCode(i))
    if len(listDitail) > 4:
        return listDitail
    else:
        listDitail2 = []
        for i in list:
            dis = SqlDir.distance_table.selectDistance(SqlDir.city_table.selectNameChineseByCode(start),SqlDir.city_table.selectNameChineseByCode(i))
            dis2 = SqlDir.distance_table.selectDistance(SqlDir.city_table.selectNameChineseByCode(i),SqlDir.city_table.selectNameChineseByCode(end))
            collection = []
            collection.append(i)
            collection.append(dis + dis2)
            listDitail2.append(collection)
        for i in range(0, len(listDitail2) - 1):
            for j in range(0, len(listDitail2) - i - 1):
                dis = listDitail2[j][1]
                dis2 = listDitail2[j+1][1]
                if dis > dis2:
                    listDitail2[j], listDitail2[j + 1] = listDitail2[j + 1], listDitail2[j]
        finalList = tool.getTopTen(listDitail2,3)
        subList = []
        for i in finalList:
            subList.append(SqlDir.city_table.selectNameChineseByCode(i[0]))
        return subList