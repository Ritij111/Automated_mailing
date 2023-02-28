import pandas as pd
import smtplib
from email.mime.text import MIMEText
data = pd.read_csv('name.csv')
email_col = data.get("mail")
list_of_emails = list(email_col)


def send_email(to, body):
    sender = "your_email@example.com" # Change this to your email address
    password = "your_email_password" # Change this to your email password

    message = MIMEText(body)
    message["Subject"] = "Automatic Email"
    message["From"] = sender
    message["To"] = to

    server = smtplib.SMTP("smtp.gmail.com", 587) # Change this to your email server and port
    server.starttls()
    server.login(sender, password)
    server.send_message(message)
    server.quit()

# Example usage
send_email("recipient_email@example.com", "This is the body of the email.")
