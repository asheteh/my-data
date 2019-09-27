import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "ccatcracker",
    passwd ="Abhi.@239",
    database = "ccatcracker"
)


cursor = db.cursor()
query = "SELECT * FROM pages_sendemail  where status= 'New' "





## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    email_user = 'help.ccatcracker@gmail.com'
    email_password = 'abhi.239'
    email_send = record[1]
    subject = 'Question-Of-The-Day'
    print(email_send)
    v = record[0]
    
   
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject


    body = '''Hi Dear  : ,
Please check  : 
ccatcracker.in/ccat 
Our CCAT DEC -2019 Daily questions program will start from 1st Sep 2019 . So dont waste your time Purchase our great Study Material Only at Rs.200 and Start Prepare You Will Get Lots of benefits . 
If You Have any doubts query regarding study Material Please let Us know .. 

Dont Think Too Much for 200 Rs only its really very very low cost Pre Dac Course ..


!! All The Best !!

Thanks,

ccatcracker
'''

    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    ## executing the query
   
#    cursor.execute("update payment_orders set material = '%s' where order_id = '%s' " %('Sent',v))

## final step to tell the database that we have changed the table data
    db.commit()


    server.sendmail(email_user,email_send,text)
    server.quit()



