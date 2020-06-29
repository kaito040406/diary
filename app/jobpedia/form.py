from django import forms

class DiaryForm(forms.Form):
  name = forms.CharField(label='userNmae')
  text = forms.CharField(label='body') 