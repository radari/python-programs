import parameters

import smtplib

               
def send_email(to, subject, text):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(parameters.gmail_sender, parameters.gmail_passwd)

    body = '\r\n'.join(['To: %s'% to, 'From: %s' % parameters.gmail_sender, 'Subject: %s' % subject, '', text])

    try:
        server.sendmail(parameters.gmail_sender, [to], body)
        print('email sent')
    except:
        print('error sending mail')
        
    server.quit()
    
def test_sender():
    to = 'tomail@gmail.com'
    subject = 'test mail'
    text = 'here is a msg from python'

    send_email(to, subject, text)

