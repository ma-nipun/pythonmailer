import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SmtpCredentials

port = 465

c = SmtpCredentials(
    server="smtp.gmail.com",
    sender="youremailgoeshere.com",
    password="yourapppasword",
    port=465
)


def send_mail(credentials, receiver):
    message = MIMEMultipart()
    message["From"] = credentials.sender
    message["To"] = receiver
    # customize your email
    message["Subject"] = f"Email Subject goes here"

    html = f"""\
        <html>
          <body>
            <p>This is a simple html section which will be used as the body of the email</p>
          </body>
        </html>
    """
    message.attach(MIMEText(html, "html"))

    # filename = f"- Credit Application - Automall Delivers.pdf"

    # Attach the PDF file
    # with open(attachments[0], "rb") as file:
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(file.read())
    #     encoders.encode_base64(part)
    #     part.add_header("Content-Disposition", f"attachment; filename={filename}")
    #     message.attach(part)

    text = message.as_string()

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(credentials.server, credentials.port, context=context) as server:
            server.login(credentials.sender, credentials.password)
            server.sendmail(credentials.sender, receiver, text)
        return "success"
    except Exception as e:
        return str(e)


result = send_mail(c, "mahela.nipun@gmail.com")
print(result)
