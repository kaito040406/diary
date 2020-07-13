from django import forms
from django.core.exceptions import ValidationError

class NameForm(forms.Form):
  user_name = forms.CharField(label='お名前：', max_length=20, required=False)

  def clean_user_name(self):
    user_name = self.cleaned_data['user_name']
    if user_name == "":
      raise forms.ValidationError("お名前を入力してください")
    elif len(user_name) >= 21:
      raise forms.ValidationError("20文字以内で入力してください")
    return user_name

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class DiaryForm(forms.Form):
  article = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'ここに記事を書いてください'}), label='', max_length=1000,required=False) 

  def clean_article(self):
    article = self.cleaned_data['article']
    if article == "":
      raise forms.ValidationError("日誌を入力してください")
    elif len(article) >= 1001:
      raise forms.ValidationError("全角500文字以内で入力してください")
    return article

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class CommnterName(forms.Form):
  commenter = forms.CharField(label='名前：', max_length=20,required=True)

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class CommentForm(forms.Form):
  comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'コメント'}), label='', max_length=1000,required=True)

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)
