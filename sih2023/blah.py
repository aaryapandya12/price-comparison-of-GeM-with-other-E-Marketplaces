from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_flipkart(product_name):
    service = Service(executable_path=r'c:\Users\AARYA\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe')
    options = Options()
    driver = webdriver.Chrome(service = service , options = options)
    
    try:
        driver.get("https://www.flipkart.com")
        driver.maximize_window()
        
        search_bar = driver.find_element("name","q")
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.RETURN)
        
    except(NoSuchElementException, ElementClickInterceptedException) as e:
        print("Error Occurred")
        print(e)
    finally:
        driver.quit()

get_flipkart("teddy bear")
        
            
        
            

