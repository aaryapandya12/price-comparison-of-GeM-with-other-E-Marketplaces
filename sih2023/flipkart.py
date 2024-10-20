from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import sys

def get_flipkart_price(product_name):
    service = Service(executable_path=r'c:\Users\AARYA\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe')
    
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.flipkart.com")
        
        # driver.set_window_size(1024, 600)
        # driver.maximize_window()

        try:
            close_button = driver.find_element("css selector","button._2KpZ6l._2doB4z")
            close_button.click()
        except NoSuchElementException:
            pass  

        time.sleep(10)
        search_bar = driver.find_element("name","q")
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.RETURN)

        time.sleep(10)

        try:
            price = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[3]/div/div[1]').text.replace('₹','').replace(',','')
        except:
            price = driver.find_element('css selector','._1_WHN1').text.replace('₹','').replace(',','')
        product_url = driver.current_url
        print(f"Price of '{product_name}': ₹{price}")

    except (NoSuchElementException, ElementClickInterceptedException) as e:
        print("Error occurred.")
        print(e)
    finally:
        driver.quit()

try:
    get_flipkart_price(sys.argv[1])
except:
    get_flipkart_price(sys.argv)

    

    
