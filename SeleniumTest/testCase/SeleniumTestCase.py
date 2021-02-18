# coding=utf-8
from selenium import webdriver
import unittest
import os
import time,logging.config
from report import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

class TestForum(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("http://47.104.84.186:8080/")
        self.driver.get("https://apartment.deayea.com/login")
        self.driver.maximize_window()
        time.sleep(3)

    def tearDown(self):
        print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        filedir = '../screenShot/'
        if not os.path.exists(filedir):
            os.makedirs(os.path.join(filedir))

        # screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        # self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    #测试发布帖子：不输入任何内容，点击发布
    def testReleasePost_01(self):
        self.driver.find_element_by_link_text('登入').click()
        time.sleep(2)
        self.driver.find_element_by_id("email").send_keys("285954980@qq.com")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_class_name("layui-btn").click()
        time.sleep(3)
        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(5)

        # test = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(By.CLASS_NAME,'page-title'))
        title = self.driver.find_element_by_class_name('page-title')
        self.assertTrue(title.is_displayed())
        #点击立即发布按钮
        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(2)
        #内容框是否显示 ，显示：发布失败  不显示：发布成功
        contentKuang = self.driver.find_element_by_xpath('//div[@class="layui-layedit-iframe"]/iframe')
        self.assertTrue(contentKuang.is_displayed())

    #只输入标题，点击发布
    def testReleasePost_02(self):
        self.driver.find_element_by_link_text('登入').click()
        time.sleep(2)
        self.driver.find_element_by_id("email").send_keys("285954980@qq.com")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_class_name("layui-btn").click()
        time.sleep(3)
        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(5)

        # test = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(By.CLASS_NAME,'page-title'))
        title = self.driver.find_element_by_class_name('page-title')
        self.assertTrue(title.is_displayed())
        #只输入标题，点击立即发布按钮
        self.driver.find_element_by_id('L_title').send_keys('哈哈哈')

        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(2)
        # 内容框是否显示 ，显示：发布失败  不显示：发布成功
        contentKuang = self.driver.find_element_by_xpath('//div[@class="layui-layedit-iframe"]/iframe')
        self.assertTrue(contentKuang.is_displayed())


    #发布帖子，输入标题 ，选择标签，点击发布
    def testReleasePost_03(self):
        self.driver.find_element_by_link_text('登入').click()
        time.sleep(2)
        self.driver.find_element_by_id("email").send_keys("285954980@qq.com")
        self.driver.find_element_by_id("password").send_keys("123456")

        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(3)

        self.driver.find_element_by_class_name('layui-btn').click()
        # self.driver.find_element_by_css_selector('.layui-btn jie-add').click()
        time.sleep(5)

        # test = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(By.CLASS_NAME,'page-title'))
        title = self.driver.find_element_by_class_name('page-title')
        self.assertTrue(title.is_displayed())
        #输入标题
        self.driver.find_element_by_id('L_title').send_keys('哈哈哈')
        #点击标签选择框
        # self.driver.find_element_by_xpath("//div[@class='layui-input-inline']/select[@id='label_select']").click()
        # self.driver.find_element_by_class_name('layui-edge').click()
        self.driver.find_element_by_class_name('layui-input-inline').click()
        time.sleep(2)

        # #第一种写法：选择标签，不知为啥错误
        # # selectTag = self.driver.find_element_by_id('label_select')
        # # WebDriverWait(self.driver,10).until(EC.presence_of_element_located(selectTag))
        #
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"label_select")))
        # selectTag = self.driver.find_element_by_id('label_select')
        # time.sleep(3)
        #
        # # Select(selectTag).select_by_value('1')
        # Select(selectTag).select_by_visible_text('测试01')
        # time.sleep(5)


        #第二种 写法
        self.driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[@lay-value = "1"]').click()
        time.sleep(3)

        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(2)
        # 内容框是否显示 ，显示：发布失败  不显示：发布成功
        contentKuang = self.driver.find_element_by_xpath('//div[@class="layui-layedit-iframe"]/iframe')
        self.assertTrue(contentKuang.is_displayed())

 #发布帖子，输入标题 ，输入内容，选择标签，点击发布
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
        #输入标题
        self.driver.find_element_by_id('L_title').send_keys('哈哈哈')


        #点击标签选择框
        # self.driver.find_element_by_xpath("//div[@class='layui-input-inline']/select[@id='label_select']").click()
        self.driver.find_element_by_class_name('layui-edge').click()
        time.sleep(2)


        # #第一种写法：选择标签，不知为啥错误
        # selectTag = self.driver.find_element_by_id('label_select')
        # selectTag1 = self.driver.find_element_by_tag_name('select')
        # time.sleep(3)
        #
        # # Select(selectTag).select_by_value('1')
        # Select(selectTag1).select_by_visible_text('测试01')
        # time.sleep(5)


        #第二种 写法
        self.driver.find_element_by_xpath('//dl[@class="layui-anim layui-anim-upbit"]/dd[@lay-value = "1"]').click()
        time.sleep(3)

        # 输入内容
        self.driver.switch_to.frame("LAY_layedit_1")
        content = '帖子内容。。。'
        # js = "document.getElementById('content_ifr').contentWindow.document.body.innerText = '%s'" % (content)
        # self.driver.execute_script(js)
        self.driver.find_element_by_xpath("//body").send_keys(content)
        # self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()
        time.sleep(2)


        self.driver.find_element_by_class_name('layui-btn').click()
        time.sleep(2)
        # 内容框是否显示 ，显示：发布失败  不显示：发布成功
        # contentKuang = self.driver.find_element_by_xpath('//div[@class="layui-layedit-iframe"]/iframe')
        # self.assertTrue(contentKuang.is_displayed())

        # WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//body/div[@class='layui-layer and @type='dialog']")))

        # alertKuang = self.driver.find_element_by_xpath("//body/div[@class='layui-layer and @type='dialog']")
        # layui-layer-msg
        # text = alertKuang.text

        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_elements_located((By.XPATH, "//*[contains(@id,'layui-layer')]/div")))
        alertKuang1 = self.driver.find_elements_by_xpath("//*[contains(@id,'layui-layer')]/div")

        # WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//*[contains(@type,'dialog')]")))
        # alertKuang2 = self.driver.find_element_by_xpath("//*[contains(@type,'dialog')]")


        time.sleep(3)
        text = alertKuang1[0].text
        # text = alertKuang1[0].get_attribute('innerText')
        print(text)
        self.assertEqual(alertKuang1[0].text, '发布帖子失败!')

    def test01_login(self):
        """测试登录"""
        logging.info("测试登录")
        self.driver.find_element_by_xpath('//*[@id="login-wrap"]/div[2]/div/div/form/div[1]/div/div/input').send_keys("123")
        self.driver.find_element_by_xpath('//*[@id="login-wrap"]/div[2]/div/div/form/div[2]/div/div/input').send_keys("123")
        self.driver.find_element_by_xpath('//*[@id="login-btn"]').click()
        # self.driver.implicitly_wait(10)
        time.sleep(2)
        # self.driver.switch_to.active_element('/html/body/div[2]')
        # self.driver.find_element_by_xpath('/html/body/div[2]')
        text = self.driver.find_element_by_xpath('/html/body/div[2]/p').text
        # alert = self.driver.switch_to.alert()
        # logging.info(alert.text())
        # print(alert.text())
        # self.driver.implicitly_wait(10)
        logging.info(text)
        self.assertEqual("登录成功",text)


if __name__ == "__main__":
    suiteTest = unittest.TestSuite()
    # suiteTest.addTest(TestForum("testReleasePost_01"))
    # suiteTest.addTest(TestForum("testReleasePost_02"))
    # suiteTest.addTest(TestForum("testReleasePost_03"))
    # suiteTest.addTest(TestForum("testReleasePost_04"))
    suiteTest.addTest(TestForum("test01_login"))
    filePath = "../report/testResult.html"
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report for me', description='This is my Report')
    runner.run(suiteTest)
