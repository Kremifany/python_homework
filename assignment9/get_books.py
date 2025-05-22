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

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

# Task 1: Review robots.txt to Ensure Policy Compliance
# try:
#     robots_url = " https://durhamcountylibrary.org/robots.txt"
#     driver.get(robots_url)
#     print(f"ROBOTS.TXT:\n{driver.page_source}")
# except Exception as e:
#     print(f"An error occurred during scraping: {e}")
# finally:
#     driver.quit()
#############################3
# Task 2,3: Understanding HTML and the DOM for the Durham Library Site,Write a Program to Extract this Data

SEARCH_RESULT_LI_TAG_NAME = "li"
SEARCH_RESULT_LI_CLASS = "row cp-search-result-item"

TITLE_TAG_NAME = "span"  # User needs to verify this (e.g., span, a, h2, h3, h4)
TITLE_CLASS = "title-content" # User needs to verify this

AUTHOR_TAG_NAME = "a" # Authors are typically links
AUTHOR_LINK_CLASS = "author-link" # User needs to verify this

FORMAT_YEAR_TAG_NAME = "span" # User needs to verify this
FORMAT_YEAR_SPAN_CLASS = "display-info-primary" 

def get_book_data(pageToScrape_url):
    try:
        driver.get(pageToScrape_url)
        time.sleep(5)
    except Exception as e:
        print(f"Error setting up WebDriver: {e}")
 
    results = []

    try:
        search_items = driver.find_elements(By.CSS_SELECTOR, f"{SEARCH_RESULT_LI_TAG_NAME}[class*='{SEARCH_RESULT_LI_CLASS}']")
        print(f"Found {len(search_items)} search result items.")            

        if not search_items:
            print(f"No search items found. Please check your selectors: ")
            print(f"  SEARCH_RESULT_LI_TAG_NAME: '{SEARCH_RESULT_LI_TAG_NAME}'")
            print(f"  SEARCH_RESULT_LI_CLASS: '{SEARCH_RESULT_LI_CLASS}' (check if it's a substring or needs full match)")


        for item in search_items:
            title = "N/A"
            author = "N/A"
            format_year = "N/A"

            # Get Title
            try:
                title_element = item.find_element(By.CSS_SELECTOR, f"{TITLE_TAG_NAME}[class*='{TITLE_CLASS}']")
                title = title_element.text.strip()
            except NoSuchElementException:
                print(f"Title not found for an item using class '{TITLE_CLASS}'.")

            # Get Author(s)
            try:
                author_elements = item.find_elements(By.CSS_SELECTOR, f"{AUTHOR_TAG_NAME}[class*='{AUTHOR_LINK_CLASS}']")
                if author_elements:
                    authors_list = [auth.text.strip() for auth in author_elements if auth.text.strip()]
                    author = "; ".join(authors_list) if authors_list else "N/A"
                else:
                    print(f"Author elements not found using class '{AUTHOR_LINK_CLASS}'.")
            except NoSuchElementException:
                print(f"Author not found for an item using class '{AUTHOR_LINK_CLASS}'.")

            # Get Format and Year
            try:
                format_year_element = item.find_element(By.CSS_SELECTOR, f"{FORMAT_YEAR_TAG_NAME}[class*='{FORMAT_YEAR_SPAN_CLASS}']")
                format_year = format_year_element.text.strip()
            except NoSuchElementException:
                print(f"Format-Year container or span not found using classes '{FORMAT_YEAR_SPAN_CLASS}'.")


            if title != "N/A" or author != "N/A" or format_year != "N/A":
                book_info = {
                    "Title": title,
                    "Author": author,
                    "Format-Year": format_year
                }
                results.append(book_info)
                print(f"Added: {book_info}") # For debugging each item
            else:
                print("Skipping an item as no information could be extracted.")
        books_df = pd.DataFrame(results)
        if not books_df.empty:
            print("\n--- Scraped Book Data ---")
            print(books_df)
        else:
            print("\nNo data was scraped. Please check the selectors and the website structure.")
            
    except Exception as e:
        print(f"An error occurred during scraping: {e}")

#TASK 4 Write out the Data
        books_df.to_csv('./get_books.csv', sep='')
        with open('get_books.json', 'w') as json_file:
            json.dump(results, json_file, indent=4)
    return results

if __name__ == "__main__":
    try:      
        driver.get(" https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart ")
        #for a single page:
        get_book_data(" https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart ")
        #for multiple pages:
        # results = []  
        # results.append(get_book_data(" https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart "))
        # while True:
        # # ... (scrape current page content) ...
        #     try:
        #         next_page_button = driver.find_element(By.CSS_SELECTOR, "[class='cp-link pagination-item__link']") 
        #         if "disabled" in next_page_button.get_attribute("class"): # Check if button is disabled class="cp-pagination-item pagination__next-chevron pagination-item--disabled"
        #             print("Next page button is disabled. Reached the last page.")
        #             break
        #         next_page_button.click()
        #         url_to_scrape = next_page_button.get_attribute("href")
        #         print(f"Navigating to the next page...{url_to_scrape}\n")
        #         results.append(get_book_data(url_to_scrape))
        #         time.sleep(5) # Wait for page to load  
        #    except Exception as e:
        #       print(f"Error clicking next page: {e}")   
        
  
    # Task 5: Ethical Web Scraping 
    except Exception as e:
        print(f"An error occurred during scraping: {e}")
    try:
        robots_url = "https://en.wikipedia.org/robots.txt"
        driver.get(robots_url)
        print(f"::::::::::::::::::::::::::::::::::::::::::::ROBOTS.TXT OF WIKIPEDIA IS::::::::::::::::::::::::\n{driver.page_source}")

    finally:
        driver.quit()





