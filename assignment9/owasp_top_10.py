import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import json 
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_owasp_top_ten_data(url):

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Enable headless mode
    options.add_argument('--disable-gpu')  # Optional, recommended for Windows
    options.add_argument('--window-size=1920x1080')  # Optional, set window size
    driver = webdriver.Chrome()
    results = []
    try:
        driver.get(url)
        h2_element = driver.find_element(By.CSS_SELECTOR,'h2[id="top-10-web-application-security-risks"]')
        if(h2_element):
            ul_element = h2_element.find_element(By.XPATH,'following-sibling::ul')
            if(ul_element):
                li_elements_for_top_10_volnurabilities = ul_element.find_elements(By.CSS_SELECTOR,'li')
                if li_elements_for_top_10_volnurabilities:
                    for li_element in li_elements_for_top_10_volnurabilities:
                        link = li_element.find_element(By.TAG_NAME, 'a')
                        if link:
                            url = link.get_attribute('href')
                            title = link.text
                            vulnerability_dict = {'Title': title, 'URL': url}
                            results.append(vulnerability_dict)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
    return results

if __name__ == "__main__":
    owasp_url = "https://owasp.org/www-project-top-ten/"
    extracted_data = extract_owasp_top_ten_data(owasp_url)
    if extracted_data:
        for item in extracted_data:
            print(f"Title: {item['Title']}")
            print(f"URL: {item['URL']}\n")
            df = pd.DataFrame(extracted_data)
            df.to_csv('./owasp_top_10.csv', sep=' ')
    else:
        print("No data extracted.")