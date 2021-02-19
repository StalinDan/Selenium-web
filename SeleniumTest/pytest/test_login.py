import time

import pytest


class TestLogin:
    def test_09_login1(self):
        # time.sleep(3)
        print('测试login1')

    @pytest.mark.smoke
    def test_07_login2(self):
        # time.sleep(3)
        print('测试login2')

    def test_08_login3(self):
        # time.sleep(3)
        print('测试login3')
        # assert 1 == 2

    @pytest.mark.run(order=2)
    @pytest.mark.user
    def test_04_login4(self):
        # time.sleep(3)
        print('测试login4')

    @pytest.mark.run(order=1)
    def test_03_login5(self):
        # time.sleep(3)
        print('测试login4')


# if __name__ == '__main__':
#     pytest.main(['-s'])