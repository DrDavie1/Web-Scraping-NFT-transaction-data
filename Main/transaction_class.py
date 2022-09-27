from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from set_variables import ChromeDriver_Location

import time

from Functions.conversion_functions import *



class txns():

    def __init__(self,ids):
        self.ids_S = ids
        self.ids = []
        self.newIDs = []

        for i in self.ids_S:
            if i not in self.ids:
                self.ids.append(i)

        self.driver = webdriver.Chrome(ChromeDriver_Location)

        self.values_eth = []
        self.values_dollar = []
        self.dates = []
        self.times = []
        self.tokenIDs = []

        for i in self.ids:
            time.sleep(0.05)
            url = "https://etherscan.io/tx/" + str(i)
            self.driver.get(url)
            
            # we need to catch errors if any elements aren't found:

            #price

            try:
                search_price_element = self.driver.find_element(By.XPATH,'//span[@id="ContentPlaceHolder1_spanValue"]')
                price_element = search_price_element.text

                eth_price,dollar_price = convert_etherscan_price(price_element)



                if float(eth_price) > 0:
                    self.values_eth.append(float(eth_price))
                    self.values_dollar.append(dollar_price)

                    #date and time

                    try:
                        search_date_element = self.driver.find_element(By.XPATH,'//span[@id="clock"]/..')
                        datetime_element = search_date_element.text

                        date_i,time_i = convert_etherscan_date(datetime_element)
                    except:
                        date_i,time_i = "Not Found","Not Found"

                    #tokenID

                    try:
                        search_tokenID_element = self.driver.find_element(By.XPATH,'//li[@class="media align-items-baseline mb-2 ml-2"]')
                        token_element = search_tokenID_element.text

                        tokenID = convert_etherscan_id(token_element)
                    
                        
                    except:
                        tokenID = "Not Found"


                    self.dates.append(date_i)
                    self.times.append(time_i)
                    self.tokenIDs.append(tokenID)
                    self.newIDs.append(i)

            except:
                eth_price,dollar_price = "Not Found","Not Found"
                



    def quit(self):
        self.driver.quit()

