#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import datetime


def get_rank_from_flag(x, cluster_centers):
    sort_cluster_centers = sorted([i[0] for i in cluster_centers])
    if len(sort_cluster_centers) <= 1:
        return '低'
    low = sort_cluster_centers[0]
    medium = sort_cluster_centers[1]
    aim = cluster_centers[x][0]
    if aim == low:
        return '低'
    elif aim == medium:
        return '中'
    else:
        return '高'


def time_standard(time_list):
    res = []
    tmp_res = []
    left = 0
    right = 0
    while left < len(time_list):
        if right >= len(time_list):
            tmp_res.append([time_list[left], time_list[-1]])
            break
        if (right - left) * 0.5 == time_list[right] - time_list[left]:
            right += 1
        else:
            tmp_res.append([time_list[left], time_list[right - 1]])
            left = right

    for tmp in tmp_res:
        if tmp[0] == tmp[1]:
            if int(tmp[0]) == tmp[0]:
                res.append(str(int(tmp[0])) + ':00~' + str(int(tmp[0])) + ':30')
            else:
                res.append(str(int(tmp[0])) + ':30~' + str(int(tmp[0]) + 1) + ':00')
        else:
            if int(tmp[0]) == tmp[0] and int(tmp[1]) == tmp[1]:
                res.append(str(int(tmp[0])) + ':00~' + str(int(tmp[1])) + ':30')
            elif int(tmp[0]) == tmp[0] and int(tmp[1]) != tmp[1]:
                res.append(str(int(tmp[0])) + ':00~' + str(int(tmp[1]) + 1) + ':00')
            elif int(tmp[0]) != tmp[0] and int(tmp[1]) == tmp[1]:
                res.append(str(int(tmp[0])) + ':30~' + str(int(tmp[1])) + ':30')
            else:
                res.append(str(int(tmp[0])) + ':30~' + str(int(tmp[1]) + 1) + ':00')
    return res


def optimize_peak_period(supplier_group_id, res_df, cluster_way='flag_3_cluster', period_limit=6):
    new_res_df = res_df.copy()
    info = res_df.groupby([cluster_way])['order_num'].mean().reset_index()
    info = info.sort_values(by='order_num', ascending=False).reset_index(drop=True)
    if cluster_way == 'flag_3_cluster':
        high_flag_list = [info.iloc[0, 0]]
        medium_flag = info.iloc[1, 0]
    else:
        high_flag_list = [info.iloc[0, 0], info.iloc[1, 0]]
        medium_flag = info.iloc[2, 0]
    # 获取需要将高峰期转为中峰期的时间段
    need_change_time_list = change_high_to_medium(res_df, high_flag_list, cluster_way, period_limit)
    if len(need_change_time_list) > 0:
        new_res_df.loc[new_res_df['time'].isin(need_change_time_list), cluster_way] = medium_flag
        #print(supplier_group_id, need_change_time_list)
    return new_res_df


def change_high_to_medium(res_df, high_flag_list, cluster_way, period_limit):
    # 筛选高峰期的时间段和对应单量
    high_res_df = res_df.loc[res_df[cluster_way].isin(high_flag_list), ['time', 'order_num']].reset_index(drop=True)
    if len(high_res_df) <= period_limit:
        return []
    # 将预估单量排序，只保留单量最高的前period_limit个时间段
    high_res_df = high_res_df.sort_values(by='order_num', ascending=False).reset_index(drop=True)
    no_high_time_list = list(high_res_df.iloc[period_limit:, 0].values)
    return no_high_time_list


if __name__ == '__main__':
    # 读取数据
    whole_data = pd.read_csv('data/0321.csv')

    # 待预测的日期
    need_predict_datetime = datetime.datetime.strptime('2023-03-21', '%Y-%m-%d')
    # 近几天
    two_days_ago = (need_predict_datetime - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    three_days_ago = (need_predict_datetime - datetime.timedelta(days=2)).strftime('%Y-%m-%d')
    four_days_ago = (need_predict_datetime - datetime.timedelta(days=3)).strftime('%Y-%m-%d')
    # 近几周相同星期数
    one_week_ago = (need_predict_datetime - datetime.timedelta(days=7*1)).strftime('%Y-%m-%d')
    two_weeks_ago = (need_predict_datetime - datetime.timedelta(days=7*2)).strftime('%Y-%m-%d')
    three_weeks_ago = (need_predict_datetime - datetime.timedelta(days=7*3)).strftime('%Y-%m-%d')

    data = whole_data[
        whole_data['create_dt'].isin([two_days_ago, three_days_ago, four_days_ago, one_week_ago, two_weeks_ago, three_weeks_ago])]
    # 门店与门店组的对应关系调整
    """"""
    data.loc[data['id'].isin([120025169]), 'supplier_group_id'] = 100010772

    data.loc[data['id'].isin(
        [127089193, 153550556]), 'supplier_group_id'] = 100013163

    # data['supplier_group_id'] = data['supplier_group_id'].apply(lambda x: 100008544 if x == 100008500 else x)
    data = data[~data.isnull().T.any()].reset_index(drop=True)
    predict_data = pd.DataFrame(
        columns=['supplier_group_id', 'supplier_id_list', 'high_predict1', 'medium_predict1', 'low_predict1', 'high_medium_boundary1', 'medium_low_boundary1',
                 'high_predict2', 'medium_predict2', 'low_predict2', 'high_medium_boundary2', 'medium_low_boundary2'])
    # 各中心门店的品牌
    # 瑞幸门店组
    luckin_supplier_group = [100004332, 100008007, 100007909, 100007485, 100008353, 100008437, 100007487,
                             100008186, 100008165, 100007685, 100006643, 100002579, 100008606, 100007595, 100008307,
                             100006188, 100006184, 100007677, 100001183, 100007677, 100008021, 100007662, 100005488,
                             100009234, 100000916, 100009074, 100005186, 100008385, 100000428, 100007490, 100009039, 100008189,
                             100008246, 100008462, 100001967, 100008874, 100006176, 100007163, 100009287, 100004002, 100009472,
                             100008118, 100006115, 100006113, 100001820, 100009346, 100009657, 100009687, 100008876, 100009669,
                             100002092, 100008607, 100009678, 100006174, 100002124, 100004416, 100009337, 100009314, 100009337,
                             100009685, 100009644, 100009739, 100010305]
    # 奈雪的茶+麦当劳门店组
    naixue_maidanglao_supplier_group = [100008368, 100004500]
    # 奈雪的茶门店组
    naixue_supplier_group = [100007924, 100005043, 100001676, 100008311, 100007363, 100007389, 100003903, 100004434, 100008244, 100004373, 100003905]
    # 其它
    others_supplier_group = [100008548, 100008544, 100008404, 100008471, 100008140, 100007777, 100006385, 100008639, 100005761,
                             100004136, 100008092, 100003982, 100009217, 100008628, 100008561, 100005069, 100009025, 100008836,
                             100007656, 100007656, 100008854, 100008371, 100008644, 100009523, 100007476]

    """"""
    total_supplier_group = [100010772, 100013163]

    data = data[data['supplier_group_id'].isin(total_supplier_group)].reset_index(drop=True)

    # 遍历各个门店组
    print('************第一个for循环**************')
    for supplier_group_id in list(data['supplier_group_id'].unique()):
        # 瑞幸
        if supplier_group_id in luckin_supplier_group:
            alpha = 0.5
        # 奈雪的茶+麦当劳
        elif supplier_group_id in naixue_maidanglao_supplier_group:
            alpha = 0.5
        # 奈雪的茶
        elif supplier_group_id in naixue_supplier_group:
            alpha = 0.5
        else:
            alpha = 0.5

        supplier_id_list = list(set(data.loc[data['supplier_group_id'] == supplier_group_id, 'id'].values))
        tmp_data = data[data['supplier_group_id'] == supplier_group_id]
        tmp_tmp_data1_1 = tmp_data[tmp_data['create_dt'] == three_weeks_ago]
        tmp_tmp_data1_2 = tmp_data[tmp_data['create_dt'] == two_weeks_ago]
        tmp_tmp_data1_3 = tmp_data[tmp_data['create_dt'] == one_week_ago]

        tmp_tmp_data2_0 = tmp_data[tmp_data['create_dt'] == four_days_ago]
        tmp_tmp_data2_1 = tmp_data[tmp_data['create_dt'] == three_days_ago]
        tmp_tmp_data2_2 = tmp_data[tmp_data['create_dt'] == two_days_ago]

        # 两天前、三天前数据有缺失的，用四天前的数据或者两、三天前的完整数据替代
        if len(tmp_tmp_data2_1) == 0 or len(tmp_tmp_data2_2) == 0:
            if len(tmp_tmp_data2_0) > 0:
                if len(tmp_tmp_data2_1) == 0:
                    tmp_tmp_data2_1 = tmp_tmp_data2_0
                if len(tmp_tmp_data2_2) == 0:
                    tmp_tmp_data2_2 = tmp_tmp_data2_0
            else:
                if len(tmp_tmp_data2_1) > 0:
                    tmp_tmp_data2_2 = tmp_tmp_data2_1
                if len(tmp_tmp_data2_2) > 0:
                    tmp_tmp_data2_1 = tmp_tmp_data2_2
        # 一、二、三周前数据有缺失的，用一、二、三周的完整数据部分替代
        if len(tmp_tmp_data1_1) == 0 or len(tmp_tmp_data1_2) == 0 or len(tmp_tmp_data1_3) == 0:
            if len(tmp_tmp_data1_1)+len(tmp_tmp_data1_2)+len(tmp_tmp_data1_3) > 0:
                if len(tmp_tmp_data1_1) > 0:
                    if len(tmp_tmp_data1_2) == 0:
                        tmp_tmp_data1_2 = tmp_tmp_data1_1
                    if len(tmp_tmp_data1_3) == 0:
                        tmp_tmp_data1_3 = tmp_tmp_data1_1
                elif len(tmp_tmp_data1_2) > 0:
                    if len(tmp_tmp_data1_1) == 0:
                        tmp_tmp_data1_1 = tmp_tmp_data1_2
                    if len(tmp_tmp_data1_3) == 0:
                        tmp_tmp_data1_3 = tmp_tmp_data1_2
                else:
                    if len(tmp_tmp_data1_1) == 0:
                        tmp_tmp_data1_1 = tmp_tmp_data1_3
                    if len(tmp_tmp_data1_2) == 0:
                        tmp_tmp_data1_2 = tmp_tmp_data1_3

        # 如果两、三、四天前数据全部缺失或者一、二、三周前数据全部缺失，用未全部缺失的数据补充
        if len(tmp_tmp_data2_0)+len(tmp_tmp_data2_1)+len(tmp_tmp_data2_2) == 0 and len(tmp_tmp_data1_1)+len(tmp_tmp_data1_2)+len(tmp_tmp_data1_3) > 0:
            tmp_tmp_data2_0 = tmp_tmp_data1_1
            tmp_tmp_data2_1 = tmp_tmp_data1_2
            tmp_tmp_data2_2 = tmp_tmp_data1_3
        if len(tmp_tmp_data2_0)+len(tmp_tmp_data2_1)+len(tmp_tmp_data2_2) > 0 and len(tmp_tmp_data1_1)+len(tmp_tmp_data1_2)+len(tmp_tmp_data1_3) == 0:
            tmp_tmp_data1_1 = tmp_tmp_data2_1
            tmp_tmp_data1_2 = tmp_tmp_data2_2
            tmp_tmp_data1_3 = tmp_tmp_data2_2

        if len(tmp_tmp_data1_1) == 0 or len(tmp_tmp_data1_2) == 0 or len(tmp_tmp_data1_3) == 0 or len(tmp_tmp_data2_1) == 0 or len(tmp_tmp_data2_2) == 0:
            print('%%%%%%%', supplier_group_id)
            print(len(tmp_tmp_data1_1))
            print(len(tmp_tmp_data1_2))
            print(len(tmp_tmp_data1_3))
            print(len(tmp_tmp_data2_0))
            print(len(tmp_tmp_data2_1))
            print(len(tmp_tmp_data2_2))
            continue
        cleaned_tmp_data = {}
        # 合并同一个门店组下的中心门店数据
        # 三周前
        for i in range(len(tmp_tmp_data1_1)):
            row_data = [j.strip('"') for j in tmp_tmp_data1_1.iloc[i, 3].strip('[').strip(']').split(',')]
            for tmp in row_data:
                key = float(tmp.split(':')[0])
                value = float(tmp.split(':')[1])
                if key not in cleaned_tmp_data:
                    cleaned_tmp_data[key] = alpha * value / 3
                else:
                    cleaned_tmp_data[key] += alpha * value / 3
        # 两周前
        for i in range(len(tmp_tmp_data1_2)):
            row_data = [j.strip('"') for j in
                        tmp_tmp_data1_2.iloc[i, 3].strip('[').strip(']').split(',')]
            for tmp in row_data:
                key = float(tmp.split(':')[0])
                value = float(tmp.split(':')[1])
                if key not in cleaned_tmp_data:
                    cleaned_tmp_data[key] = alpha * value / 3
                else:
                    cleaned_tmp_data[key] += alpha * value / 3
        # 一周前
        for i in range(len(tmp_tmp_data1_3)):
            row_data = [j.strip('"') for j in
                        tmp_tmp_data1_3.iloc[i, 3].strip('[').strip(']').split(',')]
            for tmp in row_data:
                key = float(tmp.split(':')[0])
                value = float(tmp.split(':')[1])
                if key not in cleaned_tmp_data:
                    cleaned_tmp_data[key] = alpha * value / 3
                else:
                    cleaned_tmp_data[key] += alpha * value / 3
        # 三天前
        for i in range(len(tmp_tmp_data2_1)):
            row_data = [j.strip('"') for j in tmp_tmp_data2_1.iloc[i, 3].strip('[').strip(']').split(',')]
            for tmp in row_data:
                key = float(tmp.split(':')[0])
                value = float(tmp.split(':')[1])
                if key not in cleaned_tmp_data:
                    cleaned_tmp_data[key] = (1 - alpha) * value / 2
                else:
                    cleaned_tmp_data[key] += (1 - alpha) * value / 2
        # 两天前
        for i in range(len(tmp_tmp_data2_2)):
            row_data = [j.strip('"') for j in tmp_tmp_data2_2.iloc[i, 3].strip('[').strip(']').split(',')]
            for tmp in row_data:
                key = float(tmp.split(':')[0])
                value = float(tmp.split(':')[1])
                if key not in cleaned_tmp_data:
                    cleaned_tmp_data[key] = (1 - alpha) * value / 2
                else:
                    cleaned_tmp_data[key] += (1 - alpha) * value / 2

        # 预估
        cleaned_tmp_data_df = pd.DataFrame([[i, cleaned_tmp_data[i]] for i in list(cleaned_tmp_data.keys())],
                                           columns=['time', 'order_num'])
        X = [[i] for i in cleaned_tmp_data_df['order_num'].values]
        X = np.array(X)

        cls1 = KMeans(min(3, len(set(cleaned_tmp_data_df['order_num'].values)))).fit(X)
        cls2 = KMeans(min(4, len(set(cleaned_tmp_data_df['order_num'].values)))).fit(X)

        cleaned_tmp_data_df['flag_3_cluster'] = cls1.labels_
        cleaned_tmp_data_df['flag_4_cluster'] = cls2.labels_

        # 修正高峰期时间跨度
        if len(cleaned_tmp_data_df['flag_3_cluster'].unique()) == 3:
            cleaned_tmp_data_df = optimize_peak_period(supplier_group_id, cleaned_tmp_data_df.copy(), cluster_way='flag_3_cluster', period_limit=9)
        # cleaned_tmp_data_df = optimize_peak_period(cleaned_tmp_data_df.copy(), cluster_way='flag_4_cluster', period_limit=3)

        cleaned_tmp_data_df['rank_3_cluster'] = cleaned_tmp_data_df['flag_3_cluster'].apply(
            lambda x: get_rank_from_flag(x, cls1.cluster_centers_))
        cleaned_tmp_data_df['rank_4_cluster'] = cleaned_tmp_data_df['flag_4_cluster'].apply(
            lambda x: get_rank_from_flag(x, cls2.cluster_centers_))

        high_level_period1 = sorted(
            list(cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_3_cluster'] == '高', 'time'].values))
        medium_level_period1 = sorted(
            list(cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_3_cluster'] == '中', 'time'].values))
        low_level_period1 = sorted(
            list(cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_3_cluster'] == '低', 'time'].values))

        high_level_order_num1 = list(cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_3_cluster'] == '高', 'order_num'].values)
        medium_level_order_num1 = list(cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_3_cluster'] == '中', 'order_num'].values)
        low_level_order_num1 = list(cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_3_cluster'] == '低', 'order_num'].values)

        if len(high_level_order_num1) > 0:
            min_high_level_order_num1 = np.ceil(min(high_level_order_num1))
        else:
            min_high_level_order_num1 = -1
        if len(medium_level_order_num1) > 0:
            max_medium_level_order_num1 = np.ceil(max(medium_level_order_num1))
            min_medium_level_order_num1 = np.ceil(min(medium_level_order_num1))
        else:
            max_medium_level_order_num1 = -1
            min_medium_level_order_num1 = -1
        if len(low_level_order_num1) > 0:
            max_low_level_order_num1 = np.ceil(max(low_level_order_num1))
        else:
            max_low_level_order_num1 = -1
        if min_high_level_order_num1 != -1 and max_medium_level_order_num1 != -1:
            high_medium_boundary1 = np.ceil((min_high_level_order_num1+max_medium_level_order_num1)*0.5)
        else:
            high_medium_boundary1 = -1
        if min_medium_level_order_num1 != -1 and max_low_level_order_num1 != -1:
            medium_low_boundary1 = np.ceil((min_medium_level_order_num1+max_low_level_order_num1)*0.5)
        else:
            medium_low_boundary1 = -1

        high_level_period2 = sorted(
            list(cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_4_cluster'] == '高', 'time'].values))
        medium_level_period2 = sorted(
            list(cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_4_cluster'] == '中', 'time'].values))
        low_level_period2 = sorted(
            list(cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_4_cluster'] == '低', 'time'].values))

        high_level_order_num2 = list(
            cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_4_cluster'] == '高', 'order_num'].values)
        medium_level_order_num2 = list(
            cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_4_cluster'] == '中', 'order_num'].values)
        low_level_order_num2 = list(
            cleaned_tmp_data_df.loc[cleaned_tmp_data_df['rank_4_cluster'] == '低', 'order_num'].values)

        if len(high_level_order_num2) > 0:
            min_high_level_order_num2 = np.ceil(min(high_level_order_num2))
        else:
            min_high_level_order_num2 = -1
        if len(medium_level_order_num2) > 0:
            max_medium_level_order_num2 = np.ceil(max(medium_level_order_num2))
            min_medium_level_order_num2 = np.ceil(min(medium_level_order_num2))
        else:
            max_medium_level_order_num2 = -1
            min_medium_level_order_num2 = -1
        if len(low_level_order_num2) > 0:
            max_low_level_order_num2 = np.ceil(max(low_level_order_num2))
        else:
            max_low_level_order_num2 = -1
        if min_high_level_order_num2 != -1 and max_medium_level_order_num2 != -1:
            high_medium_boundary2 = np.ceil((min_high_level_order_num2 + max_medium_level_order_num2) * 0.5)
        else:
            high_medium_boundary2 = -1
        if min_medium_level_order_num2 != -1 and max_low_level_order_num2 != -1:
            medium_low_boundary2 = np.ceil((min_medium_level_order_num2 + max_low_level_order_num2) * 0.5)
        else:
            medium_low_boundary2 = -1

        high_level_period1 = time_standard(high_level_period1)
        medium_level_period1 = time_standard(medium_level_period1)
        low_level_period1 = time_standard(low_level_period1)

        high_level_period2 = time_standard(high_level_period2)
        medium_level_period2 = time_standard(medium_level_period2)
        low_level_period2 = time_standard(low_level_period2)

        predict_data = predict_data.append(
            {'supplier_group_id': int(supplier_group_id), 'supplier_id_list': supplier_id_list,
             'high_predict1': high_level_period1, 'medium_predict1': medium_level_period1,
             'low_predict1': low_level_period1, 'high_medium_boundary1': high_medium_boundary1,
             'medium_low_boundary1': medium_low_boundary1, 'high_predict2': high_level_period2,
             'medium_predict2': medium_level_period2, 'low_predict2': low_level_period2,
             'high_medium_boundary2': high_medium_boundary2, 'medium_low_boundary2': medium_low_boundary2
             }, ignore_index=True)
    predict_data = predict_data[predict_data['supplier_group_id'].isin(total_supplier_group)].reset_index(drop=True)

    data['hour_order_num_map'] = data['hour_order_num_map'].apply(
        lambda x: [[float(i.strip('"').split(':')[0]), float(i.strip('"').split(':')[1])] for i in
                   x.strip('[').strip(']').split(',')])
    data['hour_order_num_map'] = data['hour_order_num_map'].apply(lambda x: dict(x))
    for i in range(48):
        time = 0.5 * i
        data[str(time)] = data['hour_order_num_map'].apply(lambda x: x[time] if time in x else 0)

    origin_data = data[data['supplier_group_id'].isin(total_supplier_group)]

    origin_data = origin_data.drop(['is_supplier_group', 'hour_order_num_map', 'sort_order_hour'], axis=1)
    origin_data.sort_values(by=['supplier_group_id', 'id', 'create_dt'], ascending=[True, True, True], inplace=True)

    # 门店组订单预估
    print('************第二个for循环**************')
    supplier_group_order_predict = pd.DataFrame(columns=['supplier_group_id'] + [str(i * 0.5) for i in range(48)])
    for supplier_group_id in list(origin_data['supplier_group_id'].unique()):
        # 奈雪
        if supplier_group_id in naixue_supplier_group:
            alpha = 0.5
        # 麦当劳+奈雪
        elif supplier_group_id in naixue_maidanglao_supplier_group:
            alpha = 0.5
        # 其它
        else:
            alpha = 0.5
        group_predict_value_dict = dict()
        for i in range(48):
            time = 0.5 * i
            t1_1 = origin_data.loc[
                (origin_data['supplier_group_id'] == supplier_group_id) & (origin_data['create_dt'] == three_weeks_ago)]
            t1_2 = origin_data.loc[
                (origin_data['supplier_group_id'] == supplier_group_id) & (origin_data['create_dt'] == two_weeks_ago)]
            t1_3 = origin_data.loc[
                (origin_data['supplier_group_id'] == supplier_group_id) & (origin_data['create_dt'] == one_week_ago)]
            t2_0 = origin_data.loc[
                (origin_data['supplier_group_id'] == supplier_group_id) & (origin_data['create_dt'] == four_days_ago)]
            t2_1 = origin_data.loc[
                (origin_data['supplier_group_id'] == supplier_group_id) & (origin_data['create_dt'] == three_days_ago)]
            t2_2 = origin_data.loc[
                (origin_data['supplier_group_id'] == supplier_group_id) & (origin_data['create_dt'] == two_days_ago)]
            # 两天前、三天前数据有缺失的，用四天前的数据或者两、三天前的完整数据替代
            if len(t2_1) == 0 or len(t2_2) == 0:
                if len(t2_0) > 0:
                    if len(t2_1) == 0:
                        t2_1 = t2_0
                    if len(t2_2) == 0:
                        t2_2 = t2_0
                else:
                    if len(t2_1) > 0:
                        t2_2 = t2_1
                    if len(t2_2) > 0:
                        t2_1 = t2_2
            # 一、二、三周前数据有缺失的，用一、二、三周的完整数据部分替代
            if len(t1_1) == 0 or len(t1_2) == 0 or len(t1_3) == 0:
                if len(t1_1) + len(t1_2) + len(t1_3) > 0:
                    if len(t1_1) > 0:
                        if len(t1_2) == 0:
                            t1_2 = t1_1
                        if len(t1_3) == 0:
                            t1_3 = t1_1
                    elif len(t1_2) > 0:
                        if len(t1_1) == 0:
                            t1_1 = t1_2
                        if len(t1_3) == 0:
                            t1_3 = t1_2
                    else:
                        if len(t1_1) == 0:
                            t1_1 = t1_3
                        if len(t1_2) == 0:
                            t1_2 = t1_3
            # 如果两、三、四天前数据全部缺失或者一、二、三周前数据全部缺失，用未全部缺失的数据补充
            if len(t2_0) + len(t2_1) + len(t2_2) == 0 and len(t1_1) + len(
                    t1_2) + len(t1_3) > 0:
                if len(t1_1) + len(t1_2) + len(t1_3) == 3:
                    t2_0 = t1_1
                    t2_1 = t1_2
                    t2_2 = t1_3
                elif len(t1_1) > 0:
                    t2_0 = t1_1
                    t2_1 = t1_1
                    t2_2 = t1_1
                elif len(t1_2) > 0:
                    t2_0 = t1_2
                    t2_1 = t1_2
                    t2_2 = t1_2
                else:
                    t2_0 = t1_3
                    t2_1 = t1_3
                    t2_2 = t1_3

            if len(t2_0) + len(t2_1) + len(t2_2) > 0 and len(t1_1) + len(
                    t1_2) + len(t1_3) == 0:
                if len(t2_0) + len(t2_1) + len(t2_2) == 3:
                    t1_1 = t2_0
                    t1_2 = t2_1
                    t1_3 = t2_2
                elif len(t2_0) > 0:
                    t1_1 = t2_0
                    t1_2 = t2_0
                    t1_3 = t2_0
                elif len(t2_1) > 0:
                    t1_1 = t2_1
                    t1_2 = t2_1
                    t1_3 = t2_1
                else:
                    t1_1 = t2_2
                    t1_2 = t2_2
                    t1_3 = t2_2

            if len(t1_1) == 0 or len(t1_2) == 0 or len(t1_3) == 0 or len(t2_1) == 0 or len(t2_2) == 0:
                print('*******', supplier_group_id)
                print(len(t1_1))
                print(len(t1_2))
                print(len(t1_3))
                print(len(t2_1))
                print(len(t2_2))
                continue
            t1_1 = t1_1[str(time)].sum()
            t1_2 = t1_2[str(time)].sum()
            t1_3 = t1_3[str(time)].sum()
            t2_1 = t2_1[str(time)].sum()
            t2_2 = t2_2[str(time)].sum()
            predict_value = (t1_1 + t1_2 + t1_3) * alpha / 3 + (t2_1 + t2_2) * (1 - alpha) / 2
            group_predict_value_dict[str(time)] = int(np.ceil(predict_value))
            group_predict_value_dict['supplier_group_id'] = supplier_group_id
        supplier_group_order_predict = supplier_group_order_predict.append(group_predict_value_dict, ignore_index=True)

    # 张老板需要的高峰期配置list
    def deal_for_zhang(period_list):
        res = []
        for period in period_list:
            tmp1 = period.split('~')[0]
            tmp2 = period.split('~')[1]
            tmp1_1 = int(tmp1.split(':')[0])
            tmp1_2 = tmp1.split(':')[1]
            tmp2_1 = int(tmp2.split(':')[0])
            tmp2_2 = tmp2.split(':')[1]
            if tmp2_1 == 24:
                tmp2_1 = 23
                tmp2_2 = '59'

            res.append([str(tmp1_1)+':'+tmp1_2, str(tmp2_1)+':'+tmp2_2])
        return res


    predict_data['high_predict1'] = predict_data['high_predict1'].apply(lambda x: deal_for_zhang(x))
    predict_data['medium_predict1'] = predict_data['medium_predict1'].apply(lambda x: deal_for_zhang(x))
    predict_data['low_predict1'] = predict_data['low_predict1'].apply(lambda x: deal_for_zhang(x))
    predict_data['high_predict2'] = predict_data['high_predict2'].apply(lambda x: deal_for_zhang(x))
    predict_data['medium_predict2'] = predict_data['medium_predict2'].apply(lambda x: deal_for_zhang(x))
    predict_data['low_predict2'] = predict_data['low_predict2'].apply(lambda x: deal_for_zhang(x))

    # 施老板需要的高峰期与对应的预估单量
    whole_predict_data = pd.merge(predict_data, supplier_group_order_predict, on='supplier_group_id', how='left')

    supplier_group_order_predict = supplier_group_order_predict[
        ~supplier_group_order_predict.isnull().T.any()].reset_index(drop=True)

    # 张老板需要的预估单量dict
    print('************第三个for循环**************')
    brother_zhang_need_dict = dict()
    for supplier_group_id in supplier_group_order_predict['supplier_group_id'].unique():
        tmp_dict = dict()
        for i in range(48):
            value = supplier_group_order_predict.loc[
                supplier_group_order_predict['supplier_group_id'] == supplier_group_id, str(0.5 * i)].values[0]
            if value > 0:
                tmp_dict[i] = int(value)
        brother_zhang_need_dict.update({int(supplier_group_id): tmp_dict})

    additional_supllier_group = total_supplier_group

    for supplier_group_id in additional_supllier_group:
        res1 = brother_zhang_need_dict[supplier_group_id]
        res2_1 = predict_data.loc[predict_data['supplier_group_id'] == supplier_group_id, 'high_predict1'].values[0]
        res2_2 = predict_data.loc[predict_data['supplier_group_id'] == supplier_group_id, 'medium_predict1'].values[0]
        res3_1 = predict_data.loc[predict_data['supplier_group_id'] == supplier_group_id, 'high_predict2'].values[0]
        res3_2 = predict_data.loc[predict_data['supplier_group_id'] == supplier_group_id, 'medium_predict2'].values[0]
        print({supplier_group_id: res1})
        print('激进：')
        print('高：', res2_1)
        print('中：', res2_2)