#encoding: utf-8

from flask import *
from fm import MongoConn
import sys
import json
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():

    my_conn = MongoConn()
    res = my_conn.db['product_type_and_name'].find({})
    data = []
    nodes = []
    links = []

    for k in res:
        data.append(k)

    for i in data:
        nodes.extend(i["nodes"])
        links.extend(i["relations"])

    for index, node in enumerate(nodes):
        nodes[index]["symbolSize"] *= 2

    data1 = json.dumps(nodes)
    data2 = json.dumps(links)


    category = []
    Category = []

    for i in range(len(data[0]["nodes"])):
        temp = {}
        category.append(data[0]["nodes"][i]["category"])
        temp["name"] = data[0]["nodes"][i]["category"]
        Category.append(temp)

    data3 = json.dumps(category)
    data4 = json.dumps(Category)

    return render_template('graph2.html',data1 = data1,data2 = data2,data3 = data3,data4 = data4)

if __name__ == '__main__':
    app.run(host='127.0.0.1')

