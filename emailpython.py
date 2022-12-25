import smtplib,ssl
import time
# # email sender program
# import smtplib

class Sumbition():

    def __init__(self,sender,password,reciever,subject,body) :
        
        self.sender=sender
        self.password=password
        self.reciever=reciever
        self.subject=subject
        self.body=body
    

    def sende(self):
        message= f'''From: {self.sender}
        To: {self.reciever}
        subject: {self.subject}\n
        {self.body}
        
        '''

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            print( 'wainting to log in..')
            server.login(self.sender, self.password)
            print( 'logged in...')
            server.sendmail(self.sender, self.reciever, message)
        print("Email sent")




sendere=input("Enter your email:")
passworde=input("Enter your password")
recievere=input(f"Enter email of reciever:")
subjecte=input(f"Enter email's subject:")
bodye=input(f"Enter email's body:")

while True:   # while creates a infinite loop be careful with this

    Sumbition_com=Sumbition(sendere,passworde,recievere,subjecte,bodye)

    Sumbition_com.sende()
    time.sleep(2)
    

