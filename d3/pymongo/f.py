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
    context = [
        {'_id':'打飞机可', 'data':12},
        {'_id':'的九分裤', 'data':22},
        {'_id':3, 'data':'cc'}
    ]
    data = [{
              "name": u"广州大学",
               "x": 0,
               "y": 0,
              "symbolSize": 20,
              "draggable": u"true",
              "value": 27

          }, {
              "name": u"计算机科学与教育软件学院",
              "value": 3,
              "symbolSize": 9,
              "category": u"计算机科学与教育软件学院",
              "draggable": u"true"
          }, {
              "name": "计算机科学与技术",
              "symbolSize": 3,
              "category": "计算机科学与教育软件学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "软件工程",
              "symbolSize": 3,
              "category": "计算机科学与教育软件学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "网络工程",
              "symbolSize": 3,
              "category": "计算机科学与教育软件学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "地理科学学院",
              "value": 6,
              "symbolSize": 18,
              "category": "地理科学学院",
              "draggable": "true"
          }, {
              "name": "地理科学",
              "symbolSize": 3,
              "category": "地理科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "地理信息科学",
              "symbolSize": 3,
              "category": "地理科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "人文地理与城乡规划",
              "symbolSize": 3,
              "category": "地理科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "人文地理与城乡规划(区域物流)",
              "symbolSize": 3,
              "category": "地理科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "人文地理与城乡规划(不动产)",
              "symbolSize": 3,
              "category": "地理科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "自然地理与资源环境",
              "symbolSize": 3,
              "category": "地理科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "机械与电气工程学院",
              "value": 5,
              "symbolSize": 15,
              "category": "机械与电气工程学院",
              "draggable": "true"
          }, {
              "name": "电气工程及其自动化",
              "symbolSize": 3,
              "category": "机械与电气工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "机械设计制造及其自动化",
              "symbolSize": 3,
              "category": "机械与电气工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "电子信息工程",
              "symbolSize": 3,
              "category": "机械与电气工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "工业设计",
              "symbolSize": 3,
              "category": "机械与电气工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "通信工程",
              "symbolSize": 3,
              "category": "机械与电气工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "经济与统计学院",
              "value": 6,
              "symbolSize": 18,
              "category": "经济与统计学院",
              "draggable": "true"
          }, {
              "name": "统计学",
              "symbolSize": 3,
              "category": "经济与统计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "金融工程",
              "symbolSize": 3,
              "category": "经济与统计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "经济学",
              "symbolSize": 3,
              "category": "经济与统计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "国际经济与贸易",
              "symbolSize": 3,
              "category": "经济与统计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "金融学",
              "symbolSize": 3,
              "category": "经济与统计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "会计学",
              "symbolSize": 3,
              "category": "经济与统计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "土木工程学院",
              "value": 8,
              "symbolSize": 24,
              "category": "土木工程学院",
              "draggable": "true"
          }, {
              "name": "给排水科学与工程",
              "symbolSize": 3,
              "category": "土木工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "土木工程(道路与桥梁工程)",
              "symbolSize": 3,
              "category": "土木工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "土木工程(建筑工程)",
              "symbolSize": 3,
              "category": "土木工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "土木工程(综合试点)",
              "symbolSize": 3,
              "category": "土木工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "土木工程(结构分析)",
              "symbolSize": 3,
              "category": "土木工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "土木工程(地下建筑工程)",
              "symbolSize": 3,
              "category": "土木工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "交通工程",
              "symbolSize": 3,
              "category": "土木工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "建筑环境与能源应用工程",
              "symbolSize": 3,
              "category": "土木工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "新闻与传播学院",
              "value": 5,
              "symbolSize": 15,
              "category": "新闻与传播学院",
              "draggable": "true"
          }, {
              "name": "广告学",
              "symbolSize": 3,
              "category": "新闻与传播学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "广播电视学",
              "symbolSize": 3,
              "category": "新闻与传播学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "网络与新媒体",
              "symbolSize": 3,
              "category": "新闻与传播学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "播音与主持艺术",
              "symbolSize": 3,
              "category": "新闻与传播学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "广播电视编导",
              "symbolSize": 3,
              "category": "新闻与传播学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "外国语学院",
              "value": 6,
              "symbolSize": 18,
              "category": "外国语学院",
              "draggable": "true"
          }, {
              "name": "英语(翻译)",
              "symbolSize": 3,
              "category": "外国语学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "英语(教师教育)",
              "symbolSize": 3,
              "category": "外国语学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "英语(国际商务)",
              "symbolSize": 3,
              "category": "外国语学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "日语",
              "symbolSize": 3,
              "category": "外国语学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "英语",
              "symbolSize": 3,
              "category": "外国语学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "法语",
              "symbolSize": 3,
              "category": "外国语学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "人文学院",
              "value": 10,
              "symbolSize": 30,
              "category": "人文学院",
              "draggable": "true"
          }, {
              "name": "汉语言文学",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "历史学",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "汉语国际教育",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "汉语言文学(戏剧与影视学)",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "汉语言文学(文学)",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "汉语言文学(秘书学)",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "汉语言文学(应用语言学)",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "汉语言文学(教师教育)",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "历史学(教师教育)",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "历史学(文化资源开发与利用)",
              "symbolSize": 3,
              "category": "人文学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "数学与信息科学学院",
              "value": 6,
              "symbolSize": 18,
              "category": "数学与信息科学学院",
              "draggable": "true"
          }, {
              "name": "信息安全",
              "symbolSize": 3,
              "category": "数学与信息科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "数学与应用数学(金融数学)",
              "symbolSize": 3,
              "category": "数学与信息科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "信息与计算科学",
              "symbolSize": 3,
              "category": "数学与信息科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "数学与应用数学(教师教育)",
              "symbolSize": 3,
              "category": "数学与信息科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "数学与应用数学(精算学)",
              "symbolSize": 3,
              "category": "数学与信息科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "数学与应用数学(基础数学)",
              "symbolSize": 3,
              "category": "数学与信息科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "工商管理学院",
              "value": 6,
              "symbolSize": 18,
              "category": "工商管理学院",
              "draggable": "true"
          }, {
              "name": "工程管理",
              "symbolSize": 3,
              "category": "工商管理学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "物流管理",
              "symbolSize": 3,
              "category": "工商管理学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "工商管理",
              "symbolSize": 3,
              "category": "工商管理学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "电子商务",
              "symbolSize": 3,
              "category": "工商管理学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "市场营销",
              "symbolSize": 3,
              "category": "工商管理学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "人力资源管理",
              "symbolSize": 3,
              "category": "工商管理学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "法学院",
              "value": 2,
              "symbolSize": 6,
              "category": "法学院",
              "draggable": "true"
          }, {
              "name": "法学",
              "symbolSize": 3,
              "category": "法学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "法学（律师）",
              "symbolSize": 3,
              "category": "法学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "公共管理学院",
              "value": 3,
              "symbolSize": 9,
              "category": "公共管理学院",
              "draggable": "true"
          }, {
              "name": "社会工作",
              "symbolSize": 3,
              "category": "公共管理学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "行政管理",
              "symbolSize": 3,
              "category": "公共管理学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "公共事业管理",
              "symbolSize": 3,
              "category": "公共管理学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "卫斯理安学院",
              "value": 2,
              "symbolSize": 6,
              "category": "卫斯理安学院",
              "draggable": "true"
          }, {
              "name": "经济学(卫斯理安)",
              "symbolSize": 3,
              "category": "卫斯理安学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "工商管理(卫斯理安)",
              "symbolSize": 3,
              "category": "卫斯理安学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "政治与公民教育学院",
              "value": 1,
              "symbolSize": 3,
              "category": "政治与公民教育学院",
              "draggable": "true"
          }, {
              "name": "思想政治教育",
              "symbolSize": 3,
              "category": "政治与公民教育学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "旅游学院",
              "value": 4,
              "symbolSize": 12,
              "category": "旅游学院",
              "draggable": "true"
          }, {
              "name": "会展经济与管理",
              "symbolSize": 3,
              "category": "旅游学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "旅游管理(旅游企业管理)",
              "symbolSize": 3,
              "category": "旅游学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "旅游管理(酒店管理)",
              "symbolSize": 3,
              "category": "旅游学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "旅游管理[中法]",
              "symbolSize": 3,
              "category": "旅游学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "教育学院",
              "value": 6,
              "symbolSize": 18,
              "category": "教育学院",
              "draggable": "true"
          }, {
              "name": "心理学",
              "symbolSize": 3,
              "category": "教育学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "心理学（特殊儿童心理发展与教育）",
              "symbolSize": 3,
              "category": "教育学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "应用心理学",
              "symbolSize": 3,
              "category": "教育学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "教育技术学",
              "symbolSize": 3,
              "category": "教育学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "学前教育",
              "symbolSize": 3,
              "category": "教育学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "小学教育",
              "symbolSize": 3,
              "category": "教育学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "环境科学与工程学院",
              "value": 2,
              "symbolSize": 6,
              "category": "环境科学与工程学院",
              "draggable": "true"
          }, {
              "name": "环境工程",
              "symbolSize": 3,
              "category": "环境科学与工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "环境科学",
              "symbolSize": 3,
              "category": "环境科学与工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "化学化工学院",
              "value": 5,
              "symbolSize": 15,
              "category": "化学化工学院",
              "draggable": "true"
          }, {
              "name": "化学工程与工艺",
              "symbolSize": 3,
              "category": "化学化工学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "化学(教师教育)",
              "symbolSize": 3,
              "category": "化学化工学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "化学(精细化学品化学与技术)",
              "symbolSize": 3,
              "category": "化学化工学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "化学",
              "symbolSize": 3,
              "category": "化学化工学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "食品科学与工程",
              "symbolSize": 3,
              "category": "化学化工学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "物理与电子工程学院",
              "value": 4,
              "symbolSize": 12,
              "category": "物理与电子工程学院",
              "draggable": "true"
          }, {
              "name": "光电信息科学与工程",
              "symbolSize": 3,
              "category": "物理与电子工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "物联网工程",
              "symbolSize": 3,
              "category": "物理与电子工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "物理学",
              "symbolSize": 3,
              "category": "物理与电子工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "电子信息科学与技术",
              "symbolSize": 3,
              "category": "物理与电子工程学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "建筑与城市规划学院",
              "value": 4,
              "symbolSize": 12,
              "category": "建筑与城市规划学院",
              "draggable": "true"
          }, {
              "name": "建筑学",
              "symbolSize": 3,
              "category": "建筑与城市规划学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "城乡规划",
              "symbolSize": 3,
              "category": "建筑与城市规划学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "风景园林",
              "symbolSize": 3,
              "category": "建筑与城市规划学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "建筑学（五年制）",
              "symbolSize": 3,
              "category": "建筑与城市规划学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "美术与设计学院",
              "value": 9,
              "symbolSize": 27,
              "category": "美术与设计学院",
              "draggable": "true"
          }, {
              "name": "美术学",
              "symbolSize": 3,
              "category": "美术与设计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "美术学(教师教育)",
              "symbolSize": 3,
              "category": "美术与设计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "动画",
              "symbolSize": 3,
              "category": "美术与设计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "动画(游戏动画)",
              "symbolSize": 3,
              "category": "美术与设计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "绘画",
              "symbolSize": 3,
              "category": "美术与设计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "动画(动画音乐与合成)",
              "symbolSize": 3,
              "category": "美术与设计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "产品设计",
              "symbolSize": 3,
              "category": "美术与设计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "服装与服饰设计(服装设计)",
              "symbolSize": 3,
              "category": "美术与设计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "视觉传达设计",
              "symbolSize": 3,
              "category": "美术与设计学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "生命科学学院",
              "value": 3,
              "symbolSize": 9,
              "category": "生命科学学院",
              "draggable": "true"
          }, {
              "name": "生物科学",
              "symbolSize": 3,
              "category": "生命科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "生物工程",
              "symbolSize": 3,
              "category": "生命科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "生物技术",
              "symbolSize": 3,
              "category": "生命科学学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "体育学院",
              "value": 2,
              "symbolSize": 6,
              "category": "体育学院",
              "draggable": "true"
          }, {
              "name": "体育教育",
              "symbolSize": 3,
              "category": "体育学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "社会体育指导与管理",
              "symbolSize": 3,
              "category": "体育学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "音乐舞蹈学院",
              "value": 3,
              "symbolSize": 9,
              "category": "音乐舞蹈学院",
              "draggable": "true"
          }, {
              "name": "音乐学",
              "symbolSize": 3,
              "category": "音乐舞蹈学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "舞蹈编导(编导)",
              "symbolSize": 3,
              "category": "音乐舞蹈学院",
              "draggable": "true",
              "value": 1
          }, {
              "name": "舞蹈编导(教师教育)",
              "symbolSize": 3,
              "category": "音乐舞蹈学院",
              "draggable": "true",
              "value": 1
          }]
    data = json.dumps(data)
    #my_conn = MongoConn()
    #json.dumps(data)
    #res=my_conn.db['mytest'].find({})
    return render_template('graph.html',data = data )

if __name__ == '__main__':
    app.run(host='127.0.0.1')

# <div id="dataid" d="{{data}}" style="display:none"></div>
# var js_data = document.getElementById('dataid').getAttribute('d'); 可用于js参数传递