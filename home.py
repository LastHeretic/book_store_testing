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

# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")

# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
SeleniumRuby = driver.find_element_by_css_selector("a.woocommerce-LoopProduct-link > h3").click()

# 4. Нажмите на вкладку "REVIEWS"
REVIEWS = driver.find_element_by_css_selector('[href="#tab-reviews"]').click()

# 5. Поставьте 5 звёзд
STAR = driver.find_element_by_css_selector("a.star-5").click()

# 6. Заполните поле "Review" сообщением: "Nice book!"
Review = driver.find_element_by_css_selector('#comment')
Review.send_keys("Nice book!")

# 7. Заполните поле "Name"
Name = driver.find_element_by_css_selector('#author')
Name.send_keys("PETROV")

# 8. Заполните "Email"
EmailAddress = driver.find_element_by_css_selector('#email')
EmailAddress.send_keys("Test@Test.test")

# 9. Нажмите на кнопку "SUBMIT"
SUBMIT = driver.find_element_by_css_selector('#submit').click()

driver.quit()