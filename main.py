from datetime import datetime
import os
import matplotlib.pyplot as plt
import numpy as np

def is_time_in_range(target_time, start_time, end_time):
    # 将输入的时间字符串转换为datetime对象
    target = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    # 判断给定时间是否在范围内
    if start <= target <= end:
        return True
    else:
        return False

def time_exceed(target_time,end_time):
    # 将输入的时间字符串转换为datetime对象
    target = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    # 判断给定时间是否在范围内
    if end < target:
        return True
    else:
        return False

#filepath1 是垃圾相关， filepath2 是加油相关
def consume(filepath1,filepath2):
    #开辟五个数组来存放加油时间，加油量，过磅时间，净重，两次加油之间的总垃圾重量
    time_fuel,fuel_amount = [],[]
    time_laji,net_weight = [],[]
    total = []

    with open(filepath1, 'r', newline='') as csvfile:
        reader = csvfile.readlines()
        title = reader.pop(0).split(',')
        p1,p2 = 0,0
        for i in range(len(title)):
            if '过磅时间' in title[i]:
                p1 = i
            elif '垃圾净重' in title[i]:
                p2 = i
        for i in range(len(reader)):
            reader[i] = reader[i].split(',')
        for item in reader:
            time_laji.append(item[p1])
            net_weight.append(item[p2])
        # print(time_laji,net_weight)

    with open(filepath2, 'r', newline='') as csvfile:
        reader = csvfile.readlines()
        title = reader.pop(0).split(',')
        p1,p2 = 0,0
        for i in range(len(title)):
            if '加油时间' in title[i]:
                p1 = i
            elif '加油量' in title[i]:
                p2 = i
        for i in range(len(reader)):
            reader[i] = reader[i].split(',')
        for item in reader:
            time_fuel.append(item[p1])
            fuel_amount.append(float(item[p2]))
        # print(time_fuel,fuel_amount)

    i = 1
    #上一次遍历到第几个时间点
    last = 0
    while i < len(time_fuel):
        start,end = time_fuel[i-1],time_fuel[i]
        #此次垃圾总重
        cur = 0
        for j in range(last,len(time_laji)):
            time = time_laji[j]
            if is_time_in_range(time,start,end):
                try:
                    cur += int(net_weight[j])
                except ValueError:
                    cur += 0
            elif time_exceed(time,end):
                last = j
                break
        total.append(cur)
        i += 1
        if j == len(time_laji)-1:
            break
    ton = []
    for i in range(len(total)):
    #吨油耗
        tmp = round(fuel_amount[i] / total[i] * 1000, 2) if total[i] else 0
        ton.append(tmp)
    # print(len(fuel_amount),len(total))
    return ton

# 定义文件夹路径
folder_path1 = './垃圾'
folder_path2 = './加油'
f1,f2 = [],[]
# 遍历文件夹下的所有文件
for filename in os.listdir(folder_path1):
    # 拼接文件路径
    filepath = os.path.join(folder_path1, filename)
    if 'csv' in filepath:
        f1.append(filepath)
for filename in os.listdir(folder_path2):
    # 拼接文件路径
    filepath = os.path.join(folder_path2, filename)
    if 'csv' in filepath:
        f2.append(filepath)
f1.sort()
f2.sort()
# print(f1,'\n',f2)
# print(f1[0][5:12])
for i in range(len(f1)):
    res = consume(f1[i],f2[i])
    mean_value = sum(res)/len(res)
    max_range = mean_value*1.1
    plt.figure()
    x = range(len(res))
    y = res
    plt.plot(x, y)
    # 添加平均值线
    plt.axhline(y=mean_value, color='r', linestyle='--')
    plt.axhline(y=max_range, color='black', linestyle='--')
    # 添加标签和标题
    plt.xlabel('Number of times refuelled')
    plt.ylabel('Fuel consumption per tonne of refuse')
    plt.title('Fuel consumption per tonne of refuse')
    # 显示图形
    plt.savefig('./图片/' + f1[i][5:12] + '.png')
    mean_value = sum(res) / len(res)
    variance = np.var(res)
    max_value, min_value = max(res), min(res)

    # 打开total文件，选择在文件后面添加内容的写入方式，写入最大值、最小值、平均值、方差
    with open('./吨垃圾油耗.txt', 'a') as file:
        file.write(f1[i][5:12]+':')
        file.write('最大值：' + str(round(max_value, 2)) + '最小值：' + str(round(min_value, 2)) +
                   '平均值：' + str(round(mean_value, 2)) + '方差：' + str(round(variance, 2)) + '\n')




