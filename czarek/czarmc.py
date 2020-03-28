from selenium import webdriver
import datetime
from time import sleep
from selenium.webdriver.common.keys import Keys

SCIEZKA_DO_CHROMEDRIVER = "C:\\Users\\Maksymilian Masek\\Desktop\\chromedriver.exe"

LINK = "https://aternos.org/go/"

LOG = "weplaytu"

PASS = "dawidek12"

def login():
        driver = webdriver.Chrome(SCIEZKA_DO_CHROMEDRIVER)
        driver.get(LINK)
        sleep(1)
        login = driver.find_element_by_id("user")
        haslo = driver.find_element_by_id("password")
        login.send_keys(LOG)
        haslo.send_keys(PASS, Keys.ENTER)
        sleep(10)
        potwierdz = driver.find_element_by_id("sncmp-popup-ok-button")
        potwierdz.click()
        sleep(4)
        zielony = driver.find_element_by_id("confirm")
        sleep(10)
        success = 0
        while not success:
            try:
                zielony.click()
                sleep(2)
                success = 1
                msg()
            except:
                print(f"{datetime.datetime.today()}     |     Jeszcze nie...")
                sleep(2)

FB_LOG = "m4ksm4sek@gmail.com"
FB_PASS = "aterrest"

def msg():
    wiadomosc = "Możesz już odpalić server Minecraft!"
    driver = webdriver.Chrome(SCIEZKA_DO_CHROMEDRIVER)
    driver.get("https://www.facebook.com/messages/t/czarek.zajdel")
    sleep(1)
    login = driver.find_element_by_id("email")
    haslo = driver.find_element_by_id("pass")
    login.send_keys(FB_LOG)
    haslo.send_keys(FB_PASS, Keys.ENTER)
    sleep(5)
    czarek = driver.find_element_by_xpath(('//*[@aria-label="Wpisz wiadomość..."]'))
    czarek.send_keys(wiadomosc, Keys.ENTER)
    sleep(2)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    driver.get("https://www.facebook.com/messages/t/100009127168912")
    sleep(1)
    dawid = driver.find_element_by_xpath(('//*[@aria-label="Wpisz wiadomość..."]'))
    dawid.send_keys(wiadomosc, Keys.ENTER)
    sleep(2)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')


login()


