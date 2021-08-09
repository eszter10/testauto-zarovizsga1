import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"

driver.get(URL)

# elemek megkeresése
cities = driver.find_element_by_id('cites')
random_cities = driver.find_element_by_id('randomCities')
missing_city = driver.find_element_by_id('missingCity')
btn = driver.find_element_by_id('submit')
result = driver.find_element_by_id('result')

'''TC001
Találd meg a hiányzó városnevet, töltsd ki a form-ban a mezőt és ellnörizd le, hogy eltaláltad-e.
'''
# listába rendezem a random városneveket - nincs kész

# l = []

# összehasonlítom a lista tartalmát sz összes városnévvel (cities) - nincs kész

# assert

# a listából hiányzó városnevet beírom a missing_city mezőbe, klikk

# összehasonlítom a megjelenő üzenetet

# TC002 üres kitöltés
btn.click()
time.sleep(1)
assert result.text == 'Nem találtad el.'

driver.close()
