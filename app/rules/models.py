from django.db import models

# Create your models here.
class job_t_rule(models.Model):
  rule = models.CharField(max_length=1000,null=False)
  delete_frg = models.IntegerField(default=0,null=False)
  rule_create_day = models.DateTimeField('date published')
  rule_update_day = models.DateTimeField('date published')