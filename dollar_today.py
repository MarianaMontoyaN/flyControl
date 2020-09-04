'''
Written in Python 3.7 using Selenium

Function that scrapes the web to update the value of the dollar
Returns a float value
'''

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def dollar_today_scrap():

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get('https://www.google.com/')

    search_field = driver.find_element_by_name('q')
    search_field.clear()

    search_field.send_keys('dolar a pesos colombianos')
    search_field.submit()

    dollar_today = float(driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr[3]/td[1]/input').get_attribute('value'))
    
    driver.quit()

    return dollar_today

