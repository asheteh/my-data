#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# import pyexcel.ext.xlsx # no longer required if you use pyexcel >= 0.2.2

print("Hello")

l2 =  ["/home/ccatcracker/pyapps/ccatcracker/files/notes/CCATCRACKER_Must_Read.pdf","/home/ccatcracker/pyapps/ccatcracker/files/notes/networking_os_notes.pdf",
        "/home/ccatcracker/pyapps/ccatcracker/files/notes/OS.pdf", "/home/ccatcracker/pyapps/ccatcracker/files/notes/c++notes.pdf","/home/ccatcracker/pyapps/ccatcracker/files/notes/c-lang.pdf",
        "/home/ccatcracker/pyapps/ccatcracker/files/notes/data-strucure.pdf"]
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "ccatcracker",
    passwd ="Abhi.@239",
    database = "ccatcracker"
)


cursor = db.cursor()
query = "SELECT * FROM payment_orders  where status= 'Placed' "

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    

    email_user = 'thinkgeek.testing@gmail.com'
    email_password = '9921471309'
    email_send = record[3]
    subject = 'subject'
    print(email_send)

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    v = record[0]
    body = 'Hi there, sending this email from Python!'
    msg.attach(MIMEText(body,'plain'))

    #filename=['2.pl','m1.pl','file2.txt']
    for filenam in l2:

        attachment  =open(filenam,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filenam)

        msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    cursor.execute("update payment_orders set status = '%s' where order_id = '%s' " %('Sent',v))

    ## final step to tell the database that we have changed the table data
    db.commit()


    server.sendmail(email_user,email_send,text)
    server.quit()







