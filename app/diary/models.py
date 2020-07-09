from django.db import models
from django.contrib.auth.models import AbstractUser

class job_m_category(models.Model):
  category_lebel = models.IntegerField(null=False)
  parent_category_id = models.IntegerField(null=False)
  category_text = models.CharField(max_length=20, null=False)
  del_flg = models.IntegerField(null=False,default=0)
  create_day = models.DateTimeField('date published')
  updata_day = models.DateTimeField('date published')

class job_t_diary(models.Model):
  writer_name = models.CharField(max_length=20,null=False,error_messages={'required': '必須です!'})
  user_id = models.IntegerField(default=0,null=False)
  title = models.CharField(max_length=80,null=False,error_messages={'required': '必須です!'})
  diary = models.CharField(max_length=1000,null=False,error_messages={'required': '必須です!'})
  category_id = models.ForeignKey(job_m_category,on_delete=models.CASCADE,null=False)
  delete_frg = models.IntegerField(default=0,null=False)
  create_day = models.DateTimeField('date published')
  like_number = models.IntegerField(default=0)
  comment_number = models.IntegerField(default=0)

class job_t_comment(models.Model):
  commenter_name = models.CharField(max_length=20,null=False,error_messages={'required': '必須です!'})
  user_id = models.IntegerField(null=False)
  comment = models.CharField(max_length=1000,null=False,error_messages={'required': '必須です!'})
  delete_frg = models.IntegerField(default=0,null=False)
  comment_diary_id = models.ForeignKey(job_t_diary,on_delete=models.CASCADE,null=False)
  create_day = models.DateTimeField('date published')

class job_t_user(AbstractUser):
  admin_level = models.IntegerField(null=False, default=1)
  del_flg = models.IntegerField(null=False,default=0)
  user_name = models.CharField(max_length=20,null=False)
  user_create_day = models.DateTimeField('date published')
  user_updata_day = models.DateTimeField('date published')

# class job_t_school_rules(models.Model):
#   rule = models.CharField(null=False, max_length=100)
#   del_frg = models.IntegerField(null=False, default=0)
#   rule_create_day = models.DateTimeField('date published')
#   rule_updata_day = models.DateTimeField('date published')

class job_t_a_picture(models.Model):
  pic_url = models.URLField(null=False)
  pic_diary_id = models.ForeignKey(job_t_user,on_delete=models.CASCADE,null=False)
  create_day = models.DateTimeField('date published')
  updata_day = models.DateTimeField('date published')

class job_t_picture(models.Model):
  pic_url = models.URLField(null=False)
  pic_diary_id = models.ForeignKey(job_t_user,on_delete=models.CASCADE,null=False)
  create_day = models.DateTimeField('date published')
  updata_day = models.DateTimeField('date published')

# Create your models here.