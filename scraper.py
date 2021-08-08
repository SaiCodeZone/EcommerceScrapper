import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
import plot
    
    
#loading the web driver
driver= webdriver.PhantomJS('phantomjs')
#storing all the results in single list to store it in csv file
results=[]

#scraping data from flipkart
def print_flipkart(products,price,links):
    products = products[0:10]
    price = price[0:10]
    links=links[:10]
    #print(products)
    #print(links)
    #cleaning the price format
    prices=[]
    for p in price:
        pri=p.text
        pri=pri[1:]
        prices.append(pri.replace(',',''))
    #print(prices)
    Source="Flipkart"
    Flipkart_results = []
    number=1
    for item, money, link in zip(products, prices,links):
        count="F"+str(number)
        Flipkart_results.append([count,item.text, money, Source, link])
        number=number+1
    #print(Flipkart_results)
    print(tabulate(Flipkart_results, headers=["S.no","Product on Flipkart", "Price", "source","product link"], tablefmt="fancy_grid"))
    for row in Flipkart_results:
        results.append(row)


def scrapeFlipkart(url):
    try:
        driver.set_page_load_timeout(20)
        driver.get(url)
        products = driver.find_elements_by_css_selector("._2cLu-l")
        price = driver.find_elements_by_css_selector("._1vC4OE")
        links = driver.find_elements_by_css_selector("._2cLu-l")
        product_links=[link.get_attribute('href') for link in links]
        if (len(products) > 0 and len(price) > 0):
            print_flipkart(products,price,product_links)
        else:
            products = driver.find_elements_by_css_selector("._3wU53n")
            price = driver.find_elements_by_css_selector("._1vC4OE._2rQ-NK")
            links = driver.find_elements_by_css_selector("._31qSD5")
            product_links=[link.get_attribute('href') for link in links]
            if(len(products) > 0 and len(price) > 0):
                print_flipkart(products,price,product_links)
            else:
                products=driver.find_elements_by_css_selector("._2mylT6")
                price=driver.find_elements_by_css_selector("._1vC4OE")
                links=driver.find_elements_by_css_selector("._3dqZjq")
                product_links=[link.get_attribute('href') for link in links]
                if(len(products)>0 and len(price)>0):
                    print_flipkart(products,price,product_links)
                else:
                    print("Flipkart does not sell this product\n")
    except Exception as e:
        print("An error occured while loading the webpage. ",e)
    finally:
        driver.close()


#scraping data from snapdeal
def scrapeSnapdeal(url):
    try:
        source = requests.get(url).content
        soup = BeautifulSoup(source, 'html.parser')
        products = soup.find_all("p", class_= "product-title")
        price = soup.find_all("span", class_= "lfloat product-price")
        produt_sections=soup.select(".product-desc-rating ")
        product_links=[]
        for section in produt_sections:
            link_section=section.find_all('a')
            for a in link_section:
                link=a.get('href')
                product_links.append(link)
        #print(product_links)
        if(len(products)>0 and len(price)>0):
            products = products[0:10]
            price = price[0:10]
            product_links=product_links[:10]
            source="snapdeal"
            #print(links)

            #cleaning the price format
            prices=[]
            for p in price:
                pri=p.text
                pri=pri[3:]
                prices.append(pri.replace(',',''))
            #print(prices)
            Snapdeal_results = []
            number=1
            for item, money, link in zip(products, prices, product_links):
                count="S"+str(number)
                Snapdeal_results.append([count,item.string, money, source, link])
                number=number+1
            print(tabulate(Snapdeal_results, headers=["S.no","Product on Snapdeal", "Price", "source", "product link"], tablefmt="fancy_grid"))
            for row in Snapdeal_results:
                results.append(row)
        else:
            print("SnapDeal does not sell this product.")
    except Exception as e:
        print("An error occured while loading the webpage. ",e)


def startScraping(query,filename):

    #reading urls
    flipkart_url = 'https://www.flipkart.com/search?q='
    snapdeal_url = 'https://www.snapdeal.com/search?keyword='
    #reading keyword through stdin  
    keyword = query.split()
    #print(query)
    #print(keyword)
    #print(filename)

    #for adding search query to url
    for word in keyword:
        flipkart_url+=word+"%20"
        snapdeal_url+=word+"%20"

    #removing the + and %20 at the end of url.
    flipkart_url = flipkart_url[:-3]
    snapdeal_url = snapdeal_url[:-3]

    #print(flipkart_url)
    #print(snapdeal_url)

    

    #calling scrapers
    scrapeSnapdeal(snapdeal_url)
    scrapeFlipkart(flipkart_url)

    #printing all the data for debugging purpose
    #print(results)

    #field names
    fields=['S.no','Product Name','Price','Source','product link']

    #writing the data to the file
    with open(filename,'w',encoding="UTF8") as csvfile:
        #creating csv writer object
        csvwriter=csv.writer(csvfile)
        #writing the fields
        csvwriter.writerow(fields)
        #writing data
        csvwriter.writerows(results)

    plot.plotResults(filename)

