from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time

def flipkart_price_checker(): 
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Time: ", current_time)
    print("Connecting to flipkart...")
    driver = webdriver.Firefox()
    driver.get("https://www.flipkart.com/jbl-c50hi-wired-headset/p/itm3b56d7f9439d3?pid=ACCFAMFQGCNEB8HM&lid=LSTACCFAMFQGCNEB8HMS8U8KK&marketplace=FLIPKART&srno=b_1_2&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_3.dealCard.OMU_Deals%2Bof%2Bthe%2BDay_AGHS7TNZN436_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&fm=neo%2Fmerchandising&iid=fb8c056a-f992-4577-bef4-4825ffa15570.ACCFAMFQGCNEB8HM.SEARCH&ppt=browse&ppn=browse&ssid=g4fyxruwds0000001596122648220")
    r = driver.page_source
    soup = BeautifulSoup(r, 'html.parser')
    print("Fetching price...")
    #js_test tracks the price
    js_test = soup.find('div', attrs={'class':'_1vC4OE _3qQ9m1'})
    print(js_test.text)
    
while True: 
    flipkart_price_checker()
    print("Will fetch again after 1 minute. To stop press ctl + c...")
    time.sleep(60)