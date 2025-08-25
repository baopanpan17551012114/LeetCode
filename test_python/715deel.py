# -*- coding: utf-8 -*-
import pandas as pd
import json

data_path = '/users/baopanpan3/downloads/715_data_before_deel.csv'
log_data = pd.read_csv(data_path, nrows=10000000, encoding='gb18030')

ka_order_id_list = []
for i, row in log_data.iterrows():
    order_ids = json.loads(row['order_id_list'])
    order_labels = json.loads(row['order_label_list'])
    if 49 not in order_labels and 1425 in order_labels and 344 in order_labels:
        ka_order_id_list.extend(order_ids)
ka_order_ids = list(set(ka_order_id_list))
print("KA限流单量", len(ka_order_ids))
print("KA限流单号")
print(ka_order_ids)

res = "杨树浦路1088号东方渔人码头B区商业1楼102-3室（靠山鹰国际江边花园）".encode('utf-8')
print(res)
