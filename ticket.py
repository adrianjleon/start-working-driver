

class Ticket:

    def __init__(self, tickets, operators):
        self.tickets = tickets
        self.operators = operators
        self.queue = { 'Organico::NOC::Tier 1': [] ,
                       'Organico::NOC::Tier 2': [] ,
                       'Organico::NOC::Tier 3': [],
                       'Organico::NOC': [],}
        self.url = 'http://nts.neutrona.com/otrs/index.pl?;Action=AgentTicketSearch;Subaction=Search;SearchTemplate=Search;CheckTicketNumberAndRedirect=1;Fulltext='

    def separaTicketsPorQueue(self):

        for key, ticket in self.tickets.items():

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


    def asignarTicketsPorQueue(self):
       #iterar perimero la queue 2 y luego la queue 1
       # si el owner no corresponde al actual se revisa el historial para buscar si un operador lo tomo, sino, se asigna al tier con menos tickts
        tickesSinOwner = []
        for key, content in self.queue.items():
            print()
            print(key)
            print()
            for i in range(len(self.queue[key])):

                print('de la queue: ', i , self.queue[key][i]['OWNER'])
                contador = 0
                for operatorPresent in range(len(self.operators)):
                    print()
                    #print('del for para buscar si esta el operador presente', self.operators[operatorPresent]['nombre'])
                    #print(self.queue[key][i]['TN#'])
                    if self.queue[key][i]['OWNER'] == self.operators[operatorPresent]['nombre']:
                        print()
                        print('El owner del ticket en la Queue es', self.queue[key][i]['OWNER'],  ' y la cual esta presente presente ' ,self.operators[operatorPresent]['nombre'])
                        self.operators[operatorPresent]['tickets'].append(self.queue[key][i]['TN#'])
                        print('se almacena el ticket ',self.queue[key][i]['TN#'] , 'al operador', self.operators[operatorPresent]['nombre'])
                        print()
                        break
                    else:
                        contador += 1
                        print(contador)
                        if contador == len(self.operators):
                            tickesSinOwner.append(self.queue[key][i])
                            contador = 0
                        #print('no le pertenece al operador presente ')

                        print()
        print()

        if len(tickesSinOwner) > 0:
            self.asignarTickesSinOwner(tickesSinOwner)

    def asignarTickesSinOwner(self, tickesSinOwner):

        for i in range(len(tickesSinOwner)):

            print('de los sin owner: ', i, tickesSinOwner[i]['QUEUE'])

            for operatorPresent in range(len(self.operators)):
                print()
                # print('del for para buscar si esta el operador presente', self.operators[operatorPresent]['nombre'])
                # print(self.queue[key][i]['TN#'])
                if tickesSinOwner[i]['QUEUE'] == self.operators[operatorPresent]['queue']:
                    print()



                    self.operators[operatorPresent]['tickets'].append(tickesSinOwner[i]['TN#'])
                    print('se almacena el ticket ', tickesSinOwner[i]['TN#'], 'al operador',
                          self.operators[operatorPresent]['nombre'])
                    print()
                    break
                else:
                    pass

                    print()



