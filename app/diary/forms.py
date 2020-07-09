from django import forms

class nameForm(forms.Form):
  user_name = forms.CharField(label='名前：', max_length=20,required=True)

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super().__init__(*args, **kwargs)

class DiaryForm(forms.Form):
  article = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'ここに記事を書いてください'}), label='', max_length=1000,required=True) 

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