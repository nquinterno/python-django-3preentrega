# Generated by Django 4.1.7 on 2023-06-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_proy_final', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='mail',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]
