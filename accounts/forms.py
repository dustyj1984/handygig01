from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import FormView
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image', 'bio', "location"]

class PaypalFormView(FormView):
    template_name = 'paypal_form.html'
    form_class = PayPalPaymentsForm

    def get_initial(self):
        return {
            "business": 'your-paypal-business-address@example.com',
            "amount": 20,
            "currency_code": "EUR",
            "item_name": 'Example item',
            "invoice": 1234,
            "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
            "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
            "lc": 'EN',
            "no_shipping": '1',
        }
