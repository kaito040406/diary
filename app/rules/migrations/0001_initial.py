# Generated by Django 2.2.3 on 2020-07-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_t_rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.CharField(max_length=1000)),
                ('delete_frg', models.IntegerField(default=0)),
                ('rule_create_day', models.DateTimeField(verbose_name='date published')),
                ('rule_update_day', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]