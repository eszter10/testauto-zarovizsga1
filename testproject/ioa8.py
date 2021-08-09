from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"

driver.get(URL)

# elemek megkeresése
num_1 = int(driver.find_element_by_id('num1'))
operator = int(driver.find_element_by_id('op'))
num_2 = int(driver.find_element_by_id('num2'))
btn = driver.find_element_by_id('submit')
result = driver.find_element_by_id('result')

res = 0
'''
TC001
Ki kell olvasni a két operandust (számot) és az operátort (műveleti jelet).
Ennek megfelelően kell elvégezni a kalkulációt Pythonban.
Összehasonlítjuk az applikáció által kínált megoldást és a Python által kalkulált eredményt.
'''
# elágazások: a különböző műveletek végrehajtása

if operator = +:
    res = num_1 + num_2
elif operator = -:
    res = num_1 - num_2
elif operator = *:
    res = num_1 * num_2
else operator = /:
res = num_1 / num_2

# összehasonlítom az eredményeket

assert res == result.text

driver.close()
