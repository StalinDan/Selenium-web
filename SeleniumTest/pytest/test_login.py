import time

import pytest

age = 19

# @pytest.fixture(scope='function',autouse=True)
# @pytest.fixture(scope='class')
@pytest.fixture(scope='function',params=['苹果','香蕉','橘子'])
def my_fixture(request):
    print('这是前置的方法')
    # return和yield都表示返回的意思，但是return后面不能有代码，yield返回后，后面可以有代码
    yield request.param
    print('这是后置的方法')

    # return request.param

class TestLogin:

    # # 这个在所有的用例之前只执行一次
    # def setup_class(self):
    #     print('\n在每个类之前的初始化的工作，比如：创建日志对象、创建数据库的连接，创建接口的请求对象')
    #
    # # 在每个用例之前执行一次
    # def setup(self):
    #     print('\n在执行测试用例之前初始化的代码：打开浏览器、加载网页')

    def test_09_login1(self,my_fixture):
        # time.sleep(3)
        print('测试login1')
        print('----'+str(my_fixture))

    @pytest.mark.smoke
    def test_07_login2(self):
        # time.sleep(3)
        print('测试login2')

    @pytest.mark.skipif(age>18,reason='已成年，就跳过')
    def test_08_login3(self):
        # time.sleep(3)
        print('测试login3')
        # assert 1 == 2

    @pytest.mark.skip(reason='跳过原因')
    @pytest.mark.run(order=2)
    @pytest.mark.user
    def test_04_login4(self):
        # time.sleep(3)
        print('测试login4')

    @pytest.mark.run(order=1)
    def test_03_login5(self):
        # time.sleep(3)
        print('测试login4')


    # def teardown(self):
    #     print('\n 在执行用例之后的扫尾的代码：关闭浏览器')
    #
    #
    # def teardown_class(self):
    #     print('\n 在每个类执行后的扫尾的工作，比如：销毁日志对象、销毁数据库的连接，销毁接口的请求对象')


# if __name__ == '__main__':
#     pytest.main(['-s'])