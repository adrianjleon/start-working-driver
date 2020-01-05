from selenium import webdriver
from funtions import openFirefoxWebs, openChromePhone, openWeb, log_in, operadoresPresentes
from dashlet import Dashlet
from database import webs, todosoperadores
from ticket import Ticket
import sys


operadoresPresentes = operadoresPresentes(sys.argv)



#CHORME PART
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# chrome_driver = webdriver.Chrome(options=chrome_options, executable_path=r'P:\proyectos-pycharm\drivers\chrome\chromedriver.exe')
# openChromePhone(chrome_driver, webs[5])

#FIREFOX PART
# firefox_driver = webdriver.Firefox(executable_path=r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')
# openFirefoxWebs(firefox_driver, webs)
# firefox_driver.switch_to.window(firefox_driver.window_handles[0])

#FIREFOX TEST PART
firefox_driver = webdriver.Firefox(executable_path=r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')
openWeb(firefox_driver, 'http://nts.neutrona.com/')
log_in(firefox_driver, webs[0])


#TICKET MANAGEMENT

dashlet = Dashlet(firefox_driver)

dashlet.get_all_results()

dataTickets = dashlet.tickets

ticket = Ticket(dataTickets, operadoresPresentes)

ticket.separaTicketsPorQueue()

ticket.asignarTicketsPorQueue()

print(ticket.operators)



