"""
    作者：wcz
    版本：v1.0
    日期：26/06/18
    功能：AQI计算
"""


def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
        范围缩放
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi -bp_lo) + iaqi_lo

    return iaqi


def cal_pm_iaqi(pm_val):
    """
        计算pm2.5的AQI
    """
    if 0 <= pm_val < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    elif 36 <= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    else:
        pass
    return iaqi


def cal_co_iaqi(co_val):
    """
        计算co的AQI
    """
    if 0 <= co_val < 3:
        iaqi = cal_linear(0, 50, 0, 3, co_val)
    elif 3 <= co_val < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    # elif 76 <= co_val < 116:
    #     iaqi = cal_linear(100, 150, 75, 115, co_val)
    else:
        pass
    return iaqi



def cal_aqi(param_list):
    """
        AQI计算
    """
    pm_val = param_list[0]
    co_val = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    iaqi_list = [pm_iaqi, co_iaqi]
    iaqi = max(iaqi_list)

    return iaqi


def main():
    """
        主函数
    """
    print("输入以下信息，用空格分割")
    input_str = input('(1)PM2.5 (2)CO：')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    # 调用AQI计算
    aqi_val = cal_aqi(param_list)

    print('空气质量指数为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
