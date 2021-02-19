import pytest

if __name__ == '__main__':
    # 可以打印测试模块的信息,输出print
    # pytest.main(['-s'])

    # 可以打印测试模块的详细信息，包括模块名，类名、测试用例名
    # pytest.main(['-vs'])

    # 指定用例执行
    # pytest.main(['-vs','test_login.py'])

    # 指定文件目录执行
    # pytest.main(['-vs','./pytest_interface'])

    # 根据nodeID指定函数执行,nodeid由模块名，分隔符，类名、方法名，函数名组成。
    pytest.main(['-vs','./pytest_interface/test_interface.py::test_02_func'])

    pytest.main(['-vs','./pytest_interface/test_interface.py::TestInterface::test_01_search'])