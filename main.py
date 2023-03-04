import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from bs4 import BeautifulSoup

print("-------------Amazon Product Scraper--------------")
product = input("Enter product name: ")
no_of_pages = int(input("Enter the number of pages to scrape: "))

PATH = "C:\Program Files (x86)\chromedriver.exe"



products = []
prices_list =[]
titles_list = []
urls_list = []
ratings_list =[]
reviews_list =[]
count = 0
browser = webdriver.Chrome(executable_path=PATH)
browser.get('https://www.amazon.in/')
WebElement = browser.find_element(By.ID,"twotabsearchtextbox")
WebElement.send_keys(product)
searchButton = browser.find_element(By.ID,"nav-search-submit-button")
searchButton.click()

while True:

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
                reviews = reviews.replace("(","")
                reviews = reviews.replace(")","")
                reviews_list.append(reviews)
                titles_list.append(title.get_text())
                urls_list.append(url)
                prices_list.append(price.get_text())
    count +=1 
    print("Scrapping Page :",count)
    if count == no_of_pages:
        break
    
    pagination = browser.find_element_by_xpath("//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
 
    pagination.click()
    sleep(10)

    
   

  

amazon_data = pd.DataFrame(
    {'URL': urls_list,
     'Title': titles_list,
     'Price': prices_list,
     'Rating':ratings_list,
     'No_of_reviews':reviews_list
    })

sleep(2)

amazon_data.to_csv(f'amazon {product} scrapped data.csv')
browser.quit()



