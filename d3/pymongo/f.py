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

'''
#去掉Objectid
def change(args):
    Data = []
    for k in args:
        Data.append(k)
    for i in Data:
        del i['_id']
    Data = json.dumps(Data)
    return Data
'''

@app.route('/')
def index():

    my_conn = MongoConn()
    data1 = my_conn.db['nr2'].find({})
    data = []
    nodes = []
    links = []
    for k in data1:
        data.append(k)
    for i in data:
        nodes.extend(i["nodes"])
        links.extend(i["relations"])

    data1 = json.dumps(nodes)
    data2 = json.dumps(links)

    return render_template('graph.html',data1 = data1,data2 = data2 )

if __name__ == '__main__':
    app.run(host='127.0.0.1')

# <div id="dataid" d="{{data}}" style="display:none"></div>
# var js_data = document.getElementById('dataid').getAttribute('d'); 可用于js参数传递