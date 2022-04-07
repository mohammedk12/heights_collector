from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_heights,count):
    
    from_email= "mohammedghef@gmail.com"
    from_password= "1234Abcd"
    
    to_email=email
    subject= "Height data"
    message= f"<h1>the average of the iheights is: {average_heights}</h1>your height is:<strong>{height}cm</strong>.<br><p>total number of heights is: <strong>{count}.</strong></p>"
    msg= MIMEText(message, 'html') #the message will be read as html
    msg['Subject'] =subject
    msg['To'] = to_email
    msg['From'] = from_email
    
    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
