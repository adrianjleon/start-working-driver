## crear/pedir los operadores del turno
# iterar los datos
##
##
##
##
##
#

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from funtions import openFirefoxWebs, openChromePhone
from dashlet import Dashlet
from database import webs

from dataSampleFromDashlet import dataTickets

def openWeb(driver, web):
    return driver.get(web)

#firefox_driver = webdriver.Firefox(executable_path=r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')

operadores = [
                 {'nombre': 'Adrian Leon', 'queue': 'Organico::NOC::Tier 1',  'tickets' :[] },
                 {'nombre': 'Augusto Cruz', 'queue': 'Organico::NOC::Tier 2', 'tickets' :[] },
                 {'nombre': 'Isaac Graterol', 'queue': 'Organico::NOC::Tier 3', 'tickets' :[] },
              ]


class Ticket:

    def __init__(self, tickets, operators):
        self.tickets = tickets
        self.operatos = operators
        self.queue = { 'Organico::NOC::Tier 1': [] ,
                       'Organico::NOC::Tier 2': [] ,
                       'Organico::NOC::Tier 3': [],
                       'Organico::NOC': [],}
        self.url = 'http://nts.neutrona.com/otrs/index.pl?;Action=AgentTicketSearch;Subaction=Search;SearchTemplate=Search;CheckTicketNumberAndRedirect=1;Fulltext='

    def separaTicketsPorQueue(self):

        for key ,ticket in self.tickets.items():

            if ticket['QUEUE'] == 'Organico::NOC::Tier 1':
                self.queue['Organico::NOC::Tier 1'].append(ticket)
            elif ticket['QUEUE'] == 'Organico::NOC::Tier 2':
                self.queue['Organico::NOC::Tier 2'].append(ticket)
            elif ticket['QUEUE'] == 'Organico::NOC::Tier 3':
                self.queue['Organico::NOC::Tier 3'].append(ticket)
            elif ticket['QUEUE'] == 'Organico::NOC':
                self.queue['Organico::NOC'].append(ticket)


    def imprimirTicketsPorQueue(self):

        for key, tickesList in self.queue.items():
            print(key)
            for tickes in tickesList:
                print(tickes)


    def asignarTickets(self):
       #iterar perimero la queue 2 y luego la queue 1
       # si el owner no corresponde al actual se revisa el historial para buscar si un operador lo tomo, sino, se asigna al tier con menos tickts
       #
       #



        for key, content in self.queue.items():
            print(key, content[0])
            for i in range(len(self.queue[key])):
                print('de la queue: ', self.queue[key][i]['OWNER'])
                for operatorPresent in operadores:
                    print('del for para buscar si esta el operador presente', operatorPresent['nombre'])
                    if self.queue[key][i]['OWNER'] == operatorPresent['nombre']:
                        print('owner ', self.queue[key][i]['OWNER'],  'presente ' ,operatorPresent['nombre'])
                    else:
                        print('no es del operador presente')






ticket = Ticket(dataTickets, operadores)

ticket.separaTicketsPorQueue()

ticket.asignarTickets()


# for index, ticket in dataTickets.items():
#     print(index, ticket)

