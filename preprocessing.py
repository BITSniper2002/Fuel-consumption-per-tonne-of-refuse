import pandas as pd

def excel_to_csv(input_file):
    # 读取Excel文件中的每个工作表
    excel_data = pd.read_excel(input_file, sheet_name=None)

    # 遍历每个工作表，将其保存为CSV文件
    for sheet_name, data_frame in excel_data.items():
        if sheet_name in ['加油记录','垃圾量记录']:
            csv_file = f"{sheet_name}.csv"  # 根据工作表名称生成CSV文件名
            data_frame.to_csv(csv_file, index=False)

# 调用函数来读取Excel文件并保存为CSV文件
input_file = "./融江金顺每辆车每次加油的吨垃圾油耗表(1).xlsx"  # 输入的Excel文件名
excel_to_csv(input_file)