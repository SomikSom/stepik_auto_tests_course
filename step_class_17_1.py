import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

#   ___________________________________________
#  2.4.7
# link = "http://suninjuly.github.io/wait1.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
#
# button = browser.find_element(By.XPATH, '//button[@id="verify"]')
# button.click()
#____
#
#
# ________________________________________________'
#
#
#               2.4.8
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/cats.html")
#
# browser.implicitly_wait(5)

# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text
# browser.find_element(By.ID, "button")

# ____________________________________________
#                2.4.9
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text
# _________________________________________________________________
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

# закрываем браузер после всех манипуляций
time.sleep(5)
browser.quit()