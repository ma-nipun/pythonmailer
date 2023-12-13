# Email Sender Script

## Description

This Python script enables you to send HTML-formatted emails using the SMTP protocol. It utilizes the `smtplib` library
and the `email` module to construct and send emails with ease. The SMTP credentials are managed in a separate
configuration file named `config.py`.

## Prerequisites

Before using the script, make sure you have the following:

- Python installed on your system (version 3.x recommended).
- An active internet connection.
- Access to an SMTP server (e.g., Gmail) and the necessary credentials.

## Configuration

1. Create a file named `config.py` with the following structure:

```python
# config.py

class SmtpCredentials:
    server = "smtp.gmail.com"
    sender = "youremail@gmail.com"
    password = "yourapppassword"
    port = 465
```

Replace the placeholder values with your actual SMTP server details.

## Usage

1. Import the required modules and the `SmtpCredentials` class from `config.py`.

```python
from config import SmtpCredentials
```

2. Create an instance of `SmtpCredentials` by calling `SmtpCredentials()`.

```python
result = send_mail(SmtpCredentials(), "recipient@example.com")
print(result)
```

3. Customize the email content in the `send_mail` function, including the subject, HTML body, and attachments(TBD) if
   needed.

4. Run the script to send the email.

## Notes

- Ensure that your email provider allows access for less secure apps if you are using a Gmail account. Check your
  account settings for more information.

## License

This script is released under the [MIT License](LICENSE).

