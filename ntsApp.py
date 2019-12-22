from selenium import webdriver
from funtions import openFirefoxWebs, openChromePhone, openWeb
from database import webs

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

chrome_driver = webdriver.Chrome(options=chrome_options, executable_path=r'P:\proyectos-pycharm\drivers\chrome\chromedriver.exe')
openChromePhone(chrome_driver, webs[5])


firefox_driver = webdriver.Firefox(executable_path=r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')
openFirefoxWebs(firefox_driver, webs)

firefox_driver.switch_to.window(firefox_driver.window_handles[0])










