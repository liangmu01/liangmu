class ApiTest(unittest.TestCase):
    #创建活动url
    def setUp(self):
        self.url = "http://47.92.88.246:8001/api/add_activity/"
        self.now_time = datetime.now().strftime('%Y%m%d%H%M%S')


    #activity_name添加正常数据
    # def test_add_activity01(self):
    #     self.request_data = {"activity_name": '添加活动'+self.now_time, "activity_desc": "几个人周末一起玩", "activity_project": "篮球",
    #                 "start_time": "20171902", "end_time": "2018982"}
    #     response_obj = requests.post(self.url,json.dumps(self.request_data))
    #     res = json.loads(response_obj.text)
    #     self.assertEqual(res['status'],0)
    #     print self.request_data["activity_name"]

    print time.time()
    print int(round((time.time()*1000)))
    self.assertEqual(res['status'],4)
