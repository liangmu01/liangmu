# -*- coding:utf-8 -*-
import requests
import unittest
import json
import datetime
from datetime import datetime
class ApiTest(unittest.TestCase):
    #创建活动url
    def setUp(self):
        self.url = "http://47.92.88.246:8001/api/add_activity/"
        self.now_time = datetime.now().strftime('%Y%m%d%H%M%S')
        self.search_url = "http://47.92.88.246:8001/api/search_activity/"
        self.del_url = "http://47.92.88.246:8001/api/del_activity/"

    # def test_add_activity01(self):
    #     self.request_data = {"activity_name": '天猫双14', "activity_desc": "几个人周末一起玩", "activity_project": "篮球",
    #                          "start_time": "20171902", "end_time": "2018982"}
    #     self.request_data["activity_name"] = "li" + str(self.now_time)
    #     response_obj = requests.post(self.url,json.dumps(self.request_data))
    #     res = json.loads(response_obj.text)
    #     self.assertEqual(res['status'],0)
    #     print self.request_data["activity_name"]
    #
    # #查询活动
    # def test_search_activity(self):
    #     # self.add_url = "http://127.0.0.1:8000/api/search_activity/"
    #     request_data = {"activity_name": '天猫双14'}
    #     result=requests.post(self.search_url,json.dump(request_data))
    #     res=json.loads(result)
    #     self.assertEqual(res['status'],0)

    #删除活动
    def test_del_activity(self):
        #第一步创建活动
        status=self.add_activity(u'天猫双192')
        self.assertEqual(status,0)
        #查询这个活动
        data=self.search_activity(u'天猫双192')
        #从返回结果中获取id
        id=data['id']
        #删除这个活动
        status=self.del_acitivity(id)
        #验证活动是否删除
        self.assertEquals(status,0)
    #添加活动
    def add_activity(self,activity_name):
        self.request_data = {"activity_name": '天猫双18', "activity_desc": "几个人周末一起玩", "activity_project": "篮球",
                        "start_time": "20171902", "end_time": "2018982"}
        self.request_data['activity_name']=activity_name
        response_obj = requests.post(self.url,json.dumps(self.request_data))
        res = json.loads(response_obj.text)
        return res['status']
    #查询活动
    def search_activity(self,name):
        self.request_data={'activity_name':name}
        result=requests.post(self.search_url,json.dumps(self.request_data))
        res=json.loads(result.text)
        return res['data'][0]
    #删除活动
    def del_acitivity(self, id):
        request_data = {'id': id}
        result = requests.post(self.del_url,json.dumps(request_data))
        res = json.loads(result.text)
        return res['status']

if __name__ == "__main__":
        unittest.main()