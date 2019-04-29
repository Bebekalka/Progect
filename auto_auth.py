#!/usr/bin/python
from http.client import HTTPSConnection, HTTPConnection
import bs4, email, smtplib, time
#check balance
http = "lk.qwerty.ru"
prov = "Qwerty"
url1 = "/owa/rac.k/!w3_p_main.showform"
url2 = "dima.novikovi.info"
c = HTTPSConnection(http)
c.request("POST", url1, "IDENTIFICATION=CONTRACT&USERNAME=&USERNAME=4128417368&PASSWORD=v0lthfnjh&FORMNAME=QFRAME")
response = c.getresponse()
data = response.read()
a = bs4.BeautifulSoup(data, "html.parser")
url = a.find_all("frame")[1]["src"]
quest = HTTPSConnection(http)
quest.request("GET", url1 + url)
inf = quest.getresponse().read()
content = bs4.BeautifulSoup(inf, "html.parser")
balans1 = content.findAll('tr', {"class": "Row2"})
balans = str(balans1[2].findAll('td', {"align": "RIGHT"}))
balans = balans.split(">")
balans[1] = balans[1].split("<")[0]
bal = float(balans[1].split()[0])
#print(balans[1])
#print(content.prettify())
# sntp


def smtp_init(smtpserver, smtpserverport):
    """
    Initialize SMTP connection
    """
    #print("Initializing SMTP...")
    global s
    s = smtplib.SMTP(smtpserver, smtpserverport)
    c = s.starttls()[0]  # The returned status code
    if c is not 220:
        raise Exception('Starting tls failed: ' + str(c))
    c = s.login(radr, pwd)[0]
    if c is not 235:
        raise Exception('SMTP login failed: ' + str(c))
    #print("Done. ")

def mail(text, radr, sadr, subject):
    """
    Print an email to console, then send it
    """
    #print("This email will be sent: ")
    #print(text)
    msg = email.message.EmailMessage()
    msg["from"] = radr
    msg["to"] = sadr
    msg["Subject"] = subject
    msg.set_content(text)
    res = s.send_message(msg)
    #print("Sent, res is", res)


#connection to mailBot
radr = "bot@novikovi.info"
smtpserver = "smtp.novikovi.info"
smtpserverport = 25
pwd = "webbot2019"
sadr = "nda_mine@mail.ru"
check_freq = 60
mailtext = "Внимание у вас осталось " + str(bal) + " рублей. Срочно пополните баланс."
subject = "Баланс Qwerty"
smtp_init(smtpserver, smtpserverport)


#add to database
def base_add(prov, url2, bal):
    tme = time.localtime()
    urlbase = "/add_day.php?data=" + str(tme[0]) + "-" + str(tme[1]) + "-" + str(tme[2]) + "&" + "provider=" + prov + "&" + "remain=" + str(bal)
    baseconn = HTTPConnection(url2)
    baseconn.request("GET", urlbase)
    res = baseconn.getresponse()
flag = True
while flag:  # Main loop
    try:
        base_add(prov, url2, bal)
        if bal <= 50:
            mail(mailtext, radr, sadr, subject)
        flag = False  # Blank line for clarity
    except smtplib.SMTPServerDisconnected:
        smtp_init(smtpserver, smtpserverport)
        continue
    finally:
        s.quit()

