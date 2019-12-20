from selenium import webdriver
from database import  webs

#from selenium.webdriver.common.keys import Keys



url =  webs[2]['web']



firefox_driver = webdriver.Firefox(executable_path=r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')


#INICIO DE SESION
def log_in(driver, credentials):
    """
    Log into the web page passing the user and pass credentials

    """

    #User field

    user_text = driver.find_element_by_id(credentials['user_field']) or driver.find_element_by_class_name(credentials['user_field'])
    user_text.clear()
    user_text.send_keys(credentials['user'])
    driver.implicitly_wait(1)
    # Password field
    user_pass = driver.find_element_by_id(credentials['pass_field']) or driver.find_element_by_class_name(credentials['user_field'])
    user_pass.clear()
    user_pass.send_keys(credentials['password'])
    # Click on the button
    button = driver.find_element_by_id(credentials['button']) or driver.find_element_by_class_name(credentials['button'])
    button.click()

    return driver


firefox_driver.get(url)

log_in(firefox_driver, webs[1])




