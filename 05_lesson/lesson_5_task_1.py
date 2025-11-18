from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome()
Service=ChromeService(ChromeDriverManager().install())

driver.get("http://uitestingplayground.com/classattr")
    
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()

sleep(5)