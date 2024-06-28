import os


def get_all_files(directory):
    # 获取指定目录下的所有文件和目录
    entries = os.listdir(directory)
    # 只保留文件
    files = [file for file in entries if os.path.isfile(os.path.join(directory, file))]
    return files


def get_output_file_name(input_file_path):
    # 分离文件路径、文件名和扩展名
    dir_name = os.path.dirname(input_file_path)
    base_name = os.path.basename(input_file_path)
    file_name, file_extension = os.path.splitext(base_name)

    # 构造输出文件名
    output_file_name = f"{file_name}_output{file_extension}"

    # 构造输出文件路径
    output_file_path = os.path.join(dir_name, output_file_name)

    return output_file_path