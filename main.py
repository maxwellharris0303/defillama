from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

urls = []

with open('urls.txt', 'r') as file:
    lines = file.readlines()
    
# Print each line
for line in lines:
    urls.append(line.strip())
    
print(urls)

for url in urls:
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"sc-289dd4cb-6 hmzJJz\"]"))).click()
        url_parent = driver.find_element(By.CSS_SELECTOR, "div[class=\"sc-289dd4cb-6 hmzJJz\"]")
        a_links = url_parent.find_elements(By.TAG_NAME, "a")
        for a_link in a_links:
            url = a_link.get_attribute('href')
            print(url)
            file_name = ""
            if "twitter" in url:
                file_name = 'twitter_urls.txt'
            else:
                file_name = 'website_urls.txt'
                
            with open(file_name, 'a') as file:
                file.write(url + "\n")
    except:
        pass
