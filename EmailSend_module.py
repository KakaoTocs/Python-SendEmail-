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
