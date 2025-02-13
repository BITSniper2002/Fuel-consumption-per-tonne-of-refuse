import csv

#列表用于存储每一辆不同的车
distinct_car = []

#打开前面处理完的文件
with open('加油记录.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    pos_che = 0
    for row in reader:
        if '车牌号' in row:
            #找到车牌号所在的列
            pos_che = row.index('车牌号')
            break
    for row in reader:
        #寻找独特的车牌号
        if row[pos_che] not in distinct_car and row[pos_che] != '车牌号':
            distinct_car.append(row[pos_che])


#打开前面处理完的文件
with open('加油记录.csv', 'r', newline='') as csvfile:
    reader = csvfile.readlines()
    reader.pop(0)
    #读取标题
    title = reader[0].split(',')
    pos = 0
    for i in range(len(title)):
        if '加油量' in title[i]:
            pos = i
    #将每一辆不同的车的相关信息都输出到其相应的csv文件（在加油文件夹下）
    for i in range(len(distinct_car)):
        tmp = distinct_car[i]
        data = []
        for row in reader:
            new_row = row.split(',')
            if tmp in row and new_row[pos]:
                data.append(row)
        # print(data)
        with open('./加油/'+tmp+'加油.csv', 'w', newline='') as new_csvfile:
            new_csvfile.writelines(','.join(title))
            new_csvfile.writelines(data)

#打开前面处理完的文件
with open('垃圾量记录.csv', 'r', newline='') as csvfile:
    reader = csvfile.readlines()
    reader.pop(0)
    #读取标题
    title = reader[0]
    #将每一辆不同的车的相关信息都输出到其相应的csv文件（在垃圾文件夹下）
    for i in range(len(distinct_car)):
        tmp = distinct_car[i]
        data = []
        for row in reader:
            if tmp in row:
                data.append(row)
        # print(data)
        with open('./垃圾/'+tmp+'垃圾.csv', 'w', newline='') as new_csvfile:
            new_csvfile.writelines(title)
            new_csvfile.writelines(data)

