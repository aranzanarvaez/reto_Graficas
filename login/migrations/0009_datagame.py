# Generated by Django 4.0.3 on 2022-04-30 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_countryscores'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('level', models.IntegerField()),
                ('score', models.IntegerField()),
                ('lives', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]