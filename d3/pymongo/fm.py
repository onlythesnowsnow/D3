# -*- coding: utf-8 -*-
import pymongo
import sys
import traceback
import json

MONGODB_CONFIG = {
    'host': '10.246.53.53',
    'port': 27017,
    'db_name': 'ip_db',
    'username': None,
    'password': None
}

class MongoConn(object):

    def __init__(self):
        # connect db
        try:
            self.conn = pymongo.MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
            self.db = self.conn[MONGODB_CONFIG['db_name']]  # connect db
            self.username=MONGODB_CONFIG['username']
            self.password=MONGODB_CONFIG['password']
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True

        except Exception:
            print traceback.format_exc()
            print 'Connect Statics Database Fail.'
            sys.exit(1)

if __name__ == "__main__":
    my_conn = MongoConn()


    #print datas[0]
    #插入数据，'mytest'是上文中创建的表名
    #my_conn.db['mytest'].insert(datas)
    #查询数据，'mytest'是上文中创建的表名
    res=my_conn.db['nr6'].find({}).limit(5)
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

    '''
    category = []
    Category = []
    temp = {}
    for i in range(5):
        category.append(data[i]["nodes"][0]["category"])
        temp["name"] = data[i]["nodes"][0]["category"]
        Category.append(temp)
    print category
    print Category
    '''


