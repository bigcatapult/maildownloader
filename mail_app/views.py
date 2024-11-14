from django.views.generic import ListView

from mail_app.models import Mail


class get_mail(ListView):
    """
    Вью для отображения писем.
    """
    model = Mail

    template_name = 'in.html'
    context_object_name = 'mails'
