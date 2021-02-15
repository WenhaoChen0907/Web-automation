# 绝对路径

from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://www.baidu.com"
driver.get(url)


driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("淘宝")

sleep(3)

driver.quit()