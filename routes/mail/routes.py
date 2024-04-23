import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


def mailtest():
    smtp_server = "sandbox.smtp.mailtrap.io"
    smtp_port = 2525
    smtp_username = "a934fd0459c798"
    smtp_password = "849d3adbf6a3e7"

    # Sender and recipient email addresses
    sender_email = "your_email@example.com"
    recipient_email = "recipient@example.com"

    # Message content
    subject = "Test Email"
    body = "This is a test email sent through Mailtrap."

    # Set up the MIME structure
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the Mailtrap SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())


def student_mail(student_name, email, school, modules):
    # list = ["student", "advisor", "programme_director", "faculty_administrator"]
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    # smtp_username = "a934fd0459c798"
    # smtp_password = "849d3adbf6a3e7"
    # Initialize an empty string to store the concatenated result
    modules_str = ""

    # Sender and recipient email addresses
    sender_email = f"{school}@example.com"
    recipient_email = f"{email}"
    # Loop over each string in the array and concatenate it to the result string
    for string in modules:
        modules_str += ", " + string
    # Message content
    subject = "Test Email"
    body = f"""Dear {student_name},
    We hope this message finds you well. We are writing to inform you that the student, {student_name},
    is currently on academic probation. This is due to their GPA falling below the required threshold. These modules where taken {modules_str}. 
    Academic probation is a serious matter as it can impact the student's academic progress and future opportunities.
    We strongly encourage {student_name} to take advantage of the resources available at our institution to improve their academic performance. 
    This includes academic advising, tutoring services, and workshops on study skills and time management.
    We believe in {student_name}'s potential to improve and succeed in their studies. 
    
    Please do not hesitate to reach out if you have any questions or need further information.

    Best regards, {school}"""

    # Set up the MIME structure
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the Mailtrap SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(sender_email, recipient_email, message.as_string())
    return "Sucess"


def faculity_mail(student_name, school, modules):
    lists = ["advisor", "programme_director", "faculty_administrator"]
    for list in lists:
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = os.getenv("SMTP_PORT")
        # smtp_username = "a934fd0459c798"
        # smtp_password = "849d3adbf6a3e7"
        # Initialize an empty string to store the concatenated result
        modules_str = ""

        # Sender and recipient email addresses
        sender_email = f"{school}@example.com"
        recipient_email = f"{list}@{school}.fake.edu.jm"
        # Loop over each string in the array and concatenate it to the result string
        for string in modules:
            modules_str += ", " + string
        # Message content
        subject = "Test Email"
        body = f"""Dear {list},
        We hope this message finds you well. We are writing to inform you that the student, {student_name},
        is currently on academic probation. This is due to their GPA falling below the required threshold. These modules where taken {modules_str}. Academic probation is a serious matter as it can impact the student's academic progress and future opportunities.
        We strongly encourage {student_name} to take advantage of the resources available at our institution to improve their academic performance. This includes academic advising, tutoring services, and workshops on study skills and time management.
        We believe in {student_name}'s potential to improve and succeed in their studies. Please do not hesitate to reach out if you have any questions or need further information.

        Best regards, {school}"""

        # Set up the MIME structure
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the Mailtrap SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # server.starttls()
            # server.login(smtp_username, smtp_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
    return "Success"


# student_mail("Bigtester", "Email@here", "Utech", ["FIG", "JAG"])
# faculity_mail("Bigtester", "Utech", ["FIG", "JAG"])
# mailtest()
