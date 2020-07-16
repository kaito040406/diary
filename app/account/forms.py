from django import forms
from django.core.exceptions import ValidationError
import unicodedata
import re

class idForm(forms.Form):
  idForm = forms.CharField(label='', max_length=30, min_length=6, required=False, attrs={'placeholder':'ID'})

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
  passForm = forms.CharField(label='', max_length=30, min_length=8, required=False, attrs={'placeholder':'パスワード'})

  def clean_passForm(self):
    passForm = self.cleaned_data['passForm']
    if passForm == "":
      raise forms.ValidationError("IDを入力してください")
    elif len(passForm) >= 30 or len(passForm) <= 7:
      raise forms.ValidationError("8字以上30字以内で入力してください")
    elif re.match(r"^[\x20-\x7E]+$", passForm) == None or re.match(r"^\w+$", passForm) == None or re.search(r'\d', passForm) == None:
      if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", passForm) == None:
        raise forms.ValidationError("半角英数字で入力してください")
    return passForm

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)