import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
#   Переход на сайт
login_standard_user = 'standard_user'
password_all = 'secret_sauce'


user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
#   ввод данных имени
print('Input Login')

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
#   ввод пароля
print('Input Password')

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
#   нажатие кнопки Login
print('Click Button')

filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()

print('Use sort conteiner 1')
#   кнопка фильтра
time.sleep(1)

filter.send_keys(Keys.DOWN)
time.sleep(1)
# filter.send_keys(Keys.RETURN)
# time.sleep(1)
#   меню фильтра опускается на 1 в низ
filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()

print('Use sort conteiner 2')
time.sleep(1)

filter.send_keys(Keys.DOWN)
time.sleep(1)
# filter.send_keys(Keys.RETURN)
# time.sleep(1)
#   меню фильтра опускается на 1 в низ

filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()

print('Use sort conteiner 3')
time.sleep(1)

filter.send_keys(Keys.PAGE_UP)
time.sleep(1)
# filter.send_keys(Keys.RETURN)
# time.sleep(1)
#   меню фильтра возвращается на начало

# now_date = datetime.datetime.utcnow().strftime("%Y,%M,%D")
# new_screenshot = "screenshot" + now_date + ".png"
# driver.save_screenshot(new_screenshot)

text_item_name = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_text_item_name = text_item_name.text
print(value_text_item_name)
# вывод имени товара

product_price = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_product_price = product_price.text
print(value_product_price)
# вывод цены товара

product_item = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
product_item.click()
#   выбор конкретного товара
print('Click Item')


product_item_to_cart = driver.find_element(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
product_item_to_cart.click()
#   добавление ттовара в корзину
print('Click Item Cart')

go_to_cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
go_to_cart.click()
#   переход в корзину
print('Click GO Cart')

time.sleep(1)

text_item_cart = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_text_item_cart = text_item_cart.text
print(value_text_item_cart)
assert value_text_item_cart == value_text_item_name
print("Идентично")
# вывод имени товара

cart_product_price = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_product_price = cart_product_price.text
print(value_cart_product_price)
assert value_cart_product_price == value_product_price
print("Цена совпала")
# вывод цены товара

checkout_cart = driver.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button']")
checkout_cart.click()
#   переход к оплате
print('Click Check Cart')

user_name_1 = driver.find_element(By.XPATH, "//input[@id='first-name']")
user_name_1.send_keys("Sergey")
#   ввод первого имени
print('Input First Name')

user_name_2 = driver.find_element(By.XPATH, "//input[@id='last-name']")
user_name_2.send_keys('Som')
#   ввод второго имени
print('Input Last Name')

postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('123456')
#    ввод кода\ пароля
print('Input Postal Code')

button_continue = driver.find_element(By.XPATH, "//input[@class='submit-button btn btn_primary cart_button btn_action']")
button_continue.click()
#   нажатие кнопки продолжить
print('Continue')

button_finish = driver.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium cart_button']")
button_finish.click()
#   нажатие кнопки завершение
print('Button Finish')

button_back_home = driver.find_element(By.XPATH, "//button[@class='btn btn_primary btn_small']")
button_back_home.click()
#   нажатие кнопки возврат к покупкам
print('Button Back Home')

time.sleep(1)
button_menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
button_menu.click()
# кнопка скрытого меню
print('button_menu')

time.sleep(1)

button_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
button_about.click()
#   кнопка в скрытом меню (переход на другой сайт)
print('Button About')


# button_Tri_it_Free = driver.find_element(By.XPATH, "//buttun[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedDark MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-disableElevation MuiButton-root MuiButton-outlined MuiButton-outlinedDark MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-disableElevation css-hy804n']")
# button_Tri_it_Free.click()
# #   кнопка бесплатно на втором сайте
# print('Button Tri it Free')

driver.save_screenshot('new_page.jpg')
# делаем скрин текущей страницы

time.sleep(2)
driver.quit()