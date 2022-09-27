
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from set_variables import ChromeDriver_Location

class contract():

    def __init__(self,contractaddress):
        self.contractaddress = contractaddress
        self.tokenurl = "https://etherscan.io/token/" + str(contractaddress)

        self.driver = webdriver.Chrome(ChromeDriver_Location)
        self.driver.get(self.tokenurl)

        iframe = self.driver.find_element(By.TAG_NAME,"iframe")

        self.table_url = iframe.get_attribute('src')[:-1]

        print(self.table_url)

    
    def get_transactions(self,page_factor):

        #first we get total pages:
        self.driver.get(self.table_url + "1")

        total_pages_tab = self.driver.find_element(By.CSS_SELECTOR,"span.page-link.text-nowrap")
        tab_html = total_pages_tab.get_attribute('innerHTML')

        tab_soup = BeautifulSoup(tab_html,"html.parser")

        tab_contents = tab_soup.find_all("strong")
        self.total_pages = int(tab_contents[1].text)

        self.txn_ids = []

        for i in range(1,round(self.total_pages*page_factor)):
            self.driver.get(self.table_url + str(i))

            

            transactions = self.driver.find_elements(By.CSS_SELECTOR,"span.hash-tag.text-truncate.myFnExpandBox_searchVal")

            for j in transactions:
                innerHTML = j.get_attribute('innerHTML')
                soup = BeautifulSoup(innerHTML,"html.parser")
                a = soup.find("a")
                self.txn_ids.append(a.text)

    def quit(self):
        self.driver.quit()