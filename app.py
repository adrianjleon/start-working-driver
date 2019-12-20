from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = webdriver.Chrome(r'P:\proyectos-pycharm\drivers\chrome\chromedriver.exe')
#chrome_driver2 = webdriver.Chrome(r'P:\proyectos-pycharm\drivers\chrome\chromedriver.exe')
#firefox_driver = webdriver.Chrome(r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')

url =  'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
url2 =  'https://www.google.com'

#chrome_driver.maximize_window()
chrome_driver.get(url)
text_area = chrome_driver.find_element_by_id('user-message')
show_message_button = chrome_driver.find_element_by_class_name('btn-default')



##print(text_area.get_attribute('innerHTML'))

#assert 'Enter your messaget' in chrome_driver.page_source

text_area.clear()
text_area.send_keys('I am extra cool')

show_message_button.click()

message_showed = chrome_driver.find_element_by_id('display')

print(message_showed.get_attribute('innerHTML'))

chrome_driver.implicitly_wait(3)

# NEW TAB chrome_driver.execute_script("window.open('https://www.google.com');")

# Open a new window
chrome_driver.execute_script("window.open('');")

chrome_driver.switch_to.window(chrome_driver.window_handles[1])
chrome_driver.get(url2)

# Close the tab with URL B
chrome_driver.close()

chrome_driver.switch_to.window(chrome_driver.window_handles[0])
print("Current Page Title is : %s" %chrome_driver.title)


#Take rows from the table

def takeTickesFromAOVivo(table):
    
    pass








