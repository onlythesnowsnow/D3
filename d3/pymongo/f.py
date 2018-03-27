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
    res = my_conn.db['nr6'].find({}).limit(5)
    data = []
    nodes = []
    links = []

    for i in range(5):
        for k in res:
            data.append(k)

    #for i in data:
        #nodes.extend(i["nodes"])
        #links.extend(i["relations"])

    nodes = data[1]["nodes"]
    links = data[1]["relations"]

    data1 = json.dumps(nodes)
    data2 = json.dumps(links)


    category = []
    Category = []
    for i in range(5):
        temp = {}
        category.append(data[i]["nodes"][0]["category"])
        temp["name"] = data[i]["nodes"][0]["category"]
        Category.append(temp)

    data3 = json.dumps(category)
    data4 = json.dumps(Category)

    return render_template('graph.html',data1 = data1,data2 = data2,data3 = data3,data4 = data4)

if __name__ == '__main__':
    app.run(host='127.0.0.1')

