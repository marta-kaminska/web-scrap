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
        bot.find_element_by_class_name("ng-binding").click()

        #wejscie w profil klienta
        produkty = bot.find_elements_by_class_name("cta-button")
        for element in produkty:
            if element.text == "Zrób zakupy":
                element.click()

        #zalogowanie do profilu klienta
        bot.find_element_by_id("formE-mail").send_keys(self.email)
        bot.find_element_by_id("formHasło(minimum6znaków)").send_keys(self.password)
        time.sleep(2)
        bot.find_element_by_id("formHasło(minimum6znaków)").send_keys(Keys.RETURN)
        time.sleep(5)

    def sprawdz_promocje(self, nazwa_sklepu):
    #dostępne nazwy sklepów Lidl, Carrefour, Biedronka
        bot = self.bot
        sklepy = bot.find_elements_by_class_name("name")
        for element in sklepy:
            if element.text == nazwa_sklepu:
                element.click()
        time.sleep(3)

        #wejscie w kategorie produktow
        bot.find_element_by_class_name("categories-toggler").click()
        time.sleep(2)

        #wejscie w aktualne promocje
        przyciski = bot.find_elements_by_class_name("link")
        if len(przyciski) > 2:
            for element in przyciski:
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
        else:
            print(f"w sklepie {nazwa_sklepu} aktualnie nie ma promocji")
    def wylogowanie(self):
        bot = self.bot
        bot.find_element_by_class_name("personal-area-menu").click()
        bot.find_element_by_class_name("logout").click()
        
        
    


a = Promocjebot("login", "haslo")
a.login()
a.sprawdz_promocje("Biedronka")
a.wylogowanie()