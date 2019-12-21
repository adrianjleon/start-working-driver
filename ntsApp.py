from selenium import webdriver
from funtions import openFirefoxWebs, openChromePhone
from database import webs


chrome_driver = webdriver.Chrome(r'P:\proyectos-pycharm\drivers\chrome\chromedriver.exe')
firefox_driver = webdriver.Firefox(executable_path=r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')
openFirefoxWebs(firefox_driver, webs)



openChromePhone(chrome_driver, webs[3])




