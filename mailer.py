import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


port = 465
# subject = "An email with attachment from Python"
# body = "This is an email with attachment sent from Python"
smtp_server = "smtp.gmail.com"
sender_email = "supermhmni@gmail.com"
receiver_email = "mahela.nipun@gmail.com"
password = "sgg"
name = "Mahela N. Indeewara"


def send_mail(item, attachments=[]):
    subject = f"{item[1]} - {name}"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = item[2]
    message["Subject"] = subject

    html = f"""\
        <html>
          <body>
            <p>I am writing to express my keen interest in the {item[1]} opportunities at {item[0]}. I am eager to bring my strategic vision and technical expertise to your organization.I am confident that my skills align with your goals. I look forward to the opportunity to contribute to the continued success of {item[0]} and discuss how my experience can benefit your team.</p>
            <p>Please find the attached cv for your reference. and if you need more information on what my skills are feel free to contact me.</p>
            <p>Thank you for your time and consideration<br>
                {name}</p>
          </body>
        </html>
    """

    filename = f"- Credit Application - Automall Delivers.pdf"

    message.attach(MIMEText(html, "html"))

    # Attach the PDF file
    with open(attachments[0], "rb") as file:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        message.attach(part)

    text = message.as_string()

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        return "success"
    except Exception as e:
        return str(e)

# Call the function with your data

# result = send_mail(["table.sql"])
# print(result)
