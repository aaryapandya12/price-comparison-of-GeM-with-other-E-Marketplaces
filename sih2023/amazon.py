from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import sys
from pyvirtualdisplay import Display # type: ignore


def get_amazon_price(product_name):
    # Path to GeckoDriver 
    service = Service(executable_path=r'c:\Users\AARYA\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe')
    
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)


    try:
        # Open Amazon.in
        driver.get("https://www.amazon.in")
        
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        time.sleep(5)
        # Find the search bar, enter the product name, and submit
        search_bar = driver.find_element('id','twotabsearchtextbox')
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.RETURN)

        # Wait for the page to load()
        time.sleep(5)

        # Find and print the price of the first product in search results
        price = driver.find_element('css selector','.a-price-whole').text.replace('₹','').replace(',','')
        product_url = driver.current_url
        print(f"Price of '{product_name}': ₹{price}")

    except NoSuchElementException as e:
        print("Error: Element not found.")
        print(e)
    finally:
        # Close the browser
        driver.quit()

# Example usage
try:
    get_amazon_price(sys.argv[1])
except:
    get_amazon_price(sys.argv)

    
   