import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_test_email():
    # Set your email configuration
    smtp_server = "localhost"
    smtp_port = 1025  # Mailhog default port
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"
    subject = "Test Email Subject"
    body = "This is a test email."

    # Create a MIME message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the local SMTP server (Mailhog)
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Test email sent successfully.")


if __name__ == "__main__":
    send_test_email()
