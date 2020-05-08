from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from xvfbwrapper import Xvfb
from selenium.webdriver import DesiredCapabilities

def before_all(context):
    print("> Starting the Browser")
    context.browser = webdriver.Chrome('/Users/kkavuri/Documents/github/ttc-bdd/chromedriver')

def after_all(context):
    print("> Closing the browser")
    context.browser.close()

