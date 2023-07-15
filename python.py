from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('file:///D:/SPM%20folder/DCproject/projectindex.html')
time.sleep(3)

# Click on the login button
driver.find_element(By.ID, "login").click()
time.sleep(1)
#click register for registration
driver.find_element(By.ID, "register1").click()
time.sleep(1)
driver.find_element(By.ID, "remail").send_keys('akshi@gmail.com')
time.sleep(1)
driver.find_element(By.ID, "rpassword").send_keys('12345')
time.sleep(1)
driver.find_element(By.ID, "register2").click()
alert = driver.switch_to.alert
alert.accept()

# Click on the login  button
driver.find_element(By.ID, "log2").click()
time.sleep(1)
# Fill in the email and password inputs
driver.find_element(By.ID, "email").send_keys('akshi@gmail.com')
time.sleep(1)
driver.find_element(By.ID, "password").send_keys('12345')
time.sleep(1)
# Click on the login submit button
driver.find_element(By.ID, "log").click()
time.sleep(1)
# Accept the alert dialog
alert = driver.switch_to.alert
alert.accept()

# Fill in the origin input
origin_input = driver.find_element(By.ID, "origin")
origin_input.send_keys('Bapatla Engineering College')
time.sleep(2)

# Wait for and select the origin suggestion
origin_suggestion = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='pac-item']"))
)
origin_suggestion.click()

# Fill in the destination input
destination_input = driver.find_element(By.ID, "destination")
destination_input.send_keys('Hyderabad')
time.sleep(2)

# Wait for and select the destination suggestion
destination_suggestion = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='pac-item']"))
)
destination_suggestion.click()
time.sleep(3)
# Click the submit button
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "find")))
submit_button.click()
time.sleep(10)

# Perform further actions on the map as needed

# Go back to the home page
driver.find_element(By.ID, "home").click()
time.sleep(1)

# Close the browser
driver.quit()
