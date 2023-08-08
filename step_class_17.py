import math
import time


from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button_1.click()

time.sleep(3)
# переключение вкладок
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.XPATH, "//*[@id='input_value']")
x = int(x.text)
y = calc(x)

browser.execute_script("window.scrollBy(0, 150);")

input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
input1.send_keys(y)

button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
button.click()

time.sleep(20)
browser.quit()
