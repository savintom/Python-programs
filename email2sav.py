import smtplib
import getpass
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
u=input("enter your username(email id): ")
p=getpass.getpass(prompt='Password: ') 
s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender=u
receiver='savintom@rediffmail.com'
msg = MIMEMultipart()
body="hii!!!"
msg.attach(MIMEText(body, 'plain'))
filename = "fibonacci.py"
attachment = open("/home/bl305/fibonacci.py", "rb") 
z = MIMEBase('application', 'octet-stream')
z.set_payload((attachment).read()) 
msg.attach(z)
text = msg.as_string()
s.login(u,p)
s.sendmail(sender,receiver,text)
print("msg sent succesfully")
s.quit()