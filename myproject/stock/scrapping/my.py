import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select


import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.debian.binary-package")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/PDF")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/Document")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/File")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/PDF")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/Archive")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/binary,application/octet-stream")

fp.set_preference("browser.download.panel.shown", False)
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
# prefs = {'profile.default_content_settings.popups': 0}
# fp.set_preference("browser.download.manager.useWindow", False)


# binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
# fp = (r'C:\Users\username\AppData\Roaming\Mozilla\Firefox\Profiles\oqmqnsih.default')
# opts = Options()
# opts.profile = fp
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# driver = webdriver.Firefox(capabilities=firefox_capabilities,firefox_binary=binary, firefox_options = opts)


# 
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
# # fp.set_preference("browser.download.manager.useWindow", False)
# # fp.set_preference("browser.download.manager.alertOnEXEOpen", False)





driver = webdriver.Firefox(executable_path = './geckodriver', firefox_profile=fp)
URL = 'https://www.skype.com/en/get-skype/'
# URL = 'https://www.geeksforgeeks.org/'
page = driver.get(URL)
driver.find_element_by_xpath('/html/body/form/div[5]/section/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div/span/span[1]/a').click()
