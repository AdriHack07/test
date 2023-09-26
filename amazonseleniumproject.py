from re import search
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\Users\adrie\Google Drive\Documents\Development\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://www.amazon.de/")

input_search = driver.find_element_by_id("twotabsearchtextbox")
input_search.send_keys("Smartphone", "\n")
sleep(5)
current_page = 0

products = []
for i in range(10):
    print("Scraping page ", i + 1)
    product = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
    for p in product:
        products.append(p.text)
    print(products)
    next_page_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator')]")))
    driver.execute_script("arguments[0].click();", next_page_button)
    current_page += 1
    print("current page: ", current_page)


# Problem: Can't press to the next page