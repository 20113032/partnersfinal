#files.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from posts.models import Project

class RegistrationForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Name"))
    lastname = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Last name"))
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("ID"), error_messages={ 'invalid': _("Username can only have letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    CHOICES = [("1", "Investor"), ("2", "Entreprenuer")]
    usertype = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label=_("User type"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("Username already exists."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The passwords don't match."))
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        types=kwargs.pop('types', None)
        super(RegistrationForm, self).__init__(*args, **kwargs)
        if types:
            self.fields['usertype'].choices = types

class CreateForm(forms.Form):
    projectname = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=100)), label=_("Project Name"))
    description = forms.CharField(widget=forms.Textarea(attrs=dict(required=True, max_length=2000)), label=_("Description"))
    value = forms.DecimalField(widget=forms.NumberInput(attrs=dict(required=True, max_digits=12, max_decimal_places=2)), label=_("Goal in $"))

    def clean_projectname(self):
        try:
            project = Project.objects.get(projectname__iexact=self.cleaned_data['projectname'])
        except Project.DoesNotExist:
            return self.cleaned_data['projectname']
        raise forms.ValidationError(_("Projectname already exists."))

class MessageForm(forms.Form) :
    title = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Subject"))
    message = forms.CharField(widget=forms.Textarea(attrs=dict(required=True, max_length=2000)), label=_("Message"))

class AnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(attrs=dict(required=True, max_length=2000)), label=_("Answer"))

class PaymentForm(forms.Form):
    ammount = forms.DecimalField(widget=forms.NumberInput(attrs=dict(required=True, max_digits=12, max_decimal_places=2)), label=_("Ammount in $"))
