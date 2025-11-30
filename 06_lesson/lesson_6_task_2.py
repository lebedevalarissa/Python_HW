from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
    
input_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
input_field.clear()  
input_field.send_keys("SkyPro")
  
blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()
  
button_text = blue_button.text
print(button_text)
  
driver.quit()