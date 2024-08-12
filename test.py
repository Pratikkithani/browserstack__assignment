import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys

#browserstack-sdk python ./tests/test.py
#env\Scripts\activate



options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.flipkart.com/")
    # driver.maximize_window()

    # Search for the product
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Samsung Galaxy S10")
    search_box.send_keys(Keys.RETURN)

    # Click on "Mobiles" in categories
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//a[@class="_1jJQdf _2Mji8F"]'))).click()
    
    time.sleep(3)
    # Click on "samsung"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//div[text()="SAMSUNG"]'))).click()

    #Click on assured
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH,'//div[@class="_3U-Vxu"]'))).click()
    
    # high ---> low
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH,"//div[text()='Price -- High to Low']"))).click()
    
    driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All Work is Done"}}'
            )

    time.sleep(5)
    #data of each product on page 1
    product_names = driver.find_elements(By.CLASS_NAME, "_4rR01T")
    display_prices = driver.find_elements(By.CLASS_NAME, "_30jeq3")
    product_links = driver.find_elements(By.CLASS_NAME, "_1fQZEK")

    # Create and print the list
    results_list = []
    for i in range(len(product_names)):
        results_list.append({
            "Product Name": product_names[i].text,
            "Display Price": display_prices[i].text,
            "Link to Product Details Page": product_links[i].get_attribute("href")
        })
        
    print(results_list)
    print("done succesfully")

finally:
    # Stop the driver
    driver.quit()    
