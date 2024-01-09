from django import forms
from app.models import *


def validate_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('Started with a')

def validate_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is <= 5')

class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_a,validate_len])
    Sprincipal=forms.CharField(validators=[validate_a])
    Slocation=forms.CharField()
    email=forms.EmailField()
    confirmemail=forms.EmailField()

    def clean(self):
        e=self.cleaned_data['email']
        cm=self.cleaned_data['confirmemail']
        if e!=cm:
            raise forms.ValidationError('Emails are Mismatched!!!')

class WebForm(forms.Form):
    sn=[[to.Sname,to.Sname] for to in School.objects.all()]
    Sname=forms.ChoiceField(choices=sn)
    Scont=forms.IntegerField()
    Sadd=forms.CharField(validators=[validate_a])


    









    