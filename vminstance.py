import requests
import json
import re

res = requests.get('https://g.alicdn.com/aliyun/ecs-price-info/2.0.11/price/js_price/filter_price/instanceTypePrice.js')
res.encoding = 'ASCII'
content = res.text
vm_info = content.lstrip('var instanceTypePrice = ')
jd = json.loads(vm_info)['windows']['cn-huhehaote']['ecs-3']['vpc']['true']

keys_1 = []
keys_1 = json.loads(vm_info).keys()
# print(keys_1)
for key_1 in keys_1:
    # print(key_1)
    keys_2 = []
    keys_2 = json.loads(vm_info)[key_1].keys()
    # print(keys_2)
    for key_2 in keys_2:
        keys_3 = []
        # print('.....................................................')
        keys_3 = json.loads(vm_info)[key_1][key_2].keys()
        for key_3 in keys_3:
            keys_4 = []
            if re.match(r'^ecs.', key_3) is not None:
                keys_4 = json.loads(vm_info)[key_1][key_2][key_3].keys()
                print(json.loads(vm_info)[key_1][key_2][key_3]['classic']['true'][0])



# how to get instance type_id #
# core = jd[0][4]
# instance = jd[0][0]
# memory = jd[0][5]

# print(instance, core, memory)

