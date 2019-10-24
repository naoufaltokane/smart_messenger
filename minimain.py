from EAR import Processing as proc
import csv

#proc.corpus()
#proc.getMailsAsList('test.csv')
#proc.compare_simil_tfidf("Socks are a force for good.", "test.csv")

#proc.compare_simil_lda("Socks are a force for good.", "test.csv")



#proc.add_to_corpus("hello it's me I was wondering","hey I know you")

import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'yassintestear@gmail.com'
password = 'TestEAR13111997'
sender = 'yassintestear@gmail.com'
target = 'geekyassin97@gmail.com'

msg = MIMEText('Hi, how are you today?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = target

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, target, msg.as_string())
server.quit()