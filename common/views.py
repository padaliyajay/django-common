from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'common/contact_form.html'

    def form_valid(self, form):
        send_mail(
            subject = form.fields['subject'],
            message = form.fields['message'],
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list = (form.fields['email'],),
        )

        messages.success(self.request, 'Success: your message successfully sent')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact')
