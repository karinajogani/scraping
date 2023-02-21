from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import json

# page_url = "https://www.amazon.in/"/
# driver = webdriver.Chrome()


data_list = []
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("iphone")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.get("https://www.amazon.in/Apple-iPhone-13-128GB-Starlight/dp/B09G9D8KRQ/ref=sr_1_1_sspa?crid=1W9XFXAT0LSY1&keywords=iphone&qid=1676963246&sprefix=iphone%2Caps%2C287&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
all_data = driver.find_elements(By.XPATH, "//div[@id='centerCol']")
for data in all_data:
    try:
        data_dict = {
            'name' : data.find_element(By.XPATH, ".//span[@id='productTitle']").text,
            'star' : data.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text,
            'rating' : data.find_element(By.XPATH, ".//span[@id='acrCustomerReviewText']").text,
            'discount' : data.find_element(By.XPATH, ".//span[@class='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage']").text,
            'price_with_discount' : data.find_element(By.XPATH, ".//span[@class='a-price-whole']").text,
            # 'real_price':data.find_element(By.XPATH, ".//span[@aria-hidden='true']").text,
            'EMI' : data.find_element(By.XPATH, ".//div[@id='inemi_feature_div']").text,
            'color' : data.find_element(By.XPATH, ".//span[@class='selection']").text,
            'size' : data.find_element(By.XPATH, ".//p[@class='a-text-left a-size-base']").text,
            'details' : data.find_element(By.XPATH, ".//table[@class='a-normal a-spacing-micro']").text.replace('\n', ', '),
            'about' : data.find_element(By.XPATH, ".//div[@id='feature-bullets']").text.replace('\n', ', '),
            'offers' : data.find_element(By.XPATH, ".//div[@class='celwidget']").text.replace('\n', ', '),
            # 'daily' : data.find_element(By.XPATH, ".//@span[@class='']").textx
        }
        data_list.append(data_dict)
    except NoSuchElementException:
        pass

    with open('a_data.json', 'w') as file:
        json.dump(data_list, file, indent=4)

    driver.close()