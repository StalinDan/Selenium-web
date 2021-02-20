import os

import pytest

if __name__ == '__main__':
    # 可以打印测试模块的信息,输出print
    # pytest.main(['-s'])

    # 可以打印测试模块的详细信息，包括模块名，类名、测试用例名
    # pytest.main(['-vs'])

    # 指定用例执行
    # pytest.main(['-vs','test_login.py'])

    # 两个线程运行
    # pytest.main(['-vs','-n=2'])

    # 失败重跑2次
    pytest.main(['-vs','--reruns=2'])

    #生成allure报告
    os.system('allure generate ./temp -o ./report --clean')



