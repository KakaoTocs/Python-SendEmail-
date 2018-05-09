import smtplib
from email.mime.text import MIMEText

class mail:
    def __init__(self, receiverID, title, contents):
        self.receiverID = receiverID
        self.email = MIMEText(contents)
        self.email['Subject'] = title
        self.email['To'] = receiverID

    def send(self, sender):
        sender.smtp.sendmail(sender.id, self.receiverID, self.email.as_string())
        sender.smtp.quit()

class sender:
    def __init__(self, id, password, provider):
        self.id = id
        self.smtp = smtplib.SMTP('smtp.' + provider, 587)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.login(id, password)

'''
def createDictionary(sender_ID, sender_PW, sender_Provider, receiver_ID, send_contents, send_title):
    dic = {'send_ID': sender_ID, 'send_PW': sender_PW, 'send_Pro': sender_Provider, 'receive_ID': receiver_ID, 'send_cont': send_contents, 'send_title': send_title}
    return dic

def createSMTP(ID, PW, provider):
    smtp = smtp = smtplib.SMTP('smtp.'+provider, 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(ID, PW)
    return smtp

def setMsg(ID, title, contents):
    msg = MIMEText(contents)
    msg['Subject'] = title
    msg['To'] = ID
    return msg

def run(sender_ID, sender_PW, sender_Provider, receiver_ID, send_contents, send_title):
    info_dic = createDictionary(sender_ID, sender_PW, sender_Provider, receiver_ID, send_contents, send_title)
    smtp = createSMTP(info_dic['send_ID'], info_dic['send_PW'], info_dic['send_Pro'])
    msg = setMsg(info_dic['receive_ID'], info_dic['send_title'], info_dic['send_cont'])
    smtp.sendmail(info_dic['send_ID'], info_dic['receive_ID'], msg.as_string())
    smtp.quit()
'''
