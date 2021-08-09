from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"

driver.get(URL)

# elemek megkeresése

side_a = driver.find_element_by_id('a')
side_b = driver.find_element_by_id('b')
btn = driver.find_element_by_id('submit')
result = driver.find_element_by_xpath('//*[@id="result"]')

# tesztadatok
test_data_a = ["99", "kiskutya", ""]
test_data_b = ["12", "12", ""]
result_data = ["222", "NaN", "NaN"]

''' TC001
Helyes kitöltés esete:
    * a: 99
    * b: 12
    * Eredmény: 222
'''
side_a.send_keys(test_data_a[0])
side_b.send_keys(test_data_b[0])
btn.click()
time.sleep(1)
assert result.get_attribute("value") == "222"

''' TC002
Nem számokkal történő kitöltés:
    * a: kiskutya
    * b: 12
    * Eredmény: NaN
'''
side_a.clear()
side_b.clear()
side_a.send_keys(test_data_a[1])
side_b.send_keys(test_data_b[1])
btn.click()
time.sleep(1)
assert result.get_attribute("value") == result_data[1]

''' TC003
* Üres kitöltés:
    * a: <üres>
    * b: <üres>
    * Eredmény: NaN 
'''
side_a.clear()
side_b.clear()
side_a.send_keys(test_data_a[2])
side_b.send_keys(test_data_b[2])
btn.click()
time.sleep(1)
assert result.get_attribute("value") == result_data[2]

driver.close()
