# utility.py

import configparser
import pathlib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP

def send_email(smtp_config: pathlib.Path, to_addresses: str, subject: str, body_text: str) -> None:
    config = configparser.ConfigParser()
    config.read(smtp_config)

    mail_server = config.get("SMTP Settings", "server")
    mail_port = config.get("SMTP Settings", "port")
    sender_email = config.get("SMTP Settings", "username")

    if "," in to_addresses:
        to_addresses = [a.strip() for a in to_addresses.split(",")]
    elif " " in to_addresses:
        to_addresses = [a.strip() for a in to_addresses.split(" ")]
    elif ";" in to_addresses:
        to_addresses = [a.strip() for a in to_addresses.split(";")]
    else:
        to_addresses = to_addresses.split()

    with SMTP(mail_server, mail_port) as server:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = ", ".join(to_addresses)
        msg["Subject"] = subject
        msg.attach(MIMEText(body_text, "plain"))
        server.sendmail(sender_email, to_addresses, msg.as_string())


def send_email_with_password(
    smtp_config: pathlib.Path, to_addresses: str, subject: str, body_text: str, password: str) -> None:
    config = configparser.ConfigParser()
    config.read(smtp_config)

    mail_server = config.get("SMTP Settings", "server")
    mail_port = config.get("SMTP Settings", "port")
    sender_email = config.get("SMTP Settings", "username")

    if "," in to_addresses:
        to_addresses = [a.strip() for a in to_addresses.split(",")]
    elif " " in to_addresses:
        to_addresses = [a.strip() for a in to_addresses.split(" ")]
    elif ";" in to_addresses:
        to_addresses = [a.strip() for a in to_addresses.split(";")]
    else:
        to_addresses = to_addresses.split()

    with SMTP(mail_server, mail_port) as server:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = ", ".join(to_addresses)
        msg["Subject"] = subject
        msg.attach(MIMEText(body_text, "plain"))
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, to_addresses, msg.as_string())
