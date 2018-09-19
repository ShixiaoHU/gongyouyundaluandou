#!/usr/bin/python
import requests
import json
import pymysql

#dbconnection
res = requests.get('https://g.alicdn.com/aliyun/ecs-price-info/2.0.11/price/download/instancePrice.json?spm=0.6883001.\
instance.1.455e7Xk27Xk2bz&file=instancePrice.json')
res.encoding = 'utf-8'
content = res.text
jd = json.loads(content)
priceInfo = jd['pricingInfo']
product = priceInfo.keys()
for keys, values in priceInfo.items():
    place = keys.split('::', 4)[0]
    product_id = keys.split('::', 4)[1]
    operation_sys = keys.split('::', 4)[3]
    price_hours = values['hours'][0]['price']
    price_weeks = values['weeks'][0]['price']
    price_months = values['months'][0]['price']
    price_years_p1 = values['years'][0]['price']
    price_years_p2 = values['years'][1]['price']
    price_years_p3 = values['years'][2]['price']
    price_years_p4 = values['years'][3]['price']
    price_years_p5 = values['years'][4]['price']
    results = [product_id, place, operation_sys, price_hours, price_weeks, price_months, price_years_p1, price_years_p2, price_years_p3, price_years_p4, price_years_p5]
    cursor = db.cursor()
    # sql = "INSERT INTO t_price_vm(id, type_id, region, operation_sys, price_h, price_w, price_m, price_y_p1, price_y_p2, price_y_p3, price_y_p4, price_y_p5) VALUE (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # print(sql)
sql = "select DISTINCT type_id from t_price_vm WHERE type_id NOT REGEXP '^ecs.g5';"
#g5 = "select DISTINCT type_id from t_price_vm WHERE type_id <> REGEXP '^ecs.g5'"

cursor.execute(sql)
list_vm = cursor.fetchall()
    # db.commit()
#cursor.execute(g5)
#list_g5 = cursor.fetchall()

lists_type = list(list_vm)
listtype = []
i = 47
for l in lists_type:
    listtype.extend(l)
    lt = str(l).rsplit('.', 1)[0].lstrip("('")
    type1 = 'AliCloud_' + lt
    print(type(type1))
    # vm = [i, 5, type1, l]
    l = str(l).lstrip("('").rstrip("',)")
    # print(l)
    print(type(type1))
    insert_vm = "INSERT INTO t_prod_virtualmachine(id, common, type, type_id) VALUE (%d, %d, '%s', '%s')" % (i, 5, type1, l)
    print(insert_vm)
    cursor.execute(insert_vm)
    db.commit()
    i = i + 1
    print(i)


# insert_vm = "INSERT INTO t_prod_virtualmachine(id, common, type, type_id) VALUE （%d, 5, %s, %s）"
# type_vm = list(list_vm)
# print(list_type_vm)
# print(type(type_vm))
# print(".........")
# print(list_vm)
db.close()
# insert_vm = "INSERT INTO t_prod_virtualmachine(id, common, type, type_id) VALUE （NULL, 5, %s, %s）"

