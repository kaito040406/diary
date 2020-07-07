from django import forms

class DiaryForm(forms.Form):
  writer_name = forms.CharField(label='userNmae')
  diary = forms.CharField(label='body') 
  # user_id = forms.IntegerField(label='user_id')
  # category_id = forms.ForeignKey(label='category_id')
  commenter_name = forms.CharField(label='name')
  comment = forms.CharField(label='comment')

