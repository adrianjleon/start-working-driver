

class Dashlet:
    def __init__(self, driver):
        self.driver = driver

    def get_colum_info(self):
        column_info = []
        columns = self.driver.find_elements_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/thead/tr/th')
        for column in columns:
            column_info.append(str(column.text))
        return column_info


    def get_results(self):

        columns = self.get_colum_info()
        data = {}
        elements = self.driver.find_elements_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody/tr')




        for element in elements:
            current_index = elements.index(element) + 1
            parsed_data = {}

            #print('element index', current_index  )
            for column in columns:
                value = element.find_element_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody/tr[{}]/td[{}]'.format(current_index, columns.index(column) + 1)).text
                parsed_data.update({column : str(value)})
            data.update({current_index: parsed_data })

        return data

    def get_num_of_results(self):

        return len(self.driver.find_elements_by_xpath('//*[@id="Dashboard0901-SearchTemplate03"]/form/table/tbody/tr'))