import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select


import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.panel.shown", False)
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
# prefs = {'profile.default_content_settings.popups': 0}
fp.set_preference("browser.download.manager.useWindow", False)


# binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
# fp = (r'C:\Users\username\AppData\Roaming\Mozilla\Firefox\Profiles\oqmqnsih.default')
# option = Options()
# opts.add_argument("--headless")
# opts.profile = fp
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# driver = webdriver.Firefox(capabilities=firefox_capabilities,firefox_binary=binary, firefox_options = opts)


# 
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
# # fp.set_preference("browser.download.manager.useWindow", False)
# # fp.set_preference("browser.download.manager.alertOnEXEOpen", False)



options = webdriver.FirefoxOptions()
options.set_preference("dom.webnotifications.serviceworker.enabled", False)
options.set_preference("dom.webnotifications.enabled", False)
options.add_argument('--headless')

driver = webdriver.Firefox(capabilities=firefox_capabilities,options = options, executable_path = './geckodriver')
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
