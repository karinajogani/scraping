from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import json

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
driver.implicitly_wait(3)
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("iphone")
driver.find_element(By.ID, "nav-search-submit-button").click()

data_list = []

for page in range(1, 21):
    page_url = "https://www.amazon.in/s?k=iphone&page=" +str(page)
    driver.get(page_url)
    driver.implicitly_wait(5)

    urls = []
    models = driver.find_elements(By.XPATH, ".//a[@class='a-link-normal s-no-outline']")
                                   
    for i in range(len(models)):
        urls.append(models[i].get_attribute("href"))
    # print(urls)
    # print(len(urls))

    for url in urls:
        driver.get(url)
        try:
            data_dict = {
                'name' : driver.find_element(By.XPATH, ".//span[@id='productTitle']").text,
                'star' : driver.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text,
                'rating' : driver.find_element(By.XPATH, ".//span[@id='acrCustomerReviewText']").text,
                'discount' : driver.find_element(By.XPATH, ".//span[@class='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage']").text,
                'price' : driver.find_element(By.XPATH,".//span[@class='a-price-whole']").text,
                'EMI' : driver.find_element(By.XPATH, ".//div[@id='inemi_feature_div']").text,
                'color' : driver.find_element(By.XPATH, ".//span[@class='selection']").text,
                'size' : driver.find_element(By.XPATH, ".//p[@class='a-text-left a-size-base']").text,
                'details' : driver.find_element(By.XPATH, ".//table[@class='a-normal a-spacing-micro']").text.replace('\n', ', '),
                'about' : driver.find_element(By.XPATH, ".//div[@id='feature-bullets']").text.replace('\n', ', '),
            }
            data_list.append(data_dict)
        except NoSuchElementException:
            pass
        driver.implicitly_wait(5)

with open('a_data.json', 'w') as file:
    json.dump(data_list, file, indent=4)

driver.close()

# all_data = driver.find_element(By.XPATH, ".//div[@id='centerCol']")
