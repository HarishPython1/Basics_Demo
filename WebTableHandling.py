from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/btm-fac/Desktop/WebTableDemo.html")
#Fetch individual Value
#var = driver.find_element_by_xpath("//*[@id='123']/tbody/tr[2]/td[3]").text
#print(var)  #text>>is a function>>used to fetch text of webelement
#Fetch 1st row all values
#driver.find_element_by_xpath("//*[@id="123"]/tbody/tr[1]")
# ele = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[1]/td")
# print(ele)#ele is of type list>>stored webelements
# print(len(ele))
# for i in ele:
#     print(i.text)

col_val = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[1]/td")
col_count = len(col_val)
print("col count ",col_count)

row_val = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr")
row_count = len(row_val)
print("row count ",row_count)

row_val = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr")
row_count = len(row_val)
print("row count ",row_count)








