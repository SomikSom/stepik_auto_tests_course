import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


n1 = browser.find_element(By.XPATH, "//span[@id='num1']")
n2 = browser.find_element(By.XPATH, "//span[@id='num2']")

x = n1.text
y = n2.text
s = int(x) + int(y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(s))


button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()


time.sleep(5)
browser.quit()