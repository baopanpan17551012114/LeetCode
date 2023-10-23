
def get_num(strvalue):
    # res_dict = {}
    # for ele in strvalue:
    #     res_dict[ele] = res_dict.get(ele, 0) + 1
    # res = ''
    # for key, value in res_dict.items():
    #     res = res + str(key) + str(value)

    res = ''
    index_left = -1
    for index, ele in enumerate(strvalue):
        if index == len(strvalue)-1:
            res = res + str(ele) + str(len(strvalue)-1 - index_left)
            break
        if strvalue[index+1] != ele:
            res = res + str(ele) + str(index-index_left)
            index_left = index
    return res

import json
def get_value(json_str, path):
    dict_val = json.loads(json_str)
    ele_list = path.split('/')
    for ele in ele_list[1:]:
        # if not isinstance(dict_val, dict):
        #     return None
        dict_val = dict_val.get(ele, None)
        if dict_val is None:
            break
    return dict_val


def str_reverse(str_value):
    value = str_value[::-1]
    if value[0] == '0':
        value = value[1:]
    if '-' in value:
        return '-'+value[:-1]
    return value


if __name__ == '__main__':
    # res = get_value(json.dumps(
    #     {'model':{
    #         'item1': 123,
    #         'item2': {'ii':11}
    #     }}
    # ), path='/model/item2/ii')

    res = get_num('AABBCCCD')
    print(res)



