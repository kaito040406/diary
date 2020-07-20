from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
import unicodedata
import re
from django.contrib.auth.forms import AuthenticationForm

class idForm(forms.Form):
  idForm = forms.CharField(label='',required=False)

  def clean_idForm(self):
    idForm = self.cleaned_data['idForm']
    if idForm == "":
      raise forms.ValidationError("IDを入力してください")
    elif len(idForm) >= 30 or len(idForm) <= 7:
      raise forms.ValidationError("6字以上17字以内で入力してください")
    elif re.match(r"^[\x20-\x7E]+$", idForm) == None or re.match(r"^\w+$", idForm) == None:
      if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", idForm) == None:
        raise forms.ValidationError("半角英数字で入力してください")
    return idForm

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class passForm(forms.Form):
  passForm = forms.CharField(label='',required=False)

  def clean_passForm(self):
    passForm = self.cleaned_data['passForm']
    if passForm == "":
      raise forms.ValidationError("パスワードを入力してください")
    elif len(passForm) >= 30 or len(passForm) <= 7:
      raise forms.ValidationError("8字以上30字以内で入力してください")
    elif re.match(r"^[\x20-\x7E]+$", passForm) == None or re.match(r"^\w+$", passForm) == None or re.search(r'\d', passForm) == None:
      if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", passForm) == None:
        raise forms.ValidationError("半角英数字で入力してください")
    return passForm

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class passForm_a(forms.Form):
  passForm_a = forms.CharField(label='',required=False)

  def clean_passForm_a(self):
    passForm_a = self.cleaned_data['passForm_a']
    if passForm_a == "":
      raise forms.ValidationError("パスワードを入力してください")
    elif len(passForm_a) >= 30 or len(passForm_a) <= 7:
      raise forms.ValidationError("8字以上30字以内で入力してください")
    elif re.match(r"^[\x20-\x7E]+$", passForm_a) == None or re.match(r"^\w+$", passForm_a) == None or re.search(r'\d', passForm_a) == None:
      if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", passForm_a) == None:
        raise forms.ValidationError("半角英数字で入力してください")
    return passForm_a

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class CustomAuthenticationForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)