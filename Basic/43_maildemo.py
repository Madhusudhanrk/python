import smtplib

server = smtplib.SMTP("smtp.gmail.com",587)

server.starttls()

server.login('madhusudhanrk98@gmail.com','235Main@mail$')

server.sendmail('madhusudhanrk98@gmail.com','madhusudhandummy@gmail.com','your tony')

#Here we using python app using to send mail with gmail ID not using google app 
#so google will shut your python app to send mail using gmail ID
# In order to use python app to send mail using gmail Id turn of the security in gmail id

print("mail sent")