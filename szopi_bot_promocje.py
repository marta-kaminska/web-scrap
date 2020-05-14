from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Promocjebot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        #otwarcie strony
        bot.get("https://app.szopi.pl/")
        time.sleep(3)
        #zaakceptowanie ciasteczek
        akceptuj = bot.find_element_by_class_name("ng-binding")
        akceptuj.click()
        #wejscie w profil klienta
        produkty = bot.find_elements_by_class_name("cta-button")
        for element in produkty:
            if element.text == "Zrób zakupy":
                element.click()
        #zalogowanie do profilu klienta
        email = bot.find_element_by_id("formE-mail")
        password = bot.find_element_by_id("formHasło(minimum6znaków)")
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        time.sleep(2)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        #wejscie w sklep LIDL
        sklepy = bot.find_elements_by_class_name("name")
        for element in sklepy:
            if element.text == "Lidl":
                element.click()
        time.sleep(3)
        #wejscie w kategorie produktow
        kategorie = bot.find_element_by_class_name("categories-toggler")
        kategorie.click()
        time.sleep(2)
        #wejscie w aktualne promocje
        nasze_promocje = bot.find_elements_by_class_name("link")
        for element in nasze_promocje:
            if element.text == "Nasze promocje":
                element.click()
        time.sleep(3)
        nazwa_produktu = bot.find_elements_by_class_name("name")
        stara_cena = bot.find_elements_by_class_name("full-price")
        nowa_cena = bot.find_elements_by_class_name("price")

        zbior = {}
        #klucz = nazwa produktu, wartosc klucza stara cena / nowa cena
        i = 0
        while i < len(nazwa_produktu):
            zbior[nazwa_produktu[i].text] = f"{stara_cena[i].text} / {nowa_cena[i].text}"
            i += 1
        print(zbior)
    


a = Promocjebot("login", "hasło")
a.login()
