from django.contrib import admin
from django.urls import path
from mail_app.views import get_mail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_mail/', get_mail.as_view())
]
