import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import math
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import driver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)



x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
x = x_element.text
x = int(x)
y = calc(x)

browser.execute_script("window.scrollBy(0, 150);")

input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input1.send_keys(y)
# time.sleep(2)

input2 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
input2.click()
# time.sleep(2)

input3 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
input3.click()
# time.sleep(2)


button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# button = browser.find_element(By.XPATH, "//button[@type='submit']")
# button.click()

# закрываем браузер после всех манипуляций
time.sleep(5)
browser.quit()