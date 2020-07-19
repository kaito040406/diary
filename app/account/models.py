from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class job_t_user(models.Model):
  user_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=False)
  admin_level = models.IntegerField(null=False, default=1)
  del_flg = models.IntegerField(null=False,default=0)
  user_name = models.CharField(max_length=20,null=False)
  user_create_day = models.DateTimeField('date published')
  user_updata_day = models.DateTimeField('date published')

class job_t_a_picture(models.Model):
  pic_url = models.URLField(null=False)
  pic_diary_id = models.ForeignKey(job_t_user,on_delete=models.CASCADE,null=False)
  create_day = models.DateTimeField('date published')
  updata_day = models.DateTimeField('date published')
