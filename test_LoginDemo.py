import time

from selenium import webdriver

def test_login():
    driver=webdriver.Chrome()
    driver.get("http://btm-fac8-pc:8080/login.do")
    time.sleep(3)
    driver.implicitly_wait(30)
    driver.find_element_by_name("username").send_keys("admin")
    time.sleep(3)
    driver.find_element_by_name("pwd").send_keys("manager")
    time.sleep(3)
    driver.find_element_by_id("loginButton").click()
    time.sleep(3)

def test_login1():
    driver=webdriver.Chrome()
    driver.get("http://btm-fac8-pc:8080/login.do")
    time.sleep(3)
    driver.implicitly_wait(30)
    driver.find_element_by_name("username").send_keys("admin")
    time.sleep(3)
    driver.find_element_by_name("pwd").send_keys("manager")
    time.sleep(3)
    driver.find_element_by_id("loginButton").click()
    time.sleep(3)
