# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

PATH = "C:\Program Files (x86)\chromedriver.exe"




# def launchBrowser():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach",True)
#     driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1")
#     driver.implicitly_wait(30)
#     print(driver.title)
#     search = driver.find_elements(By.CLASS_NAME,"a-size-medium a-color-base a-text-normal")
#     print(search)
#     driver.quit()

# driver = launchBrowser()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.page_load_strategy = 'eager'
# driver = webdriver.Chrome(PATH,options=options)
# driver.get("https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1")
# search = driver.find_elements(By.CLASS_NAME,"a-size-medium a-color-base a-text-normal")
# print(search)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# service = ChromeService(executable_path=PATH)
# driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1")
# search = driver.find_elements(By.CLASS_NAME,"a-size-mini a-spacing-none a-color-base s-line-clamp-2")

# print(search)
# driver.quit()

# from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(PATH,options=options)

# driver.get("https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1")
# search = driver.find_element(By.CLASS_NAME,"a-size-medium a-color-base a-text-normal")

# print(search)
# driver.quit()

import pandas as pd

from selenium import webdriver
from time import sleep
# import requests
from bs4 import BeautifulSoup

# URL = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")
products = []
prices_list =[]
titles_list = []
urls_list = []
ratings_list =[]
reviews_list =[]
browser = webdriver.Chrome(executable_path=PATH)
for page in range(1,21):
    browser.get(f'https://www.amazon.in/s?k=bags&page={page}crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{page}')

    browser.maximize_window()

    pageSource = browser.page_source
    soup = BeautifulSoup(pageSource, "html.parser")
    content = soup.find_all(attrs={'data-component-type':'s-search-result'})


    for eachContent in content:
        title = eachContent.find('span','a-size-medium a-color-base a-text-normal')
        price = eachContent.find('span','a-price-whole')
        url = eachContent.find('a','a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        divs = eachContent.find('div','a-section a-spacing-none a-spacing-top-micro')
        if divs and title and price and url:
            url_link = url.get('href')
            url = "https://www.amazon.in"+url_link
            ratings = divs.find('span')
            reviews = divs.find('span','a-size-base s-underline-text')
            if ratings and reviews:
                ratings_list.append(ratings.get_text())
                reviews = reviews.get_text()
                reviews_list.append(reviews)
                titles_list.append(title.get_text())
                urls_list.append(url)
                prices_list.append(price.get_text())

    
    # print(reviews.get_text())
    # for rate in ratings:
    #     print(rate.get_text())
    # for rate in ratings:
    #     print(rate.get('aria-label'))
    # rating = ratings.get('aria-label')
    # print(rating)
    
    
    # products.append([url,title.get_text(),price.get_text(),ratings.get_text(),reviews])
    
    # ratings_list.append(ratings.get_text())
    
#     count+=1 
# print(products)
# print(count)
# print('Scraping page', 1)
# count = 0
# sections = browser.find_elements_by_xpath("//div[@data-component-type='s-search-result']")
# links = browser.find_elements_by_xpath("//a[@class='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
# for link in links:
#     print(link.get_attribute("href"))
#     count+=1
# for section in sections:
#     title = section.find_element_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
#     price = section.find_element_by_xpath("//span[@class='a-price-whole']")
#     link = section.find_element_by_xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")
#     urls = section.find_element_by_xpath("//a[@class='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
#     print(section.text,link.get_attribute("href"),urls.get_attribute("href"))
#     count+=1
#     headings = section.find_elements_by_xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")
#     prices_Section = section.find_elements_by_xpath("//div[@class='a-row a-size-base a-color-base']")
    
    

# for url in headings:
#     titles = url.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
#     urls_list.append(url.get_attribute("href"))
# for url in prices_Section :
#     prices = url.find_elements_by_xpath("//span[@class='a-price-whole']")
# for price in prices:
#     prices_list.append(price.text)
# for title in titles:
#     titles_list.append(title.text)

# print(count)
# product = browser.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
# url = browser.find_elements_by_xpath("//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
# price = browser.find_elements_by_xpath("//span[@class='a-price-whole']")
# prices =[]
# for p in product:
#     prices.append(p.text)
# for p in price:
#     prices.append(p.text)


# for p in url :
#     products.append(p.text)

  
# list3 = [item for sublist in zip(titles_list,prices_list) for item in sublist]
amazon_data = pd.DataFrame(
    {'URL': urls_list,
     'Title': titles_list,
     'Price': prices_list,
     'Rating':ratings_list,
     'No_of_reviews':reviews_list
    })

sleep(2)
# print(products)
# print(products)
# print(prices)
# print(len(prices),len(products))
# print(len(prices_list))
# print(len(titles_list))
# print(len(urls_list))
# print(percentile_list)
# print(amazon_data)
amazon_data.to_csv('file_name.csv')
browser.quit()



