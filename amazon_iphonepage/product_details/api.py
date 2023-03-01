from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
driver.implicitly_wait(3)
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("iphone")
driver.find_element(By.ID, "nav-search-submit-button").click()

data = []

for page in range(1, 21):
    page_url = "https://www.amazon.in/s?k=iphone&page="+str(page)
    driver.get(page_url)
    driver.implicitly_wait(3)

    urls = []
    models = driver.find_elements(By.XPATH, ".//a[@class='a-link-normal s-no-outline']")

    for i in range(len(models)):
        urls.append(models[i].get_attribute("href"))

    for url in urls:
        driver.get(url)
        try:
            dict1 = {
                'price' : driver.find_element(By.XPATH, ".//span[@class='a-price-whole']").text,
            }
            data.append(dict1)
        except NoSuchElementException:
            pass

with open('price_data.json', 'w') as file:
    json.dump(data, file, indent=4)

driver.close()
