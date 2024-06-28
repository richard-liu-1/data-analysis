import os

import pandas as pd

from file_utils import get_all_files
from file_utils import get_output_file_name


def analysis_test(file_path):
    print("file path is " + file_path)
    df = pd.read_excel(file_path)
    selected_columns = [4, 8, 10, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
    result_list = []
    for index, row in df.iterrows():
        # 获取指定列的单元格数据
        if index is 0:
            continue
        selected_data = [row.iloc[i - 1] for i in selected_columns]  # i-1 because index starts from 0
        random_no = selected_data[0]
        sex = selected_data[1]
        age = selected_data[2]
        first_avg_bp = cal_avg_bp(selected_data, 3, index)
        second_avg_bp = cal_avg_bp(selected_data, 9, index)
        if not first_avg_bp or not second_avg_bp:
            print(f"第{index + 1}行数据为空，将跳过该行记录")
            result_list.append({"number": index})
            continue
        if first_avg_bp[0] > second_avg_bp[0]:
            final_avg_bp = first_avg_bp
        else:
            final_avg_bp = second_avg_bp
        result_object = {"number": index, "random_no": random_no, "age": age, "sex": sex,
                         "first_avg_sbp": first_avg_bp[0],
                         "first_avg_dbp": first_avg_bp[1], "second_avg_sbp": second_avg_bp[0],
                         "second_avg_dbp": second_avg_bp[1],
                         "final_avg_sbp": final_avg_bp[0], "final_avg_dbp": final_avg_bp[1]}
        result_list.append(result_object)
        print(
            f"第{index + 1}行, 随机号: {random_no}， 年龄·：{age}，性别：{sex}")
    return result_list


def cal_avg_bp(selected_data, start_index, index_num):
    first_sbp = selected_data[start_index]
    first_dbp = selected_data[start_index + 1]
    second_sbp = selected_data[start_index + 2]
    second_dbp = selected_data[start_index + 3]
    if pd.isna(first_sbp) or pd.isna(second_sbp):
        return []
    if first_sbp - second_sbp < 5:
        average_sbp = (first_sbp + second_sbp) / 2
        average_dbp = (first_dbp + second_dbp) / 2
    else:
        average_sbp = round(((first_sbp + second_sbp + selected_data[start_index + 4]) / 3), 1)
        average_dbp = round(((first_dbp + second_dbp + selected_data[start_index + 5]) / 3), 1)
    return [average_sbp, average_dbp]


def handle_bp_data(input_path):
    # path = "F:\wife_data_analysis\original_st.xls"
    excel_list = analysis_test(input_path)
    df = pd.DataFrame(excel_list)
    # 导出到 Excel 文件
    # output_path = "F:\wife_data_analysis\out_excel\output.xlsx"
    # 检查文件是否存在，存在则删除
    output_file_name = get_output_file_name(input_path)
    print(f"根据输入文件{input_path} 得到输出文件：{output_file_name}")
    if os.path.exists(output_file_name):
        os.remove(output_file_name)
    df.to_excel(output_file_name, index=False)


if __name__ == "__main__":
    dictionary_path = 'F:\\wife_data_analysis\\first_batch\\'
    file_names = get_all_files(dictionary_path)
    for file_name in file_names:
        if file_name.endswith('xlsx') or file_name.endswith('xls'):
            handle_bp_data(dictionary_path + file_name)
