#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd


def get_info_description(line):
    eles = line.split('description\":\"')
    description = '#'
    if len(eles) > 1:
        description_info = eles[1]
        description = description_info.split('\",')[0]
        if 'CPU利用率' in description:
            description = description.split('.')[0]
    return description


def get_info_metric(line):
    eles = line.split('metric\":\"')
    description = '#'
    if len(eles) > 1:
        description_info = eles[1]
        description = description_info.split('\",')[0]
    return description


def get_info_ruleName(line):
    eles = line.split('ruleName\":\"')
    description = '#'
    if len(eles) > 1:
        description_info = eles[1]
        description = description_info.split('\",')[0]
    return description


def get_info_summary(line):
    eles = line.split('summary\":\"')
    description = '#'
    if len(eles) > 1:
        description_info = eles[1]
        description = description_info.split(',')[0]
        if '-2' in description:
            description = description.split('-2')[0]
    return description


def get_info_user(line):
    eles = line.split('\"rd\":\"')
    description = '没有标记处理人'
    if len(eles) > 1:
        description_info = eles[1]
        description = description_info.split('\",\"')[0]
    return description


def load_file(path='data/ttt.tsv'):
    data = pd.read_csv(path, sep='\t')
    # print(data.columns.tolist())
    description = data['request_args'].map(get_info_description)
    metric = data['request_args'].map(get_info_metric)
    rule_name = data['request_args'].map(get_info_ruleName)
    user = data['request_args'].map(get_info_user)
    summary = data['request_args'].map(get_info_summary)

    print(data['request_args'][0:10])
    # print(user)
    # print(rule_name)
    # print(metric)
    # print(description)

    res_dict = {}
    count = 0
    for des, sum, met, rule, use in zip(description.tolist(), summary.tolist(), metric.tolist(), rule_name.tolist(), user.tolist()):
        res = des + '\t' + met + '\t' + rule + '\t' + use  # + '\t' + sum
        if 'uwsgi进程失联' in res:
            count += 1
    print(count)
        # res_dict[res] = res_dict.get(res, 0) + 1
    # print(len(res_dict))
    # for key, value in res_dict.items():
    #     print(key, value)
    # df = pd.DataFrame(list(res_dict.items()), columns=['des', 'count'])
    # df.to_csv('data/result.csv')


if __name__ == '__main__':
    # load_file()
    supplier_group_ids = [
        100003327,
        100002766,
        100011974,
        100011975,
        100011976,
        100011973,
        100011972,
        15739466,
        100001151,
        100001411,
        100001351,
        100011808,
        100011977,
        100011969,
        100011971,
        100008382,
        100002018,
        100008391,
        100003825,
        100003366,
        100011985,
        100011983,
        100007942,
        100002979,
        100003883,
        100002525,
        100011814,
        100011978,
        100011979,
        100001152,
        100003103,
        100011982,
        100002022,
        100002081,
        100001364,
        100001204,
        100001509,
        100001508,
        100011945,
        100011984,
        100011946,
        16267069,
        100011981,
        100011980,
        100011986,
        100012029,
        100012028,
        100012030,
        100003875,
        100012031,
        16536157,
        100003035,
        100001362,
        100012038,
        100001613,
        100002128,
        100001824,
        100002818,
        100000689,
        100001823,
        100011204,
        100008149,
        100008150,
        100003240,
        100011650,
        100000101,
        100001129,
        15876746,
        15876746,
        100001127
    ]

    supplier_ids = [
        131528979,
        131527477,
        131572846,
        131572949,
        131573046,
        131573126,
        131573198,
        131573354,
        131573531,
        130643212,
        130643653,
        131569066,
        131570483,
        131528530,
        131520803,
        131527295,
        131569951,
        131570060,
        131521291,
        129223371,
        131525995,
        131526908,
        131527868,
        129223422,
        131569245,
        131569423,
        131571135,
        131526712,
        131521090,
        130678212,
        131570172,
        131571021,
        131571641,
        130641579,
        130641436,
        130641324,
        131569687,
        131570299,
        131528217,
        131520519,
        131528086,
        130673904,
        131570742,
        131570938,
        131572791,
        130677989,
        130674185,
        130678422,
        131526236,
        130644205,
        130689159,
        130688959,
        131458509,
        131458841,
        131459034,
        130644066,
        131527091,
        131520955,
        130643062,
        131526509,
        131803107,
        130643808,
        130643934,
        131569843,
        130688880,
        130689249,
        130689738,
        130689954,
        130689552,
        130642245
    ]
    dic = {}
    for supplier_group_id, supplier_id in zip(supplier_group_ids, supplier_ids):

        dic[supplier_group_id] = {
                'jd_supplier_list': [supplier_id],
                'delay_minutes': 5,
                'limit_period_list': [
                    ['00:00:01', '23:59:59']
                ],
                'limit_period_ratio': [0.8],
                'limit_period_strategy': [1],
                'instant_order_limit_percent': 0.45,
                'different_level_config': {
                    'long_distance_threshold_list_level1': [3500, 5000],
                    'long_distance_threshold_list_level2': [3500, 4000],
                    'instance_same_way_score_threshold': [0.625, 0.625, 0.625]
                }
            }
    print(dic)

    dic = {
        100003327: {'jd_supplier_list': [131528979], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100002766: {'jd_supplier_list': [131527477], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011974: {'jd_supplier_list': [131572846], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011975: {'jd_supplier_list': [131572949], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011976: {'jd_supplier_list': [131573046], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011973: {'jd_supplier_list': [131573126], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011972: {'jd_supplier_list': [131573198], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 15739466: {'jd_supplier_list': [131573354], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001151: {'jd_supplier_list': [131573531], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001411: {'jd_supplier_list': [130643212], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001351: {'jd_supplier_list': [130643653], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011808: {'jd_supplier_list': [131569066], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011977: {'jd_supplier_list': [131570483], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011969: {'jd_supplier_list': [131528530], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011971: {'jd_supplier_list': [131520803], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100008382: {'jd_supplier_list': [131527295], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100002018: {'jd_supplier_list': [131569951], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100008391: {'jd_supplier_list': [131570060], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100003825: {'jd_supplier_list': [131521291], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100003366: {'jd_supplier_list': [129223371], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011985: {'jd_supplier_list': [131525995], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011983: {'jd_supplier_list': [131526908], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100007942: {'jd_supplier_list': [131527868], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100002979: {'jd_supplier_list': [129223422], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100003883: {'jd_supplier_list': [131569245], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100002525: {'jd_supplier_list': [131569423], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011814: {'jd_supplier_list': [131571135], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011978: {'jd_supplier_list': [131526712], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011979: {'jd_supplier_list': [131521090], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001152: {'jd_supplier_list': [130678212], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100003103: {'jd_supplier_list': [131570172], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011982: {'jd_supplier_list': [131571021], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100002022: {'jd_supplier_list': [131571641], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100002081: {'jd_supplier_list': [130641579], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001364: {'jd_supplier_list': [130641436], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001204: {'jd_supplier_list': [130641324], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001509: {'jd_supplier_list': [131569687], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001508: {'jd_supplier_list': [131570299], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011945: {'jd_supplier_list': [131528217], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011984: {'jd_supplier_list': [131520519], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011946: {'jd_supplier_list': [131528086], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 16267069: {'jd_supplier_list': [130673904], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011981: {'jd_supplier_list': [131570742], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011980: {'jd_supplier_list': [131570938], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011986: {'jd_supplier_list': [131572791], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100012029: {'jd_supplier_list': [130677989], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100012028: {'jd_supplier_list': [130674185], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100012030: {'jd_supplier_list': [130678422], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100003875: {'jd_supplier_list': [131526236], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100012031: {'jd_supplier_list': [130644205], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 16536157: {'jd_supplier_list': [130689159], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100003035: {'jd_supplier_list': [130688959], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001362: {'jd_supplier_list': [131458509], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100012038: {'jd_supplier_list': [131458841], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001613: {'jd_supplier_list': [131459034], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100002128: {'jd_supplier_list': [130644066], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001824: {'jd_supplier_list': [131527091], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100002818: {'jd_supplier_list': [131520955], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100000689: {'jd_supplier_list': [130643062], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001823: {'jd_supplier_list': [131526509], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011204: {'jd_supplier_list': [131803107], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100008149: {'jd_supplier_list': [130643808], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100008150: {'jd_supplier_list': [130643934], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100003240: {'jd_supplier_list': [131569843], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100011650: {'jd_supplier_list': [130688880], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100000101: {'jd_supplier_list': [130689249], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001129: {'jd_supplier_list': [130689738], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 15876746: {'jd_supplier_list': [130689552], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}, 100001127: {'jd_supplier_list': [130642245], 'delay_minutes': 5, 'limit_period_list': [['00:00:01', '23:59:59']], 'limit_period_ratio': [0.8], 'limit_period_strategy': [1], 'instant_order_limit_percent': 0.45, 'different_level_config': {'long_distance_threshold_list_level1': [3500, 5000], 'long_distance_threshold_list_level2': [3500, 4000], 'instance_same_way_score_threshold': [0.625, 0.625, 0.625]}}
    }





