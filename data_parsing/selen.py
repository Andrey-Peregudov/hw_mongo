from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.cbr.ru")

driver.implicitly_wait(5)

print(driver.title)
print(driver.current_url)
print(driver.name)

driver.find_elements(By.ID, 'dynamicBtn')

driver.quit()