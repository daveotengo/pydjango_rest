# Generated by Django 4.0.2 on 2022-02-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='email',
            field=models.EmailField(default='daveotengo@yahoo.com', max_length=10),
            preserve_default=False,
        ),
    ]
