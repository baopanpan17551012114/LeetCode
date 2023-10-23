import sys

import pandas as pd
from numpy import mean

if __name__ == '__main__':
    li = ['日期', '门店组id', '门店组名称', '发布单', '配送履约率',
          '驻店单占比', '骑士数', '驻店骑士数', '驻店全职骑士数', '驻店人效', '驻店全职人效']
    df = pd.read_excel('/Users/baopanpan/Desktop/【快送】京东前置仓数据监控-总部 (2).xlsx', sheet_name='Sheet1')[li]
    df_after = df[df['日期'] >= '2023-08-04']
    df_before = df[df['日期'] < '2023-08-04']

    # 门店组维度
    supplier_group_id_list = set(df['门店组id'].to_list())
    # for supplier_group_id in supplier_group_id_list:
    # child_li = ['发布单', '配送履约率', '驻店单占比', '骑士数', '驻店骑士数', '驻店全职骑士数', '驻店人效', '驻店全职人效']
    df_group_before = df_before.groupby('门店组id').agg(
        {'门店组名称': max, "发布单": mean, "配送履约率": mean, '驻店单占比': mean,
         '骑士数': mean, '驻店骑士数': mean, '驻店全职骑士数': mean,
         '驻店人效': mean, '驻店全职人效': mean})
    df_group_before.reset_index(level=0, inplace=True)
    df_group_before['label'] = 'before'

    df_group_after = df_after.groupby('门店组id').agg(
        {'门店组名称': max, "发布单": mean, "配送履约率": mean, '驻店单占比': mean,
         '骑士数': mean, '驻店骑士数': mean, '驻店全职骑士数': mean,
         '驻店人效': mean, '驻店全职人效': mean})
    df_group_after.reset_index(level=0, inplace=True)
    df_group_after['label'] = 'after'

    df_new = df_group_before.append(df_group_after)

    #
    df_new = df_new.sort_values(["门店组id", "label"], ascending=False)
    df_new.to_csv('/Users/baopanpan/Desktop/new1.csv')




