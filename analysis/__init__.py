import os

import pandas as pd

# import pandas as pd

# 读取Excel文件
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = desktop_path + '\\test.xlsx'  # 替换为你的Excel文件路径
print("file path is " + file_path)
df = pd.read_excel(file_path)

# 打印整个数据框
print("Excel文件中的数据:")
print(df)

# 解析并打印每一列的数据
# print("\n解析每一列的数据:")
for column in df.columns:
    print(f"\n列名: {column}")
    print(df[column])


