from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#export PATH=$PATH:P:\proyectos-pycharm\drivers\firefox\geckodriver.exe'

url =  'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

url2 =  'https://www.google.com'

firefox_driver = webdriver.Firefox(executable_path=r'P:\proyectos-pycharm\drivers\firefox\geckodriver.exe')



firefox_driver.get(url2)

# Open a new window
firefox_driver.execute_script("window.open('');")

firefox_driver.switch_to.window(firefox_driver.window_handles[1])
firefox_driver.get(url2)

# Close the tab with URL B
firefox_driver.close()

firefox_driver.switch_to.window(firefox_driver.window_handles[0])
print("Current Page Title is : %s" %firefox_driver.title)
