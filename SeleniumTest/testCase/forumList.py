# coding=utf-8
from selenium import webdriver
import unittest
import os
import time
from report import HTMLTestRunner


class Testlogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://47.104.84.186:8080/")
        self.driver.maximize_window()
        time.sleep(5)

    def tearDown(self):
        print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testTT01_01(self):
        '''测试帖子按钮文案显示是否正常'''
        self.driver.find_element_by_link_text("登入").click()
        time.sleep(2)
        self.driver.find_element_by_id("email").send_keys("tester666@qq.com")
        self.driver.find_element_by_id("password").send_keys("123qwe")
        self.driver.find_element_by_class_name("layui-btn").click()
        time.sleep(5)
        allForum = self.driver.find_element_by_xpath("//span[@id='postCata']/a[1]")
        bestForum = self.driver.find_element_by_xpath("//span[@id='postCata']/a[2]")
        topForum = self.driver.find_element_by_xpath("//span[@id='postCata']/a[3]")
        techType = self.driver.find_element_by_xpath("//span[@id='postCata']/a[4]")
        print(allForum.text)
        self.assertTrue(allForum.is_displayed())
        self.assertEqual("全部帖",allForum.text)
        self.assertEqual("精品帖", bestForum.text)
        self.assertEqual("置顶帖", topForum.text)
        self.assertEqual("技术文章分类", techType.text)
        self.assertNotEqual("技术文章", techType.text)
        self.assertIn(techType.text,"技术文章分类的身份和数据库")
        self.assertFalse(allForum.is_displayed())
        if allForum.text != "全部帖":
            print("不等于")
            self.driver.find_element_by_class_name("wangmazi王麻子")

    def testTT01_02(self):
        '''论坛搜索功能'''
        self.driver.find_element_by_link_text("登入").click()
        time.sleep(2)
        self.driver.find_element_by_id("email").send_keys("tester666@qq.com")
        self.driver.find_element_by_id("password").send_keys("123qwe")
        self.driver.find_element_by_class_name("layui-btn").click()
        time.sleep(5)
        self.driver.find_element_by_id("index_search_words").send_keys("BUG的要素有哪些")
        self.driver.find_element_by_xpath("//form[@id='postsSearch']/i").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_xpath("//h2[@class='fly-tip']/a")
        self.assertEqual(searchText.text, "BUG的要素有哪些")

if __name__ == "__main__":
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Testlogin("testTT01_01"))
    suiteTest.addTest(Testlogin("testTT01_02"))
    filePath = "../report/testResult.html"
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report for me', description='This is my Report')
    runner.run(suiteTest)


