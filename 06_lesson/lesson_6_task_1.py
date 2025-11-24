from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
    
check_input = driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    
waiter = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
text = waiter.text
    
print(text)   

driver.quit()