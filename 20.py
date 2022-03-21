import random
from random import randint       #引用random库


times = eval(input("请输入试验次数:"))
get_car_without_change = 0 #定义试验未开始时坚持选择得到车的次数为0
get_car_with_change = 0  #定义试验未开始时改变选择得到车的次数为0



for i in range(times):
    #假设门后物品未知，随机一个变成车
    doors = ['thing','thing','thing']
    #from random import randint
    car_id = random.randint(0,2)
    doors[car_id] = 'car'


    #定义初始选择为三扇门随机一个，我们不知道每扇门后有什么，也不知道自己选择的门后有什么
    #from random import randint
    my_choice = random.randint(0,2)


    #如果不更换就选中车，则初始选择必然是车，此时试验中坚持选择得到车的次数加1
    if my_choice == car_id:
         get_car_with_change += 1


P_change = get_car_with_change / times #用试验中改变选择得到车的次数/试验总次数得到改变选择得到车的概率
P_Not_change = get_car_without_change / times #用试验中坚持选择得到车的次数/试验总次数得到坚持选择得到车的概率
print("试验中改变选择得到车的概率为:",P_change)
print("试验中坚持选择得到车的概率为:",P_Not_change)
