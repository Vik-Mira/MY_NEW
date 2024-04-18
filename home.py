import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")

driver.find_element(By.XPATH, "//h3[text()='Selenium Ruby']").click()
driver.find_element(By.CLASS_NAME, "reviews_tab").click()
driver.find_element(By.CSS_SELECTOR, ".stars > span :nth-child(5)").click()

comm = driver.find_element(By.ID, "comment") 
comm.send_keys("Nice book!")
name = driver.find_element(By.ID, "author") 
name.send_keys("Nik")
male = driver.find_element(By.ID, "email") 
male.send_keys("Nik@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".form-submit > :nth-child(1)").click()

driver.quit()


