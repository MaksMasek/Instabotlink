
from time import sleep
import datetime
import smtplib
from email.message import EmailMessage
useremail = input('podaj swój email: ')
userpassword = input('podaj swoje hasło: ')
odbiorca = input('email adresata: ')
temat = input('temat wiadomości: ')
tresc = input('tresc wiadomości: ')
print('docelowa data wyslania(dzien/godzina/minuta)(zamias np. 08 napisz 8):')
dzien = int(input('dzien: '))
godzina = int(input('godzina: '))
minuta = int(input('minuta: '))

msg = EmailMessage()
msg['from'] = 'm.masek@zlotoryja.xyz'
msg['to'] = odbiorca
msg['Subject'] = temat
msg.set_content(tresc)

dsend = datetime.datetime(2020, 3, dzien, godzina, minuta, 0)
delta = datetime.timedelta(minutes=2)

while datetime.datetime.today()<delta+dsend:

    dowyslania = dsend - datetime.datetime.today()
    print(datetime.datetime.today(), end=f"     Do wysłania pozostało   {dowyslania}\n ")
    if datetime.datetime.today() > dsend:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(useremail,userpassword)
            smtp.send_message(msg)
            print(f'Twoja wiadomosc na adres {odbiorca} została wysłana!')
            quit()
    sleep(5)
