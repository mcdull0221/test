import json

# Python 字典类型转换为 JSON 对象
# json.dumps     仅转成字符串
# json.dump      转成字符串并写入文件
# json.loads     只将字符串转成相应类型
# json.load      从文件中加载字符并转成相应类型

data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}
# 序列化
json_str = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)

# 将数据写入文件
with open("test.json", "w") as f:
    json.dump(data1, f)


# 将 JSON 对象转换为 Python 字典  反序列化
data2 = json.loads(json_str)
print(data2)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])
