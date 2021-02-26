# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Thank you"
 
# setup the parameters of the message
password = ""
msg['From'] = "@.com.br"
msg['To'] = "@.com.br"
msg['Subject'] = "Subscription"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print("successfully sent email to %s:" % (msg['To']))


'''
import glob


cadastro_empresas = {
    191: ('ZAILAH', 'Email_ZAILAH'),
    104: ('ZRG','Email_ZRG')
    }

def encontrar_documento(codigo_empresa):
    try:
        documento = glob.glob('* - ' + str(codigo_empresa) + ' - *')
        return documento
    except Exception:
        print(Exception)        

for empresa in cadastro_empresas:
    a = encontrar_documento(empresa)
    print(cadastro_empresas[empresa][1])
    print(a[0])

'''