
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


import mysql.connector as mysql
'''
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd ="abhi.239",
    database = "ccatcracker"
)
'''
db = mysql.connect(
    host = "localhost",
    user = "ccatcracker",
    passwd ="Abhi.@239",
    database = "ccatcracker"
)



def sendmail(record):
    user_id = record[0]
    email_user = 'help@ccatcracker.in'
    email_password = 'GeTx!As7'
    email_send = record[1]

    subject = 'Last Reminder Todays Question Dont Miss'
    print(email_send)
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject


    body = '''
            Hi there,
            Click below link and solve
            todays new questions on C++ 
            and Aptitude . 
            http://ccatcracker.in
        
            Thanks,
            ccatcracker

    '''

    try :

        msg.attach(MIMEText(body,'plain'))
        text = msg.as_string()
        server = smtplib.SMTP('smtp.ccatcracker.in',587)
        server.starttls()
        server.login(email_user,email_password)
        v = record[0]
        server.sendmail(email_user,email_send,text)
        cursor.execute("update pages_send set status = '%s' where id = '%s' " %('Sent',v))
        db.commit()
    except:
        print("error")
        print(email_send)
        

    server.quit()

for i in range(99):
    cursor = db.cursor()
    query = "SELECT * FROM pages_send where status= 'New' "


    ## getting records from the table
    cursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()
   
    if records:
        sendmail(records[0])
    else:
        break




