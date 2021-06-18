#NOW OUR AUTO EMAIL FUNCTION
import smtplib
def sendmail():
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("spartaking369@gmail.com","*******")
    #server.sendmail(sender_mail,reciever_mail,message)
    server.sendmail("spartaking369@gmail.com","bishtshiva200@gmail.com","HI ")
    server.quit()
