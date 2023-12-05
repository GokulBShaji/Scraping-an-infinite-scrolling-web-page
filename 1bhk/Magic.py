from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd


df = pd.DataFrame()

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()

browser = webdriver.Chrome(service=service, options=options)

browser.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=1&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName=Hyderabad')
sleep(5)
previous_height = browser.execute_script('return document.body.scrollHeight')


while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    sleep(5)

    new_height = browser.execute_script('return document.body.scrollHeight')
    if new_height == previous_height :
        break
    previous_height = new_height

    element_1 = browser.find_elements(By.XPATH, '//h2')
    sleep(2)
    Name = []
    for element in element_1:
        Name.append(element.text)


    element_2 = browser.find_elements(By.CSS_SELECTOR, '.mb-srp__card__price--amount')
    sleep(2)
    price = []
    for element in element_2:
        price.append(element.text)

    element_3 = browser.find_elements(By.CSS_SELECTOR, '.mb-srp__card__info')
    sleep(2)
    test = []
    for element in element_3:
        test.append(element.text)


print(test)
print(len(test))

df['Detail'] = test
df['Name']   = Name
df['Price']  = price

df.to_excel('1BHK_Database.xlsx', index=False)

sleep(7)
browser.quit()