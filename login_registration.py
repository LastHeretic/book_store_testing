from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

# 1. Откройте https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")

# Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(5)

# 2. Нажмите на вкладку "My Account"
MyAccount = driver.find_element_by_css_selector('#menu-item-50').click()

# 3. В разделе "Register", введите email для регистрации
Register = driver.find_element_by_css_selector('#reg_email')
Register.send_keys("TupikovAQA@yandex.ru")

# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
Password = driver.find_element_by_css_selector('#reg_password')
Password.send_keys("12345Test@Test.test")

# 5. Нажмите на кнопку "Register"
Register_btn = WebDriverWait(driver, 60).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="Register"]')) ).click()

time.sleep(10)

# 1. Откройте https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")

# Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(5)

# 2. Нажмите на вкладку "My Account"
MyAccount = driver.find_element_by_css_selector('#menu-item-50').click()

# 3. В разделе "Login", введите email для логина
Email = driver.find_element_by_css_selector('#username')
Email.send_keys("TupikovAQA@yandex.ru")

# 4. В разделе "Login", введите пароль для логина
Password = driver.find_element_by_css_selector('#password')
Password.send_keys("12345Test@Test.test")

# 5. Нажмите на кнопку "Login"
Login_btn = WebDriverWait(driver, 60).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="Login"]')) ).click()

# 6. Добавьте проверку, что на странице есть элемент "Logout"
Logout= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout > a"), "Logout"))

driver.quit()