#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file = '【京超】京超门店监测报表.xlsx'
import sys
import time

import pandas as pd

def time_jiaoji(start1, end1, start2, end2):
    if start2 < start1 < end2 or start1 < start2 < end1:
        return True
    else:
        return False


def to_dict(li):
    return {
        'transporter_id': li[0],
        'station_road': li[1],
        'start_time': li[2],
        'end_time': li[3],
        'index': li[4],
        'order_ids': li[5]
    }


def get_not_assign_same_transporter(origin_path):
    df = pd.read_excel(origin_path, sheet_name='list')
    df_groups = df.groupby(['supplier_id'])
    columns = ['transporter_id', 'manual_group_id', 'station_road', 'start_time', 'end_time']
    res = []
    index = 0
    for supplier_id, child_supplier_group in df_groups:
        transporter_ids = df['transporter_id'].to_list()
        station_roads = df['station_road'].to_list()
        start_times = df['start_time'].to_list()
        end_times = df['end_time'].to_list()
        order_ids = df['order_id_list'].to_list()
        for i in range(len(transporter_ids)):
            transporter_id, station_road, start_time, end_time, order_id = transporter_ids[i], station_roads[i], \
                                                                           start_times[i], \
                                                                           end_times[i], order_ids[i]
            start_stamp = int(time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S')))
            end_stamp = int(time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M:%S')))
            if end_stamp - start_stamp > 45 * 60:
                continue

            # base, 被匹配的
            index += 1
            child_list = [[transporter_id, station_road, start_time, end_time, index, order_id]]

            for j in range(i + 1, len(transporter_ids)):
                transporter_id1, station_road1, start_time1, end_time1, order_id1 = transporter_ids[j], station_roads[
                    j], \
                                                                                    start_times[j], end_times[j], \
                                                                                    order_ids[j]
                start_stamp = int(time.mktime(time.strptime(start_time1, '%Y-%m-%d %H:%M:%S')))
                end_stamp = int(time.mktime(time.strptime(end_time1, '%Y-%m-%d %H:%M:%S')))
                if end_stamp - start_stamp > 45 * 60:
                    continue
                if transporter_id == transporter_id1:
                    continue
                if station_road != station_road1:
                    continue
                jiaoji = time_jiaoji(start_time, end_time, start_time1, end_time1)
                if jiaoji:
                    child_list.append([transporter_id1, station_road1, start_time1, end_time1, index, order_id1])
                    # res.append(to_dict([transporter_id, station_road, start_time, end_time, index]))
                    # res.append(to_dict([transporter_id1, station_road1, start_time1, end_time1, index]))
            if len(child_list) <= 1:
                continue
            for ele_list in child_list:
                res.append(to_dict(ele_list))
    df_res = pd.DataFrame(res)
    return df_res
    # df_res.to_csv('/Users/baopanpan/Desktop/30前置仓同一路区订单未派同一骑士数据result.csv')


def get_filter_step(filter_path, origin_path):
    df = pd.read_csv(filter_path)
    res_dict = {}
    for order_id, transporter_id, filter_step in zip(df['order_id'].to_list(), df['transporter_id'].to_list(),
                                                     df['filter_step'].to_list(),):
        key = str(order_id) + '#' + str(transporter_id)
        res_dict[key] = filter_step
    del df

    filter_df = get_not_assign_same_transporter(origin_path)
    key_set = set()
    for index, child_df in filter_df.groupby(['index']):
        line = child_df[child_df['start_time'] == min(child_df['start_time'].to_list())]
        transporter_id = line.iloc[0]['transporter_id']
        other_lines = child_df[child_df['start_time'] != min(child_df['start_time'].to_list())]
        for i in range(len(other_lines)):
            line = other_lines.iloc[i]
            order_id_list = line['order_ids'].split('###')
            for order_id in order_id_list:
                key = str(order_id) + '#' + str(transporter_id)
                key_set.add(key)
    print(len(key_set))
    total_res_dict = {}
    for ele in key_set:
        filter_tmp = res_dict.get(ele, None)
        total_res_dict[filter_tmp] = total_res_dict.get(filter_tmp, 0) + 1
    print(total_res_dict)

    # 额外信息
    extra_list = []
    for ele in key_set:
        filter_tmp = res_dict.get(ele, None)
        if filter_tmp == 'filter_queue_transporter_inshop_assign':
            extra_list.append(ele)
    print(extra_list)


if __name__ == '__main__':
    get_not_assign_same_transporter()
    filter_path = '/Users/baopanpan/Desktop/31未派过滤原因.csv'
    origin_path = '/Users/baopanpan/Desktop/31未派数据.xlsx'
    get_filter_step(filter_path, origin_path)

