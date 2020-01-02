from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
import time


class Dashlet:

    def __init__(self, driver):
        self.driver = driver
        self.dashlet = '//*[@id="Dashboard0901-SearchTemplate03-box"]'
        self.dashlet_path = self.dashlet + '//form/table/tbody/tr'
        self.tickets = {}
        self.last_key = 0
        self.paginationNumberPath = self.dashlet + '//span/a'

    def get_column_info(self):
        """
        Get every column information from the dashlet
        :return:
        """
        column_info = []
        columns = self.driver.find_elements_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/thead/tr/th')
        for column in columns:
            column_info.append(str(column.text))
        return column_info

    def get_results(self):
        print(len( self.driver.find_elements_by_xpath(self.paginationNumberPath))   )
        """
        Get all the rows from the current pagination dashlet
        :return:
        """

        columns = self.get_colum_info()
        data = {}
        # wait for element to appear, then hover it
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody')))

        elements = self.driver.find_elements_by_xpath(self.dashlet_path)

        print('obtengo  ', len(elements), 'elementos del path')

        for element in elements:
            current_index =  elements.index(element) + 1
            print('CURRENT INDEX: ',current_index)
            parsed_data = {}

            # print('element index', current_index  )
            for column in columns:
                value = element.find_element_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody/tr[{}]/td[{}]'.format(current_index , columns.index(column) + 1)).text

                parsed_data.update({column: str(value)})
            data.update({current_index + self.last_key: parsed_data})
        self.last_key = len(elements)
        print('ultimo len antes de actualizar ', self.last_key)
        self.tickets.update(data)

    def next_pagination(self, counter):
        print('entrando a next pagination: ' , counter)

        time.sleep(1)
        try:

            next_page = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dashlet + '//span//a[contains(text(), "{}")]'.format(counter))))
            next_page.click()
            print('dì clic')
            time.sleep(5)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody')))

        except Exception as e:
            flag = False
            print("no more pagination")

    def check_for_pagination(self, counter):
        return counter <= (len( self.driver.find_elements_by_xpath(self.paginationNumberPath)))

    def get_all_results(self):

        print(' entre a la funcion all results')

        counter = 2

        self.get_results()

        print('voy a entrar al while')

        while self.check_for_pagination(counter):
            print('entre al while con counter: ' , counter)
            self.next_pagination(counter)
            self.get_results()
            counter += 1
