# imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time


options = Options()
options.add_argument('--ignore-certificate-errors')
#options.add_argument('--kiosk')
#options.add_argument('--incognito')
#options.add_argument('--headless')


# open webpage
driver = webdriver.Chrome("I:/SELENIUM_REPO/CHROME_DRIVER/chromedriver.exe", options =options)
driver.get("https://www.costco.com/breakfast.html?currentPage=1&pageSize=96&sortBy=BestMatch&zipCode=02109")


zip_code_input_box_check = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,'deliveryPostalCode')))

zip_code_input_box = driver.find_element_by_name("deliveryPostalCode")
zip_code_input_box.clear()
zip_code_input_box.send_keys("01754")


element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'postal-code-submit')))
element.click()


delay = 20 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'search-results')))
    print("Page is ready!")
    with open("I:/PYTHON_WORKSPACE/OFFICE/MAR_2019/TEXT_DOC_POC/spider/data/page_source.html", "w",
              encoding='utf-8') as f:
        f.write(driver.page_source)
except TimeoutException:
    print("Loading took too much time!")





#submit_ele = driver.find_element_by_xpath("//button[@data-test='submitButton']")
#time.sleep(2)
#submit_ele.click()
#goto_costco_grocery_page = driver.find_element_by_name("postal-code-backToHome")
#goto_costco_grocery_page.click()


#driver.quit()
