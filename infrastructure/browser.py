from platform import machine
from sys import platform

from selenium import webdriver


def get_path_to_chrome_driver():
    if platform.startswith("linux"):
        return "drivers/chromedriver_linux64/chromedriver"
    elif platform == "darwin":
        if machine() == "arm64":
            return "drivers/chromedriver_mac64_m1/chromedriver"
        else:
            return "drivers/chromedriver_mac64/chromedriver"
    elif platform == "win32":
        return "drivers/chromedriver_win32/chromedriver.exe"


driver = webdriver.Chrome(executable_path=get_path_to_chrome_driver())
