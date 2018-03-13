import pyautogui as pa
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
Filename = input("Enter Filename ")
time.sleep(3)
pa.keyDown('alt')
pa.keyDown('tab')
pa.keyUp('tab')
pa.keyDown('tab')
pa.keyUp('tab')
pa.keyUp('alt')
time.sleep(2)
pa.hotkey('ctrl','a')
pa.hotkey('ctrl','c')
pa.hotkey('win')
time.sleep(2)
pa.typewrite("Wordpad")
time.sleep(2)
pa.press('enter')
time.sleep(2)
pa.hotkey('ctrl','v')
time.sleep(2)
pa.keyDown('alt')
pa.keyDown('tab')
pa.keyUp('tab')
pa.keyDown('tab')
pa.keyUp('tab')
pa.keyUp('alt')
time.sleep(3)
pa.hotkey('prtscr')
pa.hotkey('alt','tab')
time.sleep(3)
pa.hotkey('ctrl','v')
pa.hotkey('ctrl','s')
pa.typewrite(Filename)
time.sleep(2)
addressBarLoc = pa.locateOnScreen("addressbar.png")
print(addressBarLoc)
addressx,addressy = pa.center(addressBarLoc)
pa.click(addressx,addressy)
time.sleep(4)
saveBarLoc = pa.locateOnScreen("save.png")
print(saveBarLoc)
savex,savey = pa.center(saveBarLoc)
pa.click(savex,savey)
time.sleep(7)

msg = MIMEMultipart()
fromaddr = 'Your Email id'  #Enter Your Gmail id here
toaddrs  = ['friend#1 email id','friend#2 email id','friend#3 email id',]   #Enter Your Friends Gmail ids here
username = 'Your Email id'  #Enter Your Gmail id here
password = 'Your password'  #Enter Your Password
fname="D:/{}{}."
filename = Filename+".rtf"
attachment = open(fname.format(Filename,".rtf"), "rb")
p = MIMEBase('application', 'octe   t-stream')
p.set_payload((attachment).read())
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()
