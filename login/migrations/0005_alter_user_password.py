# Generated by Django 4.0.3 on 2022-04-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_rename_name_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
