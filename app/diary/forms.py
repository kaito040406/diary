from django import forms
from django.core.exceptions import ValidationError

class NameForm(forms.Form):
  user_name = forms.CharField(label='お名前：', required=False)

  def clean_user_name(self):
    user_name = self.cleaned_data['user_name']
    if user_name == "":
      raise forms.ValidationError("お名前を入力してください")
    elif len(user_name) >= 11:
      raise forms.ValidationError("10文字以内で入力してください")
    return user_name

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class DiaryForm(forms.Form):
  article = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'ここに記事を書いてください'}), label='',required=False) 

  def clean_article(self):
    article = self.cleaned_data['article']
    if article == "":
      raise forms.ValidationError("日誌を入力してください")
    elif len(article) >= 501:
      raise forms.ValidationError("全角500文字以内で入力してください")
    return article

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class CommnterName(forms.Form):
  commenter = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '名前'}),label='',required=False)

  def clean_commenter(self):
    commenter = self.cleaned_data['commenter']
    if commenter == "":
      raise forms.ValidationError("お名前を入力してください")
    elif len(commenter) >= 11:
      raise forms.ValidationError("10文字以内で入力してください")
    return commenter

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class CommentForm(forms.Form):
  comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'コメント'}), label='',required=False)

  def clean_comment(self):
    comment = self.cleaned_data['comment']
    if comment == "":
      raise forms.ValidationError("コメントを入力してください")
    elif len(comment) >= 501:
      raise forms.ValidationError("全角500文字以内で入力してください")
    return comment

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)
