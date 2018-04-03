#encoding: utf-8

from flask import *
import sys
import json
import pymongo
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():

    result_list = []
    client = pymongo.MongoClient(host="10.246.53.53", port=27017)
    db = client['ip_db']
    # 在此处更改为你自己的网站名称！
    collection = db['nr6']
    keep_collection  = db['nr6']

    # 区分不同文档（无用？）
    dict_count = 0

    big_title = "无标题"

    name_set = set()
    name_list = []

    # 设定要读取的文档数量！！！！！
    read_count = 1

    for document in collection.find({}).limit(15):
        # 默认无标题

        for node in document["nodes"]:
            name_set.add(node["name"])
            name_list.append(node['name'])

        read_count -= 1
        if read_count == 0:
            break
        dict_count += 1
        # "已经到了 "+str(dict_count)+" 个文件"

    t = 0
    for document in keep_collection.find():
        new_dict = {}
        node_list = []
        for node in document["nodes"]:
            if node["name"] in name_set:
                count = name_list.count(node["name"])
                if count > 1:
                    node["category"] = "公共"
                node_list.append(node)
                name_set.remove(node["name"])

        new_dict["nodes"] = node_list
        new_dict["relations"] = document["relations"]
        result_list.append(new_dict)
        t+=1

    data = result_list
    nodes = []
    links = []

    for i in data:
        nodes.extend(i["nodes"])
        links.extend(i["relations"])

    for index, node in enumerate(nodes):
        nodes[index]["symbolSize"] *= 2

    data1 = json.dumps(nodes)
    data2 = json.dumps(links)

    category = []
    Category = []


    for i in range(15):
        for j in range(len(data[i]["nodes"])):
            if data[i]["nodes"][j]["category"]!= "公共":
                temp = {}
                category.append(data[i]["nodes"][j]["category"])
                temp["name"] = data[i]["nodes"][j]["category"]
                Category.append(temp)


    data3 = json.dumps(category)
    data4 = json.dumps(Category)

    return render_template('graph.html',data1 = data1,data2 = data2,data3 = data3,data4 = data4)

if __name__ == '__main__':
    app.run(host='127.0.0.1')

