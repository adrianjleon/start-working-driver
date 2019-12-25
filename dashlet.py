from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Dashlet:
    def __init__(self, driver):
        self.driver = driver
        self.dashlet_path = '//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody/tr'
        self.tickets = {}
        self.paginationNumberPath = '//*[@id="Dashboard0901-SearchTemplate03"]/span/a'

    def get_colum_info(self):
        column_info = []
        columns = self.driver.find_elements_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/thead/tr/th')
        for column in columns:
            column_info.append(str(column.text))
        return column_info


    def get_results(self):

        columns = self.get_colum_info()
        data = self.tickets

        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody')))

        elements =  self.driver.find_elements_by_xpath(self.dashlet_path)
        print('obtengo los primeros elementos ', len(elements))

        ifPrevius = 0




        for element in elements:
            current_index = len(data) + elements.index(element) + 1
            parsed_data = {}

            #print('element index', current_index  )
            for column in columns:
                value = element.find_element_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody/tr[{}]/td[{}]'.format(current_index - len(self.tickets), columns.index(column) + 1)).text
                parsed_data.update({column : str(value)})
            data.update({current_index: parsed_data })
        print(' devuelvo la data')
        self.tickets.update(data)


    def checkForPagination(self, counter):
        return counter >= len(self.paginationNumberPath)


    def get_num_all_results(self):
        print(' entre a la funcion all result')



        counter = 2

        self.get_results()

        while self.checkForPagination(counter):

            time.sleep(1)
            try:

                next_page = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="Dashboard0901-SearchTemplate03"]/span//a[contains(text(), "{}")]'.format(counter))))
                next_page.click()
                time.sleep(5)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody')))
                self.tickets.update(self.get_results())
                counter =+ 1

            except Exception as e:
                break
                print("no more pagination")


        return self.tickets

    def get_num_of_results(self):
        print('entre a la funcion numero de resultados ')
        return len(self.driver.find_elements_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody/tr'))




