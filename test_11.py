import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

# login_standard_user = 'standard_user'
# password_all = 'secret_sauce'


# check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
# check_box.click()
# action = ActionChains(driver)
# double = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
# action.double_click(double).perform()
#
# right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
# action.context_click(right_click).perform()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
time.sleep(3)
now_date = datetime.utcnow().strftime("%d")
print(now_date)
date = int(now_date) +1
locator = "//div[@aria-label='Choose Tuesday, August " + str(date) + "th, 2023']"
print(locator)

# now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
date_12 = driver.find_element(By.XPATH, locator)
date_12.click()

# date_12 = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]")
time.sleep(3)


# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# time.sleep(3)
# new_date.send_keys('06/21/1985')
# time.sleep(3)
# new_date.send_keys(Keys.RETURN)
time.sleep(3)