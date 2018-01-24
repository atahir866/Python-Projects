# import necessary libraries

import time
import smtplib
from binance.client import Client
import re

# define a function which will be called after every one minute
def get_new_Currencies():
    
    # define a fucntion which will send an email to his/her account if there is a new currency is added on binance.
    def send_email(user, password, recipient, subject, body):
        gmail_user = user
        gmail_pwd = password
        FROM = user
        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
     
    # Initiating a list with current currencies
    Current_currencies=['ETHBTC',
     'LTCBTC',
     'BNBBTC',
     'NEOBTC',
     'BCCBTC',
     'GASBTC',
     'HSRBTC',
     'MCOBTC',
     'WTCBTC',
     'LRCBTC',
     'QTUMBTC',
     'YOYOBTC',
     'OMGBTC',
     'ZRXBTC',
     'STRATBTC',
     'SNGLSBTC',
     'BQXBTC',
     'KNCBTC',
     'FUNBTC',
     'SNMBTC',
     'IOTABTC',
     'LINKBTC',
     'XVGBTC',
     'CTRBTC',
     'SALTBTC',
     'MDABTC',
     'MTLBTC',
     'SUBBTC',
     'EOSBTC',
     'SNTBTC',
     'ETCBTC',
     'MTHBTC',
     'ENGBTC',
     'DNTBTC',
     'ZECBTC',
     'BNTBTC',
     'ASTBTC',
     'DASHBTC',
     'OAXBTC',
     'ICNBTC',
     'BTGBTC',
     'EVXBTC',
     'REQBTC',
     'VIBBTC',
     'TRXBTC',
     'POWRBTC',
     'ARKBTC',
     'XRPBTC',
     'MODBTC',
     'ENJBTC',
     'STORJBTC',
     'VENBTC',
     'KMDBTC',
     'RCNBTC',
     'NULSBTC',
     'RDNBTC',
     'XMRBTC',
     'DLTBTC',
     'AMBBTC',
     'BATBTC',
     'BCPTBTC',
     'ARNBTC',
     'GVTBTC',
     'CDTBTC',
     'GXSBTC',
     'POEBTC',
     'QSPBTC',
     'BTSBTC',
     'XZCBTC',
     'LSKBTC',
     'TNTBTC',
     'FUELBTC',
     'MANABTC',
     'BCDBTC',
     'DGDBTC',
     'ADXBTC',
     'ADABTC',
     'PPTBTC',
     'CMTBTC',
     'XLMBTC',
     'CNDBTC',
     'LENDBTC',
     'WABIBTC',
     'TNBBTC',
     'WAVESBTC',
     'GTOBTC',
     'ICXBTC',
     'OSTBTC',
     'ELFBTC',
     'AIONBTC',
     'NEBLBTC',
     'BRDBTC',
     'EDOBTC',
     'WINGSBTC',
     'NAVBTC',
     'LUNBTC',
     'TRIGBTC',
     'APPCBTC',
     'VIBEBTC',
     'RLCBTC' ,
     'INSBTC']
    
    client = Client('Enter your Api Key', 'Enter your Api secret')
    
    # get all currencies
    prices = client.get_all_tickers()
    y=[]
    
    # extracting the currency name
    for i in prices:
        if re.search('.+BTC',i['symbol']):
            y.append(i['symbol'])
    New=[]
    j=[]
    Text=''
    if y==Current_currencies:
        print('No new currency')
    else:
        for i in y:
            if i not in Current_currencies:
                New.append(re.findall('(.*)BTC',i))
        for i in New:
            for l in i:
                j.append(l)
        for i in j:
            Text=Text + '\n' + i
        Current_currencies=y

        send_email('Enter sender email address','enter sender password','enter reciepent email address',
                   'Enter subject','New currenies added are' + Text )        


# define a function that will call the above function after every 1 minute

def executeSomething():
    get_new_Currencies()
    time.sleep(3600)

while True:
    executeSomething()