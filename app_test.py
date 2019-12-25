from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from funtions import openFirefoxWebs, openChromePhone, openWeb,log_in
from dashlet import Dashlet



chrome_driver = webdriver.Chrome(r'P:\proyectos-pycharm\drivers\chrome\chromedriver.exe')

openWeb(chrome_driver, 'http://nts.neutrona.com/')
log_in(chrome_driver,     {'url':   'http://nts.neutrona.com/',
     'user': 'adrian.leon',
     'password': 'Neutrona1',
     'user_field': 'User',
     'pass_field': 'Password',
     'button': 'CallForAction'})

chrome_driver.implicitly_wait(10)
#page = len(chrome_driver.find_elements_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody/tr'))

dashlet = Dashlet(chrome_driver)


dashlet.get_all_results()
print(dashlet.tickets)







"""

print(len(tickets[0]))

for i in range(len(tickets[0])):
     print(tickets[0][i+1]['TN#'])
     print()

"""







