# Generated by Django 2.2.1 on 2019-08-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190812_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='tools',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='created_date',
        ),
        migrations.AddField(
            model_name='skill',
            name='tool',
            field=models.ManyToManyField(to='user.Tool'),
        ),
        migrations.AlterField(
            model_name='signupregistration',
            name='experience',
            field=models.FloatField(verbose_name=range(1, 100)),
        ),
    ]
