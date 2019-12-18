from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#export PATH=$PATH:P:\proyectos-pycharm\drivers\firefox\geckodriver.exe'

url =  'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

url2 =  'https://www.google.com'

firefox_driver = webdriver.Firefox(executable_path=r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')

