"""
    作者：wcz
    版本：v8.0
    日期：27/06/18
    功能：AQI计算
    获取所有城市的aqi
    保存到CSV
    pandas
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data.head(5))
    # print(aqi_data[['AQI', 'no2/h']])
    print('基本信息')
    print(aqi_data.info())

    print('数据预览')
    print(aqi_data.head())

    # 数据清洗
    # 只保留AQI > 0 的数据
    filter_conditon = aqi_data['AQI'] > 0
    clear_aqi_data = aqi_data[filter_conditon]

    # 基本统计
    print('AQI最大值', clear_aqi_data['AQI'].max())
    print('AQI最小值', clear_aqi_data['AQI'].min())
    print('AQI平均值', clear_aqi_data['AQI'].mean())

    # top50
    top50_cities = clear_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='city', y='AQI', title='空气质量最佳50城市', figsize=(20, 10))
    # plt.savefig('top50_aqi.png')
    plt.show()


if __name__ == '__main__':
    main()
