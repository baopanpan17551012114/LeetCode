#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd

file_name = '/Users/baopanpan3/Desktop/【京超】京超门店监测报表 (1).xlsx'


def load_file():
    column_list = ['日期', '门店组id', '门店组模式', '分发模式']
    df = pd.read_excel(file_name, sheet_name='3-by门店组骑士维度近30天（附件）')[column_list]
    df = df[df['日期'] >= '2023-10-15']
    df = df[df['门店组模式'] == '单实体门店'].drop_duplicates(subset=['门店组id'], ignore_index=True)

    # 所有京超单店门店组
    supplier_group_list = df['门店组id'].to_list()
    print(supplier_group_list)

    # 统计京超门店组中派单占比较低的  2-by门店组维度近30天（附件）
    column_list = ['日期', 's_name', '门店组id', '分发模式', '全职算法派单占比', '发布单']
    df = pd.read_excel(file_name, sheet_name='2-by门店组维度近30天（附件）')[column_list]
    df = df[df['日期'] >= '2023-10-15'].drop_duplicates(ignore_index=True)
    result_dict = {}
    id_name_dict = {}
    id_number_dict = {}
    for supplier_group_id, algo_per, supplier_group_name, order_num in zip(
            df['门店组id'].to_list(), df['全职算法派单占比'].to_list(), df['s_name'].to_list(), df['发布单'].to_list()):
        if supplier_group_id in supplier_group_list:
            id_name_dict[supplier_group_id] = supplier_group_name
            id_number_dict[supplier_group_id] = order_num
            value = 0
            if isinstance(algo_per, str):
                value = round(float(algo_per.split('%')[0])/100, 3)
            result_dict[supplier_group_id] = max(value, result_dict.get(supplier_group_id, 0))
    print(result_dict)
    result_list = []

    for k, v in result_dict.items():
        result_list.append({'supplier_group_id': k, 'algo_per': v,
                            'supplier_group_name': id_name_dict.get(k),
                            'order_num': id_number_dict.get(k)
                            })
    res_df = pd.DataFrame(result_list)
    print(res_df)
    res_df.to_csv('/Users/baopanpan3/Desktop/jingchao.csv')


if __name__ == '__main__':
    load_file()
    # df = pd.read_excel('/Users/baopanpan3/Downloads/mart_tc_bi_dw_124912996.xlsx', sheet_name='list')[['receiver_lat', 'receiver_lng']]
    # li = []
    # for lat, lng in zip(df['receiver_lat'].to_list(), df['receiver_lng'].to_list()):
    #     li.append(lat)
    #     li.append(lng)
    # print(li)
    # # result_dict = {}
    # # for sup in res_list:
    # #     result_dict[sup] = 300
    # # print(result_dict)