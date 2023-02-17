from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import json

data_list = []
for page in range(1, 21):
    # page_= page + 1
    page_url = "https://www.amazon.in/s?k=iphone&page="+ str(page)
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Navigate to a webpage
    driver.get(page_url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    all_products = driver.find_elements(By.XPATH,"//div[@data-component-type='s-search-result']")
    driver.implicitly_wait(4)
    for product in all_products:
        try:
            data_dict ={
                'model_name' : product.find_element(By.XPATH,".//span[@class='a-size-medium a-color-base a-text-normal']" ).text,
                'price' : product.find_element(By.XPATH,".//span[@class='a-price-whole']").text,
            }
            data_list.append(data_dict)
        except NoSuchElementException:
            pass
          
    with open('p_data.json', 'w') as file:
        json.dump(data_list, file, indent=4)

    driver.close()


# Open a Chrome browser instance
# driver = webdriver.Chrome()
# search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# search_box.clear()
# search_box.send_keys("iphone")
# driver.find_element(By.ID, "nav-search-submit-button").click()  

# phone_names = []
# phone_price = []

# print(len(all_products))
# for product in all_products:

#     names = product.find_elements(By.XPATH,".//span[@class='a-size-medium a-color-base a-text-normal']" )
#     for name in names:
#         phone_names.append(name.text)

#     prices = product.find_elements(By.XPATH,".//span[@class='a-price-whole']")
#     for price in prices:
#         phone_price.append(price.text)

# print('names====>', len(phone_names))
# print('price====>', len(phone_price))

# with open('p_data.json', 'w') as file:
#         json.dump(phone_names, file, indent=4)

# # Close the browser
# driver.close()
