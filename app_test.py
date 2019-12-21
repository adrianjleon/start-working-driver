
chrome_driver = webdriver.Chrome(r'P:\proyectos-pycharm\drivers\chrome\chromedriver.exe')

openWeb(chrome_driver, 'http://nts.neutrona.com/')
log_in(chrome_driver,     {'url':   'http://nts.neutrona.com/',
     'user': 'adrian.leon',
     'password': 'Neutrona1',
     'user_field': 'User',
     'pass_field': 'Password',
     'button': 'CallForAction'})

chrome_driver.implicitly_wait(10)

table = Table(chrome_driver)

print(table.get_colum_info())

print(table.get_results())









