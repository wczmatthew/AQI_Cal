"""
    作者：wcz
    版本：v1.0
    日期：26/06/18
    功能：AQI计算
"""
import json


def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, 'r', encoding='utf-8')
    city_list = json.load(f)
    f.close()

    return city_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    top3_list = city_list[:3]

    f = open('top3_aqi.json', 'w', encoding='utf-8')
    json.dump(top3_list, f, ensure_ascii=False)
    f.close()

    print(city_list)

if __name__ == '__main__':
    main()
