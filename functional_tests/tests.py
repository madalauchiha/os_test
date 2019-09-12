from selenium import webdriver
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class OSTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_case_exec_flow(self):
        # 小明输入网址localhost，进入《主页》

        # 页面上包含用例条目的选择，可以进行单个或多个用例勾选
        # 用例勾选同时支持全选和取消全选
        # 勾选好需要执行的用例后，小明点击了页面上的执行按钮
        # 在执行当前用例时，用例名后有执行中、执行成功与执行失败三个状态指示
        # 点击用例名，可以进入《执行详情页面》，可以看到系统测试的输出打印的实时更新
        # 在执行几轮测试后，小明点击主页上的历史记录，进入了《历史详情页》
        # 历史详情页中，按照时间列出了时间超链接
        # 小明点击了某个时间，看到了当时的《用例执行结果页》
        # 小明查看历史执行情况后，点击返回主页，开始新一轮测试
        self.fail('End the test')

