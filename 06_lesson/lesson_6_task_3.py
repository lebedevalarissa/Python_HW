from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
element = WebDriverWait(driver,20).until(
  EC.presence_of_element_located ((By.CLASS_NAME, "col-12")))

img_element = WebDriverWait(driver,20).until(
  EC.presence_of_element_located ((By.CSS_SELECTOR, "#award")))
    
src_value = img_element.get_attribute("src")
    
print(src_value)
    
driver.quit()