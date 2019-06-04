from selenium import webdriver

browser='ie'

# if(browser=='chrome'):
#     driver=webdriver.Chrome(executable_path="C:/Users/btm-fac/Downloads/chromedriver.exe")
# elif(browser=='ff'):
#     driver=webdriver.Firefox(executable_path="C:/Users/btm-fac/Downloads/geckodriver.exe")
# elif (browser=='ie'):
#     driver=webdriver.Ie(executable_path="C:/Users/btm-fac/Downloads/IEDriverServer.exe")

if(browser=='chrome'):
    driver=webdriver.Chrome()
elif(browser=='ff'):
    driver=webdriver.Firefox()
elif (browser=='ie'):
    driver=webdriver.Ie()



driver.get("http://www.facebook.com")
driver.implicitly_wait(30)
driver.find_element_by_name("firstname").send_keys("Harish")
driver.find_element_by_name("lastname").send_keys("Qspiders")
driver.find_element_by_xpath("//input[contains(@aria-label,'Mobile number')]").send_keys("3216549877")
driver.find_element_by_xpath("//input[@value='2']").click()
driver.find_element_by_name("websubmit").click()
#Assignment>> 1) Perform Select operation  2)Explain all exceptions  3)challenges faced