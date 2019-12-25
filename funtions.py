from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#OPEN A WEB
def openWeb(driver, web):
    return driver.get(web)




# INICIO DE SESION
def log_in(driver, credentials):
    """
    Log into the web page passing the user and pass credentials
    where user  and pass fields get id and button gets the class of the element

    """

    #OPEN GRAMARLY
    if credentials['url'] == 'https://www.grammarly.com/signin?allowUtmParams=true':
        print(credentials['url'])
        try:
            email_field = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/form/div[1]/div/input')
            driver.implicitly_wait(10)
            email_field.clear()
            email_field.send_keys(credentials['user'])

            button_continue = driver.find_element_by_css_selector(
                '.TqtVC-_-_-_-_-_-client-guidelines-button--button-basicButton').click()

            wait = WebDriverWait(driver, 10)

            pass_field = wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/form/div[2]/input')))

            pass_field.send_keys(credentials['password'])

            button_signInLoader = wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/form/button')))

            button_signInLoader = driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/form/button').click()

            delay = 3  # seconds
            try:
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div/div/div/div[2]/div[4]/div/div[3]/div[1]/div/input')))
                print("Page is ready!")
            except TimeoutException:
                print("Loading took too much time!")

            driver.get('https://app.grammarly.com/ddocs/531109872')
        except Exception as e:
            print("PROBLEMAS PARA ABRIR GRAMARLY", e)

    # User field
    try:
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
    except:
        print("Algo salio mal con una pagina que no es GRamarly")
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
        setAvailableButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/button')))
        time.sleep(5)
        driver.implicitly_wait(500)
        setAvailableButton.click()
        setAvailableButton.click()

    except:
        print("We couldnt open the webs")


def takeTickesFromAOVivo(table):
    pass