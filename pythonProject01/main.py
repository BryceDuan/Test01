import pytest
import time
import os


if __name__ == '__main__':
    print("测试开始：")
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./report --clean")


