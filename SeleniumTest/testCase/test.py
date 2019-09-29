# coding=utf-8
from selenium import webdriver
import unittest
import time
from report import HTMLTestRunner
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import logging

class TestForum(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://47.104.84.186:8080/")
        self.driver.maximize_window()
        time.sleep(5)

    def tearDown(self):
        print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        filedir = '../screenShot/'
        if not os.path.exists(filedir):
            os.makedirs(os.path.join(filedir))

        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

        # 发布帖子，输入标题 ，输入内容，选择标签，点击发布

    def testReleasePost_04(self):
        self.driver.find_element_by_link_text('登入').click()
        time.sleep(2)
        self.driver.find_element_by_id("email").send_keys("285954980@qq.com")
        self.driver.find_element_by_id("password").send_keys("123456")

        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(3)

        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(5)

        # test = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(By.CLASS_NAME,'page-title'))
        title = self.driver.find_element_by_class_name('page-title')
        self.assertTrue(title.is_displayed())
        # 输入标题
        self.driver.find_element_by_id('L_title').send_keys('哈哈哈')

        # 点击标签选择框
        # self.driver.find_element_by_xpath("//div[@class='layui-input-inline']/select[@id='label_select']").click()
        self.driver.find_element_by_class_name('layui-edge').click()
        time.sleep(2)

        # 第二种 写法
        self.driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[@lay-value = "1"]').click()
        time.sleep(3)

        # 输入内容
        self.driver.switch_to.frame("LAY_layedit_1")
        content = '帖子内容。。。'

        self.driver.find_element_by_xpath("//body").send_keys(content)
        # self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()
        time.sleep(2)

        self.driver.find_element_by_class_name('layui-btn').click()

        #第一种不是不可行 时间合适就行，等待时间过长，提示框会消失，定位不到，等待时间较短，提示框还没出来，也定位不到
        time.sleep(1)

        #第二种可行
        # self.driver.implicitly_wait(5)

        # 第三种可行
        # WebDriverWait(self.driver, 10,0.5).until(
        #     EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'layui-layer')]/div")))


        alertKuang1 = self.driver.find_element_by_xpath("//*[contains(@id,'layui-layer')]/div")
        text = alertKuang1.text


        # alertKuang1 = self.driver.find_element_by_xpath("//*[contains(@class,'layui-layer-content')]").text
        time.sleep(3)
        print(text)
        self.assertEqual(text, '发布帖子失败!')


if __name__ == "__main__":
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestForum("testReleasePost_04"))
    filePath = "../report/testResult.html"
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report for me', description='This is my Report')
    runner.run(suiteTest)