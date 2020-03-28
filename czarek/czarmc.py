from selenium import webdriver
import datetime
from time import sleep
from selenium.webdriver.common.keys import Keys

OSOBY = ["https://www.facebook.com/messages/t/czarek.zajdel","https://www.facebook.com/messages/t/100009127168912"]

SCIEZKA_DO_CHROMEDRIVER = "C:\\Users\\Maksymilian Masek\\Desktop\\chromedriver.exe"


LINK = "https://aternos.org/go/"
LOG = "weplaytu"
PASS = "dawidek12"
FB_LOG = "m4ksm4sek@gmail.com"
FB_PASS = "aterrest"
driver = webdriver.Chrome(SCIEZKA_DO_CHROMEDRIVER)

def atter():
        
        driver.get(LINK)
        sleep(1)
        login = driver.find_element_by_id("user")
        haslo = driver.find_element_by_id("password")
        login.send_keys(LOG)
        haslo.send_keys(PASS, Keys.ENTER)
        sleep(10)
        potwierdz = driver.find_element_by_id("sncmp-popup-ok-button")
        potwierdz.click()
        try:
            uruchom = driver.find_element_by_id("start")
            uruchom.click()
            print("dołączyłeś do kolejki")
        except:
            print("jesteś już w kolejce")
        sleep(4)
        zielony = driver.find_element_by_id("confirm")
        sleep(10)
        
        success = 0
        while not success:
            try:
                zielony.click()
                sleep(2)
                success = 1
                zaloguj_fb()
                for i in OSOBY:
                    msg(i,"Możesz już wejść na swór server Minecraft!")
            except:
                print(f"{datetime.datetime.today()}     |     Jeszcze nie...")
                sleep(2)



def zaloguj_fb():
    driver.get("https://www.facebook.com/messages/")
    sleep(1)
    login = driver.find_element_by_id("email")
    haslo = driver.find_element_by_id("pass")
    login.send_keys(FB_LOG)
    haslo.send_keys(FB_PASS, Keys.ENTER)
    sleep(5)

wiadomosc = "Możesz już odpalić server Minecraft!"

def msg(MSG_LINK, wiadomosc):
    driver.get(MSG_LINK)
    sleep(3)
    osoba = driver.find_element_by_xpath(('//*[@aria-label="Wpisz wiadomość..."]'))
    osoba.send_keys(wiadomosc, Keys.ENTER)
    sleep(2)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')



atter()


