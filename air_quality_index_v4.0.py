"""
    作者：wcz
    版本：v1.0
    日期：26/06/18
    功能：AQI计算
"""
import csv
import json
import os


def process_json_file(filepath):
    """
        解码json文件
    """
    # f = open(filepath, 'r', encoding='utf-8')
    # city_list = json.load(f)
    # f.close()
    print('json文件')
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)

    print(city_list)


def process_csv_file(filepath):
    """
        解码json文件
    """
    # f = open(filepath, 'r', encoding='utf-8')
    # city_list = json.load(f)
    # f.close()
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))

        city_list = json.load(f)

    print(city_list)


def main():
    """
        主函数
    """
    filepath = input('请输入文件名称：')
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        # json文件
        process_json_file(filepath)
    elif file_ext == '.csv':
        # csv文件
        process_csv_file(filepath)
    else:
        print('不支持的文件格式')


    # city_list = process_json_file(filepath)
    # city_list.sort(key=lambda city: city['aqi'])
    #
    # lines = []
    # lines.append(list(city_list[0].keys()))
    # for city in city_list:
    #     lines.append(list(city.values()))
    #
    # f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    # writer = csv.writer(f)
    # for line in lines:
    #     writer.writerow(line)
    # f.close()


if __name__ == '__main__':
    main()
