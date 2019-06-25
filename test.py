import time
import json

import Interface.distance
import SqlDir.city_table
import MainMethod.timeLeast
import MainMethod.costLeast
import MainMethod.firstArrive
import MainMethod.multJudge


startCity = '北京'
toCity = '天津'
print('请输入起始城市：'+startCity)
print('请输入终点城市：'+toCity)

#start=time.clock()
#筛选出理论合理中转城市集合(参数：起点城市、终点城市)
list = Interface.distance.connectedDistanceList(SqlDir.city_table.selectNameCodeByChinese(startCity),SqlDir.city_table.selectNameCodeByChinese(toCity))
#给出具体乘车方案参数：起点城市、中转城市、终点城市)

#耗时最少
#resu =MainMethod.timeLeast.timeLeast(SqlDir.city_table.selectNameCodeByChinese(startCity),SqlDir.city_table.selectNameCodeByChinese(list[0]),SqlDir.city_table.selectNameCodeByChinese(toCity))
#花费最少
#print(MainMethod.costLeast.costLeast(SqlDir.city_table.selectNameCodeByChinese(startCity),SqlDir.city_table.selectNameCodeByChinese(list[0]),SqlDir.city_table.selectNameCodeByChinese(toCity)))

#最早到达
#print(MainMethod.firstArrive.firstArrive(SqlDir.city_table.selectNameCodeByChinese(startCity),SqlDir.city_table.selectNameCodeByChinese(list[0]),SqlDir.city_table.selectNameCodeByChinese(toCity)))

#综合排序
#resu =MainMethod.multJudge.multJudge(SqlDir.city_table.selectNameCodeByChinese(startCity),SqlDir.city_table.selectNameCodeByChinese(list[0]),SqlDir.city_table.selectNameCodeByChinese(toCity))
#end=time.clock()
#print("final is in ",end-start)