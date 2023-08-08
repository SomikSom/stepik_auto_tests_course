import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# driver.find_element(By.XPATH, "//TЭГ[@АТРИБУТ='ЗНАЧЕНИЕ']")

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'


user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)

# user_name.send_keys(Keys.BACKSPACE)

print('Input Login')

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)

print('Input Password')

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

print('Click Login Button')
filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()

print('Use sort conteiner')
time.sleep(3)

filter.send_keys(Keys.DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)
time.sleep(3)

filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()

print('Use sort conteiner')
time.sleep(3)

filter.send_keys(Keys.DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)
time.sleep(3)

# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_product = text_products.text
#
# print(value_text_product)

time.sleep(3)
driver.quit()