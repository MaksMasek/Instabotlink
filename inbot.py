import json
from selenium import webdriver
import datetime
from time import sleep
from selenium.webdriver.common.keys import Keys

#def findword(pol):




#def newword(ang):



def logowanie():
    login = 'majmas552'
    password = 'tiemx'
    driver = webdriver.Chrome("C:\\Users\\Maksymilian Masek\\Desktop\\chromedriver.exe")
    driver.get('https://instaling.pl/teacher.php?page=login')
    sleep(8)
    log = driver.find_element_by_name("log_email")
    haslo = driver.find_element_by_name("log_password")
    log.send_keys(login)
    haslo.send_keys(password, Keys.ENTER)
    sleep(3)
    sesja = driver.find_element_by_id("session_button")
    sesja.click()
    potwiedz = driver.find_element_by_id("session_button")

logowanie()

