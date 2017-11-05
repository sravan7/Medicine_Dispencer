import time
import threading
import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText
from time import sleep
class ti:
   def __init__(self, times):
      time.sleep(times)
      
   def on(self,med,button):
       print "Medicine to be taken:"+med
       GPIO.output(button,1)
       
   def des(self,button):
       self.button = button
       GPIO.output(button,0)
   def mail(self,msg,addr,passw,fromadd,toadd):
       
       print "Email sent"

        
GPIO.setmode(GPIO.BOARD)               
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
button1=16
button2=22
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
timetup = time.localtime( time.time() )
t = time.strftime('%Y-%m-%dT %H %M %S', timetup)

timsec=[]
se=[]
inp=raw_input("Choose the container numbers you want to use:")
s=inp.split()
if (int(s[1])==0 and int(s[0])==1):
    name=raw_input("enter the name of medicine in container 1:")
    seco=raw_input("Enter the time in the Format hh mm ss:")
    message="Remainder for medicine to be taken"+name
    msg=MIMEText(message)
    msg['subject']='Take medicine:'+name
    msg['From']='yourMail@gmail.com'
    msg['To']='yourMail@gmail.com'
    hrs=int(t.split()[1])-int(seco.split()[0]);
    minu=int(t.split()[2])-int(seco.split()[1]);
    sec=int(t.split()[3])-int(seco.split()[2]);
    tim=abs(hrs)*3600+abs(minu)*60+abs(sec)
    print tim
    k=ti(tim)
    print "processing Mail"
    s=smtplib.SMTP('smtp.gmail.com')
    s.starttls()
    s.login('yourMail@gmail.com','Your password')
    s.sendmail(msg['From'],msg['To'],msg.as_string())
    s.close()
    print "Email sent"
    
    def con1():
      threading.Timer(20,con1).start()
      while True:
         
         k.on(name,12)
         if GPIO.input(button1)>0:
            k.des(12)
            break
    con1()
            
elif (int(s[0])==0 and int(s[1])==2):
    name=raw_input("enter the name of medicine in container 2:")
    seco=raw_input("Enter the time in the Format hh mm ss:")
    hrs=int(t.split()[1])-int(seco.split()[0]);
    minu=int(t.split()[2])-int(seco.split()[1]);
    sec=int(t.split()[3])-int(seco.split()[2]);
    tim=abs(hrs)*3600+abs(minu)*60+abs(sec);
    print tim
    k=ti(tim)
    while True:
        k.on(name,12)
        if GPIO.input(button2)>0:
            k.des(12)
            break
elif (int(s[0])==1 and int(s[1])==2):
    name1=raw_input("enter the name of medicine in container 1:")
    name2=raw_input("enter the name of medicine in container 2:")
    sec1=raw_input("Enter the time for container 1 in the Format hh mm ss:")
    se.append(sec1)
    sec2=raw_input("Enter the time for container 2 in the Format hh mm ss:")
    se.append(sec2)
    hrs=int(t.split()[1])-int(se[0].split()[0]);
    minu=int(t.split()[2])-int(se[0].split()[1]);
    sec=int(t.split()[3])-int(se[0].split()[2]);
    tim1=abs(hrs)*3600+abs(minu)*60+abs(sec);
    timsec.append(tim1)
    hrs=int(t.split()[1])-int(se[1].split()[0]);
    minu=int(t.split()[2])-int(se[1].split()[1]);
    sec=int(t.split()[3])-int(se[1].split()[2]);
    tim2=abs(hrs)*3600+abs(minu)*60+abs(sec);
    timsec.append(tim2)
    print timsec
    k1=ti(tim1)
    
    while True:
        k1.on(name1,12)
        
        if GPIO.input(button1)>0:
            k1.des(12)
            break
         
    k2=ti(abs(tim2-tim1))

    while True:
        k2.on(name2,12)
        
        if GPIO.input(button2)>0:
            k2.des(12)
            break
    
    
else:
    print "Wrong Input given"
    


              
