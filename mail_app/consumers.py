import os

from channels.generic.websocket import WebsocketConsumer
from django.core.files.uploadedfile import SimpleUploadedFile
from dotenv import load_dotenv
from imap_tools import MailBox

from mail_app.models import Mail, MailFiles

load_dotenv()

IMAP_HOST = 'imap.mail.ru'  # IMAP хост mail.ru
IMAP_USER = os.getenv('IMAP_USER')
IMAP_PASSWORD = os.getenv('IMAP_PASSWORD')


class MailConsumer(WebsocketConsumer):
    """ Веб-сокет для получения объектов и сохранения их в БД. """
    def connect(self):
        self.accept()

    def disconnect(self, text_data):
        pass

    def receive(self, text_data):
        with MailBox(IMAP_HOST).login(IMAP_USER, IMAP_PASSWORD) as mailbox:
            for message in mailbox.fetch('UNSEEN'):
                obj, created = Mail.objects.get_or_create(
                    uid=message.uid,
                    subject=message.subject,
                    mail_from=message.from_,
                    date_time_sent=message.date,
                    body=message.text
                    )
                if not created:
                    raise ValueError('Письмо уже есть в БД.')
                if message.attachments:
                    for att in message.attachments:
                        file_object = SimpleUploadedFile(
                            att.filename,
                            att.payload,
                            att.content_type)
                        obj = MailFiles.objects.create(
                            file=file_object,
                            mail=obj
                        )
                        obj.save()
