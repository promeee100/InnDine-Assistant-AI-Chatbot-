import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SENDER_EMAIL = "sanjanatasnim18@gmail.com"
APP_PASSWORD = "bipi wgmq qumb vazd"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def send_email(receiver_email, subject, message):

    try:

        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))


        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)


        server.send_message(msg)
        server.quit()

        print(f" Email sent successfully to {receiver_email}")
        return "Email sent successfully!"

    except Exception as e:
        print(f" Failed to send email: {e}")
        return f"Error sending email: {e}"
