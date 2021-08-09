from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"

driver.get(URL)

# elemek megkeresése
btn = driver.find_element_by_id('submit')
results = driver.find_elements_by_id('results')

# listát készítek az eredményekből - nincs kész
l = []


# megszámolom a "fej" eredményeket - nincs kész
def get_results():
    return results.count()


# TC001
# Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej.
# Ezt ellenőrizzük.

for i in range(100):
    btn.click()
    time.sleep(1)

res = get_results()

# összehasonlítom a kapott eredményt az elvárttal
assert len(res) >= 30

driver.close()
