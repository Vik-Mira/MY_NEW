# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select 
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID, "menu-item-50").click()
# reg1 = driver.find_element(By.ID, "username") 
# reg1.send_keys("Nik@gmail.com")
# passwd = driver.find_element(By.ID, "password") 
# passwd.send_keys("QwertyQwerty1234__12345")
# driver.find_element(By.XPATH, "//input[@name='login']").click()
# time.sleep(5)
# driver.find_element(By.ID, "menu-item-40").click()
# driver.find_element(By.CLASS_NAME, "post-181").click()
# test = driver.find_element(By.XPATH, "//h1[text()='HTML5 Forms']")
# assert test.text == "HTML5 Forms"
# time.sleep(5)
# driver.quit()









# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select 
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID, "menu-item-50").click()
# reg1 = driver.find_element(By.ID, "username") 
# reg1.send_keys("Nik@gmail.com")
# passwd = driver.find_element(By.ID, "password") 
# passwd.send_keys("QwertyQwerty1234__12345")
# driver.find_element(By.XPATH, "//input[@name='login']").click()
# time.sleep(5)
# driver.find_element(By.ID, "menu-item-40").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//a[text()='HTML']").click()
# time.sleep(5)
# items_count = driver.find_elements(By.CLASS_NAME, "woocommerce-LoopProduct-link")
# assert len(items_count) == 3
# driver.quit()










# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select 
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID, "menu-item-50").click()
# reg1 = driver.find_element(By.ID, "username") 
# reg1.send_keys("Nik@gmail.com")
# passwd = driver.find_element(By.ID, "password") 
# passwd.send_keys("QwertyQwerty1234__12345")
# driver.find_element(By.XPATH, "//input[@name='login']").click()
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "menu-item-40")))
# driver.find_element(By.ID, "menu-item-40").click()
# ord = driver.find_element(By.CLASS_NAME, "orderby")
# assert ord.get_attribute("value") == "menu_order"
# select = Select(ord) 
# select.select_by_value("price-desc")
# ord = driver.find_element(By.CLASS_NAME, "orderby")
# assert ord.get_attribute("value") == "price-desc"
# driver.quit()










# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select 
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID, "menu-item-50").click()
# reg1 = driver.find_element(By.ID, "username") 
# reg1.send_keys("Nik@gmail.com")
# passwd = driver.find_element(By.ID, "password") 
# passwd.send_keys("QwertyQwerty1234__12345")
# driver.find_element(By.XPATH, "//input[@name='login']").click()
# driver.find_element(By.ID, "menu-item-40").click()
# driver.find_element(By.XPATH, "//h3[text()='Android Quick Start Guide']").click()
# star_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='600.00']")))
# assert star_price.text == '₹600.00'
# new_price = driver.find_element(By.XPATH, "//span[text()='450.00']")
# assert new_price.text == '₹450.00'
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-main-image")))
# driver.find_element(By.CLASS_NAME, "woocommerce-main-image").click()
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "fullResImage")))
# driver.find_element(By.CLASS_NAME, "pp_close").click()
# driver.quit()









# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select 
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID, "menu-item-40").click()
# driver.find_element(By.XPATH, "//a[@data-product_id='182']").click()
# time.sleep(5)
# amount = driver.find_element(By.XPATH, "//span[text()='1 item']")
# price = driver.find_element(By.XPATH, "//span[text()='₹180.00']")
# assert price.text == '₹180.00' and amount.text == '1 Item'
# driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
# WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//td[@data-title='Subtotal']"), "180.00"))
# WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//span[text()='183.60']"), "183.60"))
# driver.quit()












# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select 
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID, "menu-item-40").click()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element(By.XPATH, "//a[@data-product_id='182']").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//a[@data-product_id='180']").click()
# driver.find_element(By.CLASS_NAME, "cartcontents").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//a[@data-product_id='182']").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//a[text()='Undo?']").click()
# Quantity = driver.find_element(By.XPATH, "//input[contains(@name, '045117')]")
# Quantity.clear()
# Quantity.send_keys("3")
# driver.find_element(By.XPATH, "//input[@value='Update Basket']").click()
# time.sleep(5)
# val = driver.find_element(By.XPATH, "//input[contains(@name, '045117')]")
# assert val.get_attribute("value") == "3"
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, ".coupon input.button").click()
# WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code.")) 
# driver.quit()















import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select 
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element(By.ID, "menu-item-40").click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element(By.XPATH, "//a[@data-product_id='182']").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "cartcontents").click()
pr = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
pr.click()
first_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "billing_first_name")))
first_name.send_keys("Nik")
driver.find_element(By.ID, "billing_last_name").send_keys("Ryz")
driver.find_element(By.ID, "billing_email").send_keys("Nik@gmail.com")
driver.find_element(By.ID, "billing_phone").send_keys("89000000000")

driver.find_element(By.CSS_SELECTOR, ".select2-container.country_to_state.country_select").click()
driver.find_element(By.ID, "s2id_autogen1_search").send_keys("Russia")
# driver.find_element(By.CSS_SELECTOR, ".select2-results-dept-0.select2-result.select2-result-selectable:nth-child(182)").click()

# country = driver.find_element(By.ID, "#select2-results-1") 
# select = Select(country) 
# select.select_by_value("Russia")


country_input = driver.find_element(By.ID, "s2id_autogen1_search")
# country_input.send_keys("russ")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".select2-results li")))
driver.find_element(By.CSS_SELECTOR, ".select2-results li:first-child").click()

driver.find_element(By.ID, "billing_address_1").send_keys("Sputnik")
driver.find_element(By.ID, "billing_city").send_keys("Moscow")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@name = 'billing_state']").send_keys("Moscow")


driver.find_element(By.ID, "billing_postcode").send_keys("QWERTY")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
driver.find_element(By.ID, "payment_method_cheque").click() 
driver.find_element(By.ID, "place_order").click()

WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))
driver.quit()
