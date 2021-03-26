import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path = 'geckodriver')
URL = 'https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx'
# URL = 'https://www.geeksforgeeks.org/'
page = driver.get(URL)
driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/span/label').click()
# dropdown option
#  dd                                         mm                              yy 
# //*[@id="ContentPlaceHolder1_fdate1"]    //*[@id="ContentPlaceHolder1_fmonth1"]   //*[@id="ContentPlaceHolder1_fyear1"]

# Date
selectDate= Select(driver.find_element_by_id('ContentPlaceHolder1_fdate1'))
# select by visible text
selectDate.select_by_visible_text('25')
# Month
selectMonth = Select(driver.find_element_by_id('ContentPlaceHolder1_fmonth1'))
# select by visible text
# selectMonth.select_by_visible_text('Mar')
# selectMonth.select_by_visible_value('3')
selectMonth.select_by_index(3)
# Year
selectYear = Select(driver.find_element_by_id('ContentPlaceHolder1_fyear1'))
# select by visible text
selectYear.select_by_visible_text('2021')
##  Submit   //*[@id="ContentPlaceHolder1_btnSubmit"]

driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnSubmit"]').click()
driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnHylSearBhav"]').click()

## click          //*[@id="ContentPlaceHolder1_btnHylSearBhav"]
from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("browser.download.folderList",2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","/data")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream, application/zip")
driver = webdriver.Firefox(firefox_options=options)
# print(page)