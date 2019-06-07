import time

from selenium import webdriver
#from selenium.webdriver.support.select import Select

# browser='chrome'

# if(browser=='chrome'):
#     driver=webdriver.Chrome(executable_path="C:/Users/btm-fac/Downloads/chromedriver.exe")
# elif(browser=='ff'):
#     driver=webdriver.Firefox(executable_path="C:/Users/btm-fac/Downloads/geckodriver.exe")
# elif (browser=='ie'):
#     driver=webdriver.Ie(executable_path="C:/Users/btm-fac/Downloads/IEDriverServer.exe")
#
# if(browser=='chrome'):
#     driver=webdriver.Chrome()
# elif(browser=='ff'):
#     driver=webdriver.Firefox()
# elif (browser=='ie'):
#     driver=webdriver.Ie()
#
#
# driver.get("http://www.facebook.com")
# driver.implicitly_wait(30)
# driver.find_element_by_name("firstname").send_keys("Harish")
# driver.find_element_by_name("lastname").send_keys("Qspiders")
# driver.find_element_by_xpath("//input[contains(@aria-label,'Mobile number')]").send_keys("3216549877")
# driver.find_element_by_xpath("//input[@value='2']").click()
#
# day = driver.find_element_by_name("birthday_day")# return type is WebElement
#
# s1=Select(day)
# s1.select_by_visible_text("30")
#
# month = driver.find_element_by_id("month")
# s2=Select(month)
# s2.select_by_value("5")
#
#
#
# year = driver.find_element_by_id("year")
# s3=Select(year)
# s3.select_by_index("2")
#
# driver.find_element_by_name("websubmit").click()
from selenium.webdriver.support.select import Select

browser='chrome'

if(browser=='chrome'):
    driver=webdriver.Chrome()
elif(browser=='ff'):
    driver=webdriver.Firefox()
elif (browser=='ie'):
    driver=webdriver.Ie()

driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.implicitly_wait(30)
#driver.find_element_by_id("datepicker").click()
framevar = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to_frame(framevar)
driver.find_element_by_xpath("//input[@class='hasDatepicker']").click()
month = driver.find_element_by_class_name("ui-datepicker-month")
s1 = Select(month)
s1.select_by_visible_text("Mar")
year = driver.find_element_by_class_name("ui-datepicker-year")
s2=Select(year)
s2.select_by_value("2010")
driver.find_element_by_xpath("//a[text()='3']").click()












#Assignment>> 1) Perform Select operation  2)Explain all exceptions  3)challen
#4) Webelemet 5)Multiple select