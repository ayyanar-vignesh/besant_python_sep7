import pandas as pd 
import smtplib
import random
#raw data
data=pd.read_csv('aug29.csv')  #frontend
df=pd.DataFrame(data)
# print(df)
print("***********************************")
print(df["email_id"])
for i in df["email_id"]:#read
    print(i)
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("ayyanar.2481996@gmail.com", "lipfcigwfeilcurw")
    # message to be sent
    otp_number=random.randint(0000,9999)
    message = f"your otp number is {otp_number}"
    # sending the mail
    s.sendmail("ayyanar.2481996@gmail.com", i, message)
    # terminating the session
    s.quit()







