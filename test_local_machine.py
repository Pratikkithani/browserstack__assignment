from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Function to perform the required tasks on flipkart.com
def run_test(driver):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    # Search for the product
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Samsung Galaxy S10")
    search_box.send_keys(Keys.RETURN)

    # Click on "Mobiles" in categories
    mobiles_category = driver.find_element(By.LINK_TEXT, "Mobiles")
    mobiles_category.click()

    #clicking on samsung
    time.sleep(2)
    brand = driver.find_element(By.CLASS_NAME,"_3879cV")
    time.sleep(2)
    brand.click()

    #clicking on assured
    flipkart_assured_filter = driver.find_element(By.CLASS_NAME,"_3U-Vxu")
    time.sleep(2)
    flipkart_assured_filter.click()

    # high ---> low
    price_high_to_low_option = driver.find_element(By.XPATH, "//div[text()='Price -- High to Low']")
    time.sleep(2)
    price_high_to_low_option.click()
    time.sleep(6)

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

    for result in results_list:
        print(result)
    driver.quit()


try:
    for i in range(1):  # Number of parallels
        driver = webdriver.Chrome()
        run_test(driver)
except Exception as e:
    print(f"Error: {e}")





#http://localhost:8080/