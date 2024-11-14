from django.contrib import admin

from mail_app.models import Mail, MailFiles


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    pass


@admin.register(MailFiles)
class MailFilesAdmin(admin.ModelAdmin):
    pass
