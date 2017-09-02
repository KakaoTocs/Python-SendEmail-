import smtplib
from email.mime.text import MIMEText

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
