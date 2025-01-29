from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

# Shop: отображение страницы товара

# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # Реализуйте неявное ожидание поиска элементов
# driver.implicitly_wait(5)
#
# # 2. Залогиньтесь
# # . Нажмите на вкладку "My Account"
# MyAccount = driver.find_element_by_css_selector('#menu-item-50').click()
# # . В разделе "Login", введите email для логина
# Email = driver.find_element_by_css_selector('#username')
# Email.send_keys("TupikovAQA@yandex.ru")
# # . В разделе "Login", введите пароль для логина
# Password = driver.find_element_by_css_selector('#password')
# Password.send_keys("12345Test@Test.test")
# # . Нажмите на кнопку "Login"
# Login_btn = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="Login"]')) ).click()
#
# # 3. Нажмите на вкладку "Shop"
# Shop = driver.find_element_by_css_selector('#menu-item-40').click()
#
# # 4. Откройте книгу "HTML 5 Forms"
# HTML_5_Forms = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]').click()
#
# # 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
# HTML5_Form= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms"))
#
# driver.quit()

# # Shop: количество товаров в категории

# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # Реализуйте неявное ожидание поиска элементов
# driver.implicitly_wait(5)
#
# # 2. Залогиньтесь
#
# # . Нажмите на вкладку "My Account"
# MyAccount = driver.find_element_by_css_selector('#menu-item-50').click()
# # . В разделе "Login", введите email для логина
# Email = driver.find_element_by_css_selector('#username')
# Email.send_keys("TupikovAQA@yandex.ru")
# # . В разделе "Login", введите пароль для логина
# Password = driver.find_element_by_css_selector('#password')
# Password.send_keys("12345Test@Test.test")
# # . Нажмите на кнопку "Login"
# Login_btn = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="Login"]')) ).click()
#
# # 3. Нажмите на вкладку "Shop"
# Shop = driver.find_element_by_css_selector('#menu-item-40').click()
#
# # 4. Откройте категорию "HTML"
# HTML = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product-category/html/"]').click()
#
# # 5. Добавьте тест, что отображается три товара
# HTML3= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cat-item.cat-item-19.current-cat > span"), "3"))
#
# driver.quit()

# Shop: сортировка товаров

# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # Реализуйте неявное ожидание поиска элементов
# driver.implicitly_wait(5)
#
# # 2. Залогиньтесь
# # . Нажмите на вкладку "My Account"
# MyAccount = driver.find_element_by_css_selector('#menu-item-50').click()
# # . В разделе "Login", введите email для логина
# Email = driver.find_element_by_css_selector('#username')
# Email.send_keys("TupikovAQA@yandex.ru")
# # . В разделе "Login", введите пароль для логина
# Password = driver.find_element_by_css_selector('#password')
# Password.send_keys("12345Test@Test.test")
# # . Нажмите на кнопку "Login"
# Login_btn = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="Login"]')) ).click()
#
# # 3. Нажмите на вкладку "Shop"
# Shop = driver.find_element_by_css_selector('#menu-item-40').click()
#
# # 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# # • Используйте проверку по value
# Default = driver.find_element_by_css_selector ('[value="menu_order"]')
# element_check = WebDriverWait(driver,  10).until(
# EC.element_to_be_selected(Default))
#
# # 5. Отсортируйте товары по цене от большей к меньшей
# # • в селекторах используйте класс Select
# from selenium.webdriver.support.select import Select
# element = driver.find_element_by_xpath('//select[@name="orderby"]')
# select = Select(element)
# select.select_by_value('price-desc')
#
# # 6. Снова объявите переменную с локатором основного селектора сортировки т.к после сортировки страница обновится
# element = driver.find_element_by_xpath('//select[@name="orderby"]')
#
# # 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# # • Используйте проверку по value
# PriceHighToLow = driver.find_element_by_css_selector ('[value="price-desc"]')
# element_check = WebDriverWait(driver,  10).until(
# EC.element_to_be_selected(PriceHighToLow))

# driver.quit()

# # Shop: отображение, скидка товара
# # 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # Реализуйте неявное ожидание поиска элементов
# driver.implicitly_wait(5)
#
# # 2. Залогиньтесь
# # . Нажмите на вкладку "My Account"
# MyAccount = driver.find_element_by_css_selector('#menu-item-50').click()
# # . В разделе "Login", введите email для логина
# Email = driver.find_element_by_css_selector('#username')
# Email.send_keys("TupikovAQA@yandex.ru")
# # . В разделе "Login", введите пароль для логина
# Password = driver.find_element_by_css_selector('#password')
# Password.send_keys("12345Test@Test.test")
# # . Нажмите на кнопку "Login"
# Login_btn = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="Login"]')) ).click()
#
# # 3. Нажмите на вкладку "Shop"
# Shop = driver.find_element_by_css_selector('#menu-item-40').click()
#
# # 4. Откройте книгу "Android Quick Start Guide"
# AndroidQuickStartGuide = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product/android-quick-start-guide/"]').click()
#
# # 5. Добавьте тест, что содержимое старой цены = "₹600.00"
#
# # OldPrice= WebDriverWait(driver, 10).until(
# #  EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "₹600.00"))
#
# element = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span") # нашли элемент по составному селектору
# element_get_text = element.text # получили текст элемента с помощью .text
# assert element_get_text == "₹600.00"
#
# # 6. Добавьте тест, что содержимое новой цены = "₹450.00"
# element = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span") # нашли элемент по составному селектору
# element_get_text = element.text # получили текст элемента с помощью .text
# assert element_get_text == "₹450.00"
#
# # 7. Добавьте явное ожидание и нажмите на обложку книги
# # • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки
# # (не вся картинка на всю страницу)
# Book = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-169 > div.images > a > img')) ).click()
#
# # 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# Book_btn = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) ).click()

# driver.quit()

# Shop: проверка цены в корзине

# 1. Откройте https://practice.automationtesting.in/
# driver.get("https://practice.automationtesting.in/")
#
# # Реализуйте неявное ожидание поиска элементов
# driver.implicitly_wait(10)
#
# # 2. Нажмите на вкладку "Shop"
# Shop = driver.find_element_by_css_selector('#menu-item-40').click()
#
# # 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# HTML5WebAppDevelopment = driver.find_element_by_css_selector('[data-product_id="182"]').click()
#
# time.sleep(10)
#
# # 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# # • Используйте для проверки assert
# element = driver.find_element_by_css_selector("span.cartcontents") # нашли элемент по составному селектору
# element_get_text = element.text # получили текст элемента с помощью .text
# assert element_get_text == "1 Item"
#
# element = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount") # нашли элемент по составному селектору
# element_get_text = element.text # получили текст элемента с помощью .text
# assert   element_get_text == "₹180.00"
#
# # 5. Перейдите в корзину
# Basket = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]').click()
#
# # 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# Subtotal= WebDriverWait(driver, 10).until(
#   EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]'), "₹180.00"))
# #page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span > span
#
# # 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
# Total= WebDriverWait(driver, 10).until(
#   EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr.order-total > td > strong > span'), "₹183.60"))
#
# # driver.quit()

# # Shop: работа в корзине
# # Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# # 1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("https://practice.automationtesting.in/")
#
# # Реализуйте неявное ожидание поиска элементов
# driver.implicitly_wait(10)
#
# # 2. Нажмите на вкладку "Shop"
# Shop = driver.find_element_by_css_selector('#menu-item-40').click()
#
# # 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# # • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# driver.execute_script("window.scrollBy(0, 300);")
#
# # • После добавления 1-й книги добавьте sleep
# HTML5WebAppDevelopment = driver.find_element_by_css_selector('[data-product_id="182"]').click()
#
# time.sleep(30)
#
# JSDataStructuresandAlgorithm = driver.find_element_by_css_selector('[data-product_id="180"]').click()
#
# time.sleep(30)
# # 4. Перейдите в корзину
# Basket = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]').click()
#
#
# # 5. Удалите первую книгу
# # • Перед удалением добавьте sleep
# time.sleep(10)
#
# BasketDelete = driver.find_element_by_css_selector('[data-product_id="182"]').click()
#
# # 6. Нажмите на Undo (отмена удаления)
# Undo = driver.find_element_by_css_selector('div.woocommerce-message > a').click()
#
# # 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# # • Предварительно очистите поле с помощью локатор_поля.clear()
# Clear = driver.find_element_by_css_selector('td.product-quantity > div > input').clear()
# Clear = driver.find_element_by_css_selector('td.product-quantity > div > input')
# Clear.send_keys("3")
#
# # 8. Нажмите на кнопку "UPDATE BASKET"
# UPDATEBASKET = driver.find_element_by_css_selector('[value="Update Basket"]').click()
#
# time.sleep(10)
#
# # 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# element = driver.find_element_by_css_selector("td.product-quantity > div > input") # нашли элемент по составному селектору
# element_check = element.get_attribute("value") # получили текст элемента с помощью .text
# assert element_check == "3"
#
# # 10. Нажмите на кнопку "APPLY COUPON"
# # • Перед нажатимем добавьте sleep
# time.sleep(10)
# APPLYCOUPON = driver.find_element_by_css_selector('[value="Apply Coupon"]').click()
#
# # 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# # # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии
# Pleaseenteracouponcode = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))

# driver.quit()

# Shop: покупка товара
# 1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get("https://practice.automationtesting.in/")

# Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(10)

# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
Shop = driver.find_element_by_css_selector('#menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")

# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
HTML5WebAppDevelopment = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(30)

# 4. Перейдите в корзину
Basket = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]').click()

# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
PROCEEDTOCHECKOUT = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button.button.alt.wc-forward')) ).click()

# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание

Firstname = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_first_name')) )
Firstname.send_keys( "Sherlock")

LastName = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_last_name')) )
LastName.send_keys( "Holmes")

EmailAddress = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_email')) )
EmailAddress.send_keys( "SherlockHolmes@yandex.ru")

Phone = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_phone')) )
Phone.send_keys( "1234567890")

Address  = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_address_1')) )
Address .send_keys( "Baker Street")

Town  = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_city')) )
Town .send_keys( "London")

Postcode   = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_postcode')) )
Postcode.send_keys( "0987654321")

# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже

Country = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '.select2-arrow')) ). click()

Country2 = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#s2id_autogen1_search')) )
Country2.send_keys( "Russia")

Country3 = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '.select2-result-label')) ). click()

State = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_state')) ). click()

State2 = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#billing_state')) )
State2.send_keys( "London")

# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(10)
CheckPayments = driver.find_element_by_css_selector('#payment_method_cheque').click()

# 8. Нажмите PLACE ORDER
PLACEORDER = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '#place_order')) ). click()

# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
ThankyouYourorderhasbeenreceived = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
CheckPayments = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.method > strong"), "Check Payments"))

driver.quit()