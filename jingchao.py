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
    column_list = ['日期', 's_name', '门店组id', '分发模式', '全职算法派单占比']
    df = pd.read_excel(file_name, sheet_name='2-by门店组维度近30天（附件）')[column_list]
    df = df[df['日期'] >= '2023-10-15'].drop_duplicates(ignore_index=True)
    result_dict = {}
    id_name_dict = {}
    for supplier_group_id, algo_per, supplier_group_name in zip(
            df['门店组id'].to_list(), df['全职算法派单占比'].to_list(), df['s_name'].to_list()):
        if supplier_group_id in supplier_group_list:
            id_name_dict[supplier_group_id] = supplier_group_name
            value = 0
            if isinstance(algo_per, str):
                value = round(float(algo_per.split('%')[0])/100, 3)
            result_dict[supplier_group_id] = max(value, result_dict.get(supplier_group_id, 0))
    print(result_dict)
    result_list = []

    for k, v in result_dict.items():
        result_list.append({'supplier_group_id': k, 'algo_per': v,
                            'supplier_group_name': id_name_dict.get(k)})
    res_df = pd.DataFrame(result_list)
    print(res_df)
    res_df.to_csv('/Users/baopanpan3/Desktop/jingchao.csv')


if __name__ == '__main__':
    # load_file()
    df = pd.read_csv('/Users/baopanpan3/Desktop/jingchao.csv')
    df = df[df['algo_per'] >= 0.1]
    res_list = [100011656, 100013607, 100013637, 100013024, 100013687, 100013688, 100014081, 100013903, 100013902,
                100014587, 100015674, 100015250, 100015363, 100015248, 100016016]
    jingchao_list = df['supplier_group_id'].to_list()
    res_list.extend(jingchao_list)
    print(res_list)
    # result_dict = {}
    # for sup in res_list:
    #     result_dict[sup] = 300
    # print(result_dict)