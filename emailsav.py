import smtplib
import getpass
u=input("enter your username(email id): ")
p=getpass.getpass(prompt='Password: ') 
s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender=u
receiver='savintom@rediffmail.com'
msg='hii'
s.login(sender,p)
s.sendmail(sender,receiver,msg)
print("msg sent succesfully")
s.quit()