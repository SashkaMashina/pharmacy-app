import aiosmtplib
from email.message import EmailMessage
from app.core.config import settings

SMTP_HOST = "smtp.yandex.ru"  # адрес SMTP-сервера
SMTP_PORT = 465
SMTP_USER = settings.SMTP_USER  # твоя почта
SMTP_PASSWORD = settings.SMTP_PASSWORD  # пароль от почты или специальный пароль приложений

FROM_EMAIL = settings.SMTP_USER  # от кого отправляем (обычно совпадает с SMTP_USER)

async def send_email(to_email: str, subject: str, body: str):
    message = EmailMessage()
    message["From"] = FROM_EMAIL
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    await aiosmtplib.send(
        message,
        hostname=SMTP_HOST,
        port=SMTP_PORT,
        username=SMTP_USER,
        password=SMTP_PASSWORD,
        use_tls=True,
    )