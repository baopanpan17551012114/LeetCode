
import pandas as pd


if __name__ == '__main__':
    df = pd.read_excel('Z_op/data/京超直营单店门店组.xlsx')[['shop_id']]
    supplier_group_ids = df['shop_id'].to_list()

    print(supplier_group_ids)

