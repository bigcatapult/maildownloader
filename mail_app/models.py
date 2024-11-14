from django.db import models


class Mail(models.Model):
    """ Модель письма. """
    uid = models.PositiveIntegerField('uid', unique=True)
    subject = models.CharField('Тема сообщения', max_length=255)
    mail_from = models.CharField('Письмо от ', max_length=255)
    date_time_sent = models.DateTimeField('дата/время отправления письма')
    date_received = models.DateTimeField(
        'дата получения письма',
        auto_now_add=True
    )
    body = models.TextField('текст письма')

    def __str__(self):
        return self.subject


class MailFiles(models.Model):
    """ Связанная модель для сохранений вложений. """
    file = models.FileField(
        upload_to='media/',
        blank=True,
        null=True,
    )
    mail = models.ForeignKey(
        Mail,
        on_delete=models.CASCADE,
        related_name='mails',
        verbose_name='файл')

    file_url = models.URLField('скачать файл',
                               blank=True,
                               null=True)

    def save(self, *args, **kwargs):
        if self.file:
            self.file_url = self.file.url
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('file', 'mail')
