from ticket import Ticket

from dataSampleFromDashlet import dataTickets

def openWeb(driver, web):
    return driver.get(web)

#firefox_driver = webdriver.Firefox(executable_path=r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')

operadores = [
                 {'nombre': 'Adrian Leon', 'queue': 'Organico::NOC::Tier 1',  'tickets' :[] },
                 {'nombre': 'Augusto Cruz', 'queue': 'Organico::NOC::Tier 2', 'tickets' :[] },
                 {'nombre': 'Isaac Graterol', 'queue': 'Organico::NOC::Tier 3', 'tickets' :[] },
              ]









ticket = Ticket(dataTickets, operadores)

ticket.separaTicketsPorQueue()

ticket.asignarTickets()

print(ticket.operators)


# for index, ticket in dataTickets.items():
#     print(index, ticket)

