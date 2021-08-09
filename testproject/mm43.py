from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

driver.get(URL)

# elemek megkeresése
email = driver.find_element_by_id('email')
btn = driver.find_element_by_id('submit')

# tesztadatok listája
test_email = ["teszt@elek.hu", "teszt@", ""]

''' TC001
* Helyes kitöltés esete:
    * email: teszt@elek.hu
    * Nincs validációs hibazüzenet
'''
email.send_keys(test_email[0])
btn.click()
# message = driver.find_element_by_xpath('//div[@class="validation-error"]')
# assert "" == message.text
# itt nem találja meg a message-et az xpath alapján, ezért nem tudom elvégezni az assert-et


''' TC002
* Helytelen:
    * email: teszt@
    * Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.
'''
# a mező törlése után kitöltöm a tesztadattal, majd ellenőrzök
email.clear()
email.send_keys(test_email[1])
btn.click()
message = driver.find_element_by_xpath('//div[@class="validation-error"]')
assert 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.' == message.text

'''TC003
* Üres:
    * email: <üres>
    * Kérjük, töltse ki ezt a mezőt.
'''
# a mező törlése után kitöltöm a tesztadattal, majd ellenőrzök
email.clear()
email.send_keys(test_email[2])
btn.click()
message = driver.find_element_by_xpath('//div[@class="validation-error"]')
assert 'Kérjük, töltse ki ezt a mezőt.' == message.text

driver.close()
