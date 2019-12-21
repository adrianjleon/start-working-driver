from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#OPEN A WEB
def openWeb(driver, web):
    return driver.get(web)




# INICIO DE SESION
def log_in(driver, credentials):
    """
    Log into the web page passing the user and pass credentials
    where user  and pass fields get id and button gets the class of the element

    """

    # User field

    user_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, credentials['user_field'])))
    user_text.clear()
    user_text.send_keys(credentials['user'])
    driver.implicitly_wait(1)

    # Password field

    user_pass = driver.find_element_by_id(credentials['pass_field'])
    user_pass.clear()
    user_pass.send_keys(credentials['password'])

    # Click on the button by class

    driver.implicitly_wait(1)
    button = driver.find_element_by_class_name(credentials['button'])
    button.click()
    driver.implicitly_wait(1)
    return driver

#OPEN THE FIRST WORK WINDOW ON FIREFOX

def openFirefoxWebs(driver, data):

    for web in range(len(data) - 1):
        try:
            openWeb(driver, data[web]['url'])
            log_in(driver, data[web])
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[web + 1])

        except:
            print("We couldnt open the webs")

#OPEN THE FIRST WORK WINDOW ON CHROME

def openChromePhone(driver, data):
    try:
        openWeb(driver, data['url'])
        log_in(driver, data)

    except:
        print("We couldnt open the webs")


def takeTickesFromAOVivo(table):
    pass