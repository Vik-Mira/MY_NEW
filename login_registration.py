# import time 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select 
# from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Chrome()
# driver.maximize_window()

# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID, "menu-item-50").click()
# reg = driver.find_element(By.ID, "reg_email") 
# reg.send_keys("Nik@gmail.com")
# passw = driver.find_element(By.ID, "reg_password") 
# passw.send_keys("QwertyQwerty1234__12345")
# driver.find_element(By.XPATH, "//input[@name='register']").click()
# driver.quit()









import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element(By.ID, "menu-item-50").click()
reg1 = driver.find_element(By.ID, "username") 
reg1.send_keys("Nik@gmail.com")
passwd = driver.find_element(By.ID, "password") 
passwd.send_keys("QwertyQwerty1234__12345")
driver.find_element(By.XPATH, "//input[@name='login']").click()

# htm = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "modal-body"))
# )
# assert "Lorem" in message.text
time.sleep(5)
htm = driver.find_element(By.CLASS_NAME, "page-template-default")
assert "Logout" in htm.text
time.sleep(5)

driver.quit()


